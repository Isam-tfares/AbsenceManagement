const mongoose = require("mongoose");

const connectToDb = async () => {
  try {
    const connect = await mongoose.connect(process.env.connection_db);
    console.log(
      "connection db : ",
      connect.connection.host,
      connect.connection.name
    );
  } catch (err) {
    console.log(err);
    process.exit(1);
  }
};


module.exports = connectToDb;