const teacherRouter = require('express').Router();

const express = require("express");
const {
  getAllTeachers,
  getTeacherById,
} = require("../controllers/teacherControllers");


teacherRouter.route("/").get(getAllTeachers);

teacherRouter.route("/:id").get(getTeacherById);
teacherRouter.route("absence/:id").get(getTeacherById);

module.exports = teacherRouter;

