const mongoose = require("mongoose");

const studentSchema = new mongoose.Schema(
    {
    user: {
            type: mongoose.Schema.Types.ObjectId,
            required: true,
            ref: "User",
    },
    class: { 
        type: String, 
        required: true, 
        trim: true 
    },
  },
  {
    timestamps: true,
  });

  module.exports = mongoose.model("Student", studentSchema);