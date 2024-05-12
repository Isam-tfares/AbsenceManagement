const mongoose = require("mongoose");

const userSchema = mongoose.Schema(
  {
    fullName: {
      type: String,
      required: [true, "fullName is required"],
    },
    email: {
      type: String,
      required: [true, "please add the email"],
      unique: [true, "email adress already taken"],
    },
    password: {
      type: String,
      required: [true, "please enter the password"],
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("User", userSchema);