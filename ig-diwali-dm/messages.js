// Copy for the Diwali Kit comment-to-DM automation.
// Edit freely — nothing else needs to change.

export const LINK = 'https://tendsmall.com/diwali-kit';

// Public replies under the comment. Several variants are rotated so Instagram
// doesn't treat a wall of identical replies as spam.
export const COMMENT_REPLIES = [
  'Thanks for the comment ✨ Please check your DMs for the link.',
  'Thank you for this 🪔 We\'ve sent the link to your DMs.',
  'Thanks for commenting ✨ The link is waiting in your DMs.',
  'Thank you 🪔 Please check your DMs for the link.',
];

// Private reply (DM). {name} is replaced with the commenter's @username.
export const DM_TEMPLATE = `Hi {name}, thank you for commenting 🪔

Here's your link to the TENDS Diwali Kit:
${LINK}

Wishing you and your little one a calm, bright Diwali — full of light, closeness and the small rituals that make the day yours.

Happy Diwali ✨
✦ Small breed only. Big care always.`;

export function pickCommentReply(seed) {
  let h = 0;
  for (const c of String(seed)) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return COMMENT_REPLIES[h % COMMENT_REPLIES.length];
}

export function buildDm(username) {
  return DM_TEMPLATE.replace('{name}', username ? `@${username}` : 'there');
}
