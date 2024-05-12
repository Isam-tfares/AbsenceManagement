const asynchandler = require("express-async-handler");

//@des get all students
//@route GET /student
//@access private

const getAllStudents = asynchandler(async (req, res) => {
    // const contacts = await Teacher.find({ user_id: req.user.id });
    // res.status(200).json(contacts);
    res.status(200).json({
        "getAllStudents" : true
    })
  });


//@des get student
//@route GET /student/:id
//@access private

const getStudentById = asynchandler(async (req, res) => {
    // const teacher = await Teacher.findById(req.params.id);
  
    // if (!teacher) {
    //   res.status(404);
    //   throw new Error("teacher not found");
    // }
    // res.status(200).json(teacher);
    res.status(200).json({
        "student by id" : req.params.id
    })
  });

  module.exports = {
    getAllStudents,
    getStudentById
  }