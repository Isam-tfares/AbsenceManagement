const mongoose = require("mongoose");

const teacherSchema = new mongoose.Schema(
    {
    user: {
            type: mongoose.Schema.Types.ObjectId,
            required: true,
            ref: "User",
    },
    Departement : { 
        type: String, 
        required: true, 
        trim: true 
    },
  },
  {
    timestamps: true,
  });

  module.exports = mongoose.model("Teacher", teacherSchema);