require("dotenv").config();
const mongoose = require("mongoose");
const username = encodeURIComponent(process.env.USERNAME);
const password = encodeURIComponent(process.env.PASSWORD);
const url = `mongodb+srv://${username}:${password}@cluster0.hxavevb.mongodb.net/alltrails`;
mongoose
  .connect(url, { useNewUrlParser: true })
  .then(() => {
    console.log("DB connected");
  })
  .catch((error) => console.log(error));
