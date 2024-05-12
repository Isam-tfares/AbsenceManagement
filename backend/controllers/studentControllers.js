const asynchandler = require("express-async-handler");
const Student = require("../models/studentModel");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");


//@des login student
//@route POST /student/login
//@access public
const studentLogIn = asynchandler(async (req, res) => {

  const { email, password } = req.body;

  if (!email || !password) {
    res.status(400);
    throw new Error("all fields are mandatory");
  }

  const student = await Student.findOne({ email });

  const verifyPassword = (password == student.password);

  // if (student && verifyPassword) {
  //   const accessToken = jwt.sign(
  //     {
  //       student: {
  //         fullName: student.fullName,
  //         email: student.email,
  //         id: student.id,
  //       },
  //     },
  //     process.env.access_token
  //   );
  //   res.status(200).json({ accessToken });
  // } else {
  //   res.status(401);
  //   throw new Error("email or password is not valid");
  // }

  if(student && verifyPassword){
    res.status(200).json({"message " : "login successfully"});
  }else{
    res.status(401);
    throw new Error("email or password is not valid");
    
  }
});


//@des get all students
//@route GET /student
//@access private
const getAllStudents = asynchandler(async (req, res) => {
    const students = await Student.find();
    res.status(200).json(students);

    // const newstudent = await Student.create({
      
    //     fullName: "etudiant 1",
    //     email: "etudiant1@example.com",
    //     password: "mot_de_passe etudiant1",
    //     class: "Nom de la Classe etudiant1"
    // })
    // res.status(201).json(newstudent);
  });


//@des get student
//@route GET /student/:id
//@access private
const getStudentById = asynchandler(async (req, res) => {
    const student = await Student.findById(req.params.id);
  
    if (!student) {
      res.status(404);
      throw new Error("student not found");
    }
    res.status(200).json(student);

  });

  module.exports = {
    getAllStudents,
    getStudentById,
    studentLogIn
  }