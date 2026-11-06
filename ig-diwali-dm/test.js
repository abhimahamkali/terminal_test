import { test } from 'node:test';
import assert from 'node:assert/strict';
import { handleComment } from './server.js';
import { buildDm, COMMENT_REPLIES, LINK } from './messages.js';

function deps() {
  const calls = [];
  return {
    calls,
    ig: async (path, opts) => calls.push({ path, ...opts }),
    ownUserId: '111',
    targetMediaId: 'MEDIA',
    processed: new Set(),
    save: () => {},
  };
}

const comment = { id: 'c1', text: 'Love this!', from: { id: '222', username: 'priya' }, media: { id: 'MEDIA' } };

test('sends DM with link and a public reply', async () => {
  const d = deps();
  assert.equal(await handleComment(comment, d), 'handled');
  assert.equal(d.calls.length, 2);
  assert.deepEqual(d.calls[0].body.recipient, { comment_id: 'c1' });
  assert.match(d.calls[0].body.message.text, /@priya/);
  assert.ok(d.calls[0].body.message.text.includes(LINK));
  assert.match(d.calls[0].body.message.text, /Diwali/);
  assert.equal(d.calls[1].path, '/c1/replies');
  assert.ok(COMMENT_REPLIES.includes(d.calls[1].body.message));
});

test('skips duplicates, other posts, own comments and replies', async () => {
  const d = deps();
  await handleComment(comment, d);
  assert.equal(await handleComment(comment, d), 'duplicate');
  assert.equal(await handleComment({ ...comment, id: 'c2', media: { id: 'X' } }, d), 'other-post');
  assert.equal(await handleComment({ ...comment, id: 'c3', from: { id: '111' } }, d), 'own-comment');
  assert.equal(await handleComment({ ...comment, id: 'c4', parent_id: 'c1' }, d), 'reply-thread');
  assert.equal(d.calls.length, 2);
});

test('DM falls back when username missing', () => {
  assert.match(buildDm(undefined), /^Hi there/);
});
