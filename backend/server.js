const express = require("express");

const app = express();


PORT = process.env.PORT || 3000 ;

app.use('/teacher',require("./Route/teacherRouter"));
app.use('/student',require("./Route/studentRouter"));
// app.use('/admin',adminRouter);

app.listen(PORT, () => {
  console.log(
    `server running on port : ${PORT} ...... `
  );
});
