const asynchandler = require("express-async-handler");

//@des get all Teacher
//@route GET /teacher
//@access private

const getAllTeachers = asynchandler(async (req, res) => {
    // const contacts = await Teacher.find({ user_id: req.user.id });
    // res.status(200).json(contacts);
    res.status(200).json({
        "getAllTeachers" : true
    })
  });


//@des get teacher
//@route GET /teacher/:id
//@access private

const getTeacherById = asynchandler(async (req, res) => {
    // const teacher = await Teacher.findById(req.params.id);
  
    // if (!teacher) {
    //   res.status(404);
    //   throw new Error("teacher not found");
    // }
    // res.status(200).json(teacher);
    res.status(200).json({
        "Teacher by id" : req.params.id
    })
  });

  module.exports = {
    getTeacherById,
    getAllTeachers
  }