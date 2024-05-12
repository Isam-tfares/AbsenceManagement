const studentRouter = require('express').Router();

const express = require("express");
const {
  getAllStudents,
  getStudentById,
} = require("../controllers/studentControllers");


studentRouter.route("/").get(getAllStudents);

studentRouter.route("/:id").get(getStudentById);

module.exports = studentRouter;