
const status = (req, res) => {
  res.json({ message: "Server is running" });
}

const dataCheck = (req, res) => {
  const { name } = req.body;
  res.json({ message: `Hello, ${name}!` });
}

export {
    status,
    dataCheck
}