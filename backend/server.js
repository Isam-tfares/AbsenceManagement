const express = require("express");
const dotenv = require("dotenv").config();
const connectToDb = require("./Config/dbConnection");

const app = express();
app.use(express.json());

connectToDb();


app.use('/teacher',require("./Route/teacherRouter"));
app.use('/student',require("./Route/studentRouter"));
app.use('/module',require("./Route/moduleRouter"));
// app.use('/admin',adminRouter);


const PORT = process.env.PORT || 3000 ;

app.listen(PORT, () => {
  console.log(
    `server running on port : ${PORT} ...... `
  );
});
