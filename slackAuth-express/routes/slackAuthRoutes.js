import { Router } from 'express'
import { slackAuth, slackRedirect } from '../controller/slackAuthController.js';

const router = Router();

router.get("/", slackAuth);
router.get("/callback", slackRedirect);

export default router;