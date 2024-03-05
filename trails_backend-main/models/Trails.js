const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const TrialsSchema = new Schema({
  state: String,
  name: String,
  location: String,
  coords: Array,
  trailsNum: Number,
  totalDistance: String,
  ranking: Number,
  trailDifficultyList: Object,
});

const Trials = mongoose.model("Trials", TrialsSchema);
module.exports = Trials;
