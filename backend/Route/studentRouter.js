const studentRouter = require('express').Router();

const express = require("express");
const {
  getAllStudents,
  getStudentById,
  studentLogIn
} = require("../controllers/studentControllers");


studentRouter.route("/").get(getAllStudents);

studentRouter.route("/:id").get(getStudentById);

studentRouter.post("/login", studentLogIn);

module.exports = studentRouter;