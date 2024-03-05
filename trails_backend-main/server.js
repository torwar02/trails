const express = require("express");
const cors = require("cors");

require("./config/db");
const app = express();
const port = 3000;

const UserRouter = require("./api/User");
const TrialsRouter = require("./api/Trails");
const bodyParser = require("express").json;
app.use(
  cors({
    origin: "http://localhost:5173",
    methods: ["GET", "POST"],
  })
);
app.use(bodyParser());
app.use("/users", UserRouter);
app.use("/trails", TrialsRouter);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
