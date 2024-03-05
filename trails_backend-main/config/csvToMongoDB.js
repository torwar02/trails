require("./db");
const fs = require("fs");
const csv = require("csv-parser");

const Trials = require("../models/Trails");
const csvFilePath = "config/data/California.csv";

async function processCSV() {
  try {
    fs.createReadStream(csvFilePath)
      .pipe(csv())
      .on("data", async (row) => {
        let {
          Name: name,
          Location: location,
          Coords: coords,
          "Trails (view details)": trailsNum,
          "Total Distance": totalDistance,
          "State Ranking": ranking,
          "Access Road/Trail": accessRoad,
          White: white,
          Green: green,
          Blue: blue,
          Black: black,
          "Double Black Diamond": doubleBlackDiamond,
          Proline: proline,
        } = row;
        location = location.split(",")[0];
        coords = coords.replace(/[() ]/g, "").split(",").map(parseFloat);
        trailsNum = parseInt(trailsNum, 10);
        ranking = parseInt(ranking.replace(/[^0-9]/g, ""), 10);
        const trailDifficultyList = {
          accessRoad: Number(accessRoad),
          white: Number(white),
          green: Number(green),
          blue: Number(blue),
          black: Number(black),
          doubleBlackDiamond: Number(doubleBlackDiamond),
          proline: Number(proline),
        };
        const newTrail = new Trials({
          state: "California",
          name,
          location,
          coords,
          trailsNum,
          totalDistance,
          ranking,
          trailDifficultyList,
        });
        newTrail.save().catch((err) => {
          throw Error(err);
        });
      });
  } catch (error) {
    console.log("Error processing csv", error);
  }
}

processCSV();
