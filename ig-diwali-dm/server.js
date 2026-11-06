// Instagram comment -> public reply + DM automation for one post.
// Zero dependencies. Requires Node 18+.
//
// Flow: someone comments on the target reel -> Instagram sends a webhook ->
// we reply under their comment and send them a private reply (DM) with the link.

import http from 'node:http';
import crypto from 'node:crypto';
import fs from 'node:fs';
import { pickCommentReply, buildDm } from './messages.js';

const {
  IG_ACCESS_TOKEN,          // Instagram User access token (instagram_business_basic,
                            // instagram_business_manage_comments, instagram_business_manage_messages)
  IG_APP_SECRET,            // App secret, used to verify webhook signatures
  IG_VERIFY_TOKEN,          // Any string; must match what you enter in the Meta dashboard
  TARGET_SHORTCODE = 'DfZxuwOoz4J',
  TARGET_MEDIA_ID,          // Optional: skip lookup if you already know the media ID
  PORT = 3000,
  DRY_RUN,                  // Set to 1 to log instead of calling Instagram
  STATE_FILE = new URL('./processed.json', import.meta.url).pathname,
} = process.env;

const GRAPH = 'https://graph.instagram.com/v21.0';

// ---------- state (so a comment is never handled twice) ----------
const processed = new Set(
  fs.existsSync(STATE_FILE) ? JSON.parse(fs.readFileSync(STATE_FILE, 'utf8')) : [],
);
const save = () => fs.writeFileSync(STATE_FILE, JSON.stringify([...processed]));

// ---------- Instagram API ----------
async function ig(path, { method = 'GET', body } = {}) {
  if (DRY_RUN && method !== 'GET') {
    console.log('[dry-run]', method, path, JSON.stringify(body));
    return {};
  }
  const res = await fetch(`${GRAPH}${path}`, {
    method,
    headers: { Authorization: `Bearer ${IG_ACCESS_TOKEN}`, 'Content-Type': 'application/json' },
    body: body && JSON.stringify(body),
  });
  const json = await res.json();
  if (!res.ok) throw new Error(`${method} ${path} -> ${res.status} ${JSON.stringify(json.error ?? json)}`);
  return json;
}

let ownUserId;
let targetMediaId = TARGET_MEDIA_ID;

async function init() {
  const me = await ig('/me?fields=user_id,username');
  ownUserId = String(me.user_id ?? me.id);
  console.log(`Logged in as @${me.username} (${ownUserId})`);

  if (!targetMediaId) {
    let url = '/me/media?fields=id,shortcode,permalink&limit=50';
    while (url && !targetMediaId) {
      const page = await ig(url);
      const hit = page.data?.find(
        (m) => m.shortcode === TARGET_SHORTCODE || m.permalink?.includes(TARGET_SHORTCODE),
      );
      if (hit) targetMediaId = hit.id;
      url = page.paging?.next?.replace(GRAPH, '');
    }
    if (!targetMediaId) throw new Error(`Post ${TARGET_SHORTCODE} not found on this account`);
  }
  console.log(`Watching media ${targetMediaId} (${TARGET_SHORTCODE})`);
}

// ---------- core logic ----------
export async function handleComment(c, deps = { ig, ownUserId, targetMediaId, processed, save }) {
  const { id, text, from, media, parent_id } = c;
  if (!id || deps.processed.has(id)) return 'duplicate';
  if (media?.id !== deps.targetMediaId) return 'other-post';
  if (from?.id === deps.ownUserId) return 'own-comment';   // never answer ourselves (avoids loops)
  if (parent_id) return 'reply-thread';                     // only top-level comments

  deps.processed.add(id);
  deps.save();
  console.log(`Comment ${id} from @${from?.username}: ${text}`);

  // DM first: it's the part that matters, and the window is 7 days / 1 message per comment.
  try {
    await deps.ig('/me/messages', {
      method: 'POST',
      body: { recipient: { comment_id: id }, message: { text: buildDm(from?.username) } },
    });
  } catch (e) {
    console.error('DM failed:', e.message);
  }
  try {
    await deps.ig(`/${id}/replies`, { method: 'POST', body: { message: pickCommentReply(id) } });
  } catch (e) {
    console.error('Comment reply failed:', e.message);
  }
  return 'handled';
}

function validSignature(raw, header) {
  if (!IG_APP_SECRET) return true;
  if (!header) return false;
  const expected = 'sha256=' + crypto.createHmac('sha256', IG_APP_SECRET).update(raw).digest('hex');
  const a = Buffer.from(expected);
  const b = Buffer.from(header);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

// ---------- HTTP server ----------
function start() {
  http
    .createServer(async (req, res) => {
      const url = new URL(req.url, 'http://x');

      if (req.method === 'GET' && url.pathname === '/webhook') {
        const ok =
          url.searchParams.get('hub.mode') === 'subscribe' &&
          url.searchParams.get('hub.verify_token') === IG_VERIFY_TOKEN;
        res.writeHead(ok ? 200 : 403).end(ok ? url.searchParams.get('hub.challenge') : 'forbidden');
        return;
      }

      if (req.method === 'POST' && url.pathname === '/webhook') {
        const chunks = [];
        for await (const ch of req) chunks.push(ch);
        const raw = Buffer.concat(chunks);
        if (!validSignature(raw, req.headers['x-hub-signature-256'])) {
          res.writeHead(401).end();
          return;
        }
        res.writeHead(200).end('EVENT_RECEIVED'); // ack fast, then work
        const payload = JSON.parse(raw.toString() || '{}');
        for (const entry of payload.entry ?? []) {
          for (const change of entry.changes ?? []) {
            if (change.field !== 'comments') continue;
            handleComment(change.value, { ig, ownUserId, targetMediaId, processed, save })
              .then((r) => r !== 'handled' && console.log(`skip ${change.value?.id}: ${r}`))
              .catch((e) => console.error(e));
          }
        }
        return;
      }

      res.writeHead(url.pathname === '/' ? 200 : 404).end('ok');
    })
    .listen(PORT, () => console.log(`Listening on :${PORT} — webhook at /webhook`));
}

if (import.meta.url === `file://${process.argv[1]}`) {
  for (const k of ['IG_ACCESS_TOKEN', 'IG_VERIFY_TOKEN']) {
    if (!process.env[k]) throw new Error(`Missing env var ${k}`);
  }
  await init();
  start();
}
