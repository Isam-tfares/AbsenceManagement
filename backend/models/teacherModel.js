const mongoose = require("mongoose");

const teacherSchema = new mongoose.Schema(
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
    Departement : { 
        type: String, 
        required: true, 
        trim: true 
    },
    attendance: [{
      date: {
          type: Date,
          required: true
      },
      status: {
          type: String,
          enum: ['Present', 'Absent'],
          required: true
      },
      Module: {
          type: mongoose.Schema.Types.ObjectId,
          ref: 'subject',
          required: true
      }
    }]
  },
  {
    timestamps: true,
  });

  module.exports = mongoose.model("Teachers", teacherSchema);