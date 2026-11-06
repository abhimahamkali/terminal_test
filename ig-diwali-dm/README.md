# Diwali Kit — Instagram comment → DM automation

When someone comments on the reel https://www.instagram.com/reel/DfZxuwOoz4J/ this service:

1. **Sends them a DM** (an Instagram "private reply") thanking them, with the link https://tendsmall.com/diwali-kit and a Diwali wish.
2. **Replies under their comment**, e.g. *"Thanks for the comment ✨ Please check your DMs for the link."* (four versions take turns so Instagram doesn't flag the replies as spam).

It skips your own comments, replies inside comment threads, comments on other posts, and comments it has already handled.

You can change the wording in `messages.js`.

## Setup (about 20 minutes)

You need an Instagram **Business or Creator** account.

1. **Create a Meta app** at https://developers.facebook.com/apps → type *Business* → add the **Instagram** product → choose *API setup with Instagram login*.
2. **Generate a token**: in *Instagram → API setup*, add your account and generate an access token. It needs the permissions
   `instagram_business_basic`, `instagram_business_manage_comments` and `instagram_business_manage_messages`.
3. In the Instagram app, go to **Settings → Messages and story replies → Message controls → Connected tools** and turn on **Allow access to messages**.
4. **Deploy the server** anywhere with a public HTTPS URL (Render, Railway, Fly.io, a VPS, or `ngrok http 3000` for a quick test):
   ```bash
   export IG_ACCESS_TOKEN=...      # from step 2
   export IG_APP_SECRET=...        # App settings → Basic → App secret
   export IG_VERIFY_TOKEN=any-random-string
   npm start
   ```
   When it starts, it finds the reel by its code (`DfZxuwOoz4J`) and prints its media ID.
5. **Set up the webhook**: in *Instagram → API setup → Configure webhooks*, set the callback URL to `https://YOUR-HOST/webhook` and the verify token to your `IG_VERIFY_TOKEN`. Then subscribe to the **comments** field.
6. **Turn on Live mode** for the app. While the app is in Development mode, only people with a role on the app (admins and testers) trigger webhooks. To reach the public you need Advanced Access to the permissions above, which requires Meta App Review.

Test it safely first with `DRY_RUN=1 npm start`. This logs what it would send without posting anything.

## Instagram limits to know

- You can send **one DM per comment**, and only **within 7 days** of the comment. After that, Instagram doesn't allow the DM.
- If the commenter has never messaged you, the DM may land in their **Message Requests** folder. That's why the public reply tells them to check their DMs.
- The service handles comments made **while it is running**. It does not go back to earlier comments.

## Tests

```bash
npm test
```
