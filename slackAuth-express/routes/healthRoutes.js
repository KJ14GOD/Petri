import { Router } from 'express'
import { dataCheck, status } from '../controller/healthController.js';

const router = Router();

router.get("/", status);
router.post("/api/data", dataCheck);

export default router;