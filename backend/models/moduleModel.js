const mongoose = require("mongoose");

const ModuleSchema = new mongoose.Schema({
    ModName: {
        type: String,
        required: true,
    },
    ModclassName: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Class',
        required: true,
    },
    teacher: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Teachers',
    }
}, { 
    timestamps: true 
})
module.exports = mongoose.model("Modules", teacherSchema);