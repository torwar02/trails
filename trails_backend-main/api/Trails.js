const express = require("express");
const router = express.Router();

const Trials = require("../models/Trails");

router.post("/list", async (req, res) => {
  let { state, pageSize, curPage } = req.body;
  pageSize = parseInt(pageSize, 10);
  curPage = parseInt(curPage, 10);
  try {
    const query = state ? { state } : {};
    const totalCount = await Trials.countDocuments(query);
    const trails = await Trials.find(query)
      .limit(pageSize)
      .skip((curPage - 1) * pageSize)
      .exec();
    const totalPages = Math.ceil(totalCount / pageSize);
    res.json({
      pageVO: {
        pageSize,
        curPage,
        totalCount,
        totalPages,
      },
      data: trails,
    });
  } catch (error) {
    res.json({
      status: "FAILED",
      message: "An error occurred while checking for existing user!",
      err: error,
    });
  }
});

module.exports = router;
