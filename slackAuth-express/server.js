import express from "express";
import cors from "cors";


import healthRoutes from './routes/healthRoutes.js'
import slackAuthRoutes from './routes/slackAuthRoutes.js'

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.use('/', healthRoutes);
app.use('/auth/slack', slackAuthRoutes)

app.listen(PORT, () => {
  console.log(`Server listening on Port ${PORT}`);
});
