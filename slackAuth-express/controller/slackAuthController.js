import axios from "axios";
import dotenv from 'dotenv';

dotenv.config();

const slackAuth = (req, res) => {
    const scopes = "channels:read";
    res.redirect(
        `https://slack.com/oauth/v2/authorize?client_id=${
            process.env.SLACK_CLIENT_ID
        }&user_scope=${
            encodeURIComponent(scopes)
        }&redirect_uri=${
            process.env.SLACK_REDIRECT_URI
        }`
    )
}

const slackRedirect = async (req, res) => {
    const { code } = req.query; //authorization code from slack
    try {
        const tokenResponse = await axios.post(
            "https://slack.com/api/oauth.v2.access",
            null,
            {
                params: {
                    code,
                    client_id: process.env.SLACK_CLIENT_ID,
                    client_secret: process.env.SLACK_CLIENT_SECRET,
                    redirect_uri: process.env.SLACK_REDIRECT_URI
                }
            }
        )

        if(tokenResponse.data.ok) {
            const accessToken = tokenResponse.data.authed_user.access_token
            console.log(accessToken);
            console.log(tokenResponse.data.authed_user.slack_user_id)

            const channelsResponse = await axios.get("https://slack.com/api/conversations.list",
                {
                    headers: {
                        Authorization: `Bearer ${accessToken}`,
                    }
                }
            );

            if(channelsResponse) {
                const channels = channelsResponse.data.channels.map((channel) => channel.name).join(", ")
                console.log(channels);
                res.status(200).send(channels)
            } else {
                res.status(500).send('Error getting Slack Channels' + channelsResponse.data.error)
            }
        } else {
            res.status(500).send('Error fetching token' + tokenResponse.data.error);
        }
    }
    catch (error) {
        console.log(error);
        res.status(500).send('Error fetching token or getting channels')
    }

}

export {
    slackAuth,
    slackRedirect
}