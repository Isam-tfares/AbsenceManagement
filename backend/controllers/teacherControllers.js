const asynchandler = require("express-async-handler");
const Teacher = require('../models/teacherModel')

//@des get all Teacher
//@route GET /teacher
//@access private

const getAllTeachers = asynchandler(async (req, res) => {
    const teachers = await Teacher.find();
    res.status(200).json(teachers);
  });


//@des get teacher absence
//@route GET /teacher/:id
//@access private

const getTeacherById = asynchandler(async (req, res) => {
    const teacher = await Teacher.findById(req.params.id);
  
    if (!teacher) {
      res.status(404);
      throw new Error("teacher not found");
    }
    res.status(200).json(teacher);
  });


//@des get teacher Absence
//@route GET /teacher/absence/:id
//@access private

const getTeacherAbsenceById = asynchandler(async (req, res) => {
  res.status(200).json({
      "Teacher absence by id" : req.params.id
  })
});



  module.exports = {
    getTeacherById,
    getAllTeachers,
    getTeacherAbsenceById
  }