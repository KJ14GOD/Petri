import dotenv from 'dotenv';
dotenv.config();

import bolt from '@slack/bolt';
const { App, LogLevel } = bolt;

const app = new App({
  appToken: process.env.SLACK_APP_TOKEN,
  token: process.env.SLACK_BOT_TOKEN, 
  socketMode: true,
  logLevel: LogLevel.INFO,
});

app.event('app_mention', async ({ event, client, logger }) => {
    logger.info(`got app_mention from ${event.user} in ${event.channel}`);
    try {
    const threadTs = event.thread_ts || event.ts;
    await client.chat.postMessage({
      channel: event.channel, thread_ts: event.thread_ts || event.ts, text: 'Hi! from CalHacks'
    });
  } catch (error) {
    logger.error('Failed to post reply', error);
  }
});

async function start() {
  const port = process.env.PORT || 3000;
  await app.start(port);
  // eslint-disable-next-line no-console
  console.log(`Slack bot is running (Socket Mode) on port ${port}`);
}

start();

