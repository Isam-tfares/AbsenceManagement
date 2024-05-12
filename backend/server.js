const express = require("express");

const app = express();


PORT = process.env.PORT || 3000 ;


app.use('/students',studentRouter);
app.use('/teacher',teacherRouter);
app.use('/admin',adminRouter);

app.listen(PORT, () => {
  console.log(
    `server running on port : ${PORT} ...... `
  );
});
