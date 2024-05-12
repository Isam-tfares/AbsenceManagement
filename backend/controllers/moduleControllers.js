const asynchandler = require("express-async-handler");

//@des get all modules
//@route GET /module/
//@access private

const getAllModules = asynchandler(async (req, res) => {
    res.status(200).json({
        "getAllModules" : true
    })
  });


//@des get module
//@route GET /module/:id
//@access private

const getModuleByprofId = asynchandler(async (req, res) => {
    res.status(200).json({
        "getModuleByprofId" : req.params.id
    })
  });


//@des get module
//@route GET /module/:id
//@access private

const getModuleByClass = asynchandler(async (req, res) => {
    res.status(200).json({
        "getModuleByClass" : req.params.id
    })
  });


//@des get module
//@route GET /module/:id
//@access private

const getModuleById = asynchandler(async (req, res) => {
    res.status(200).json({
        "getModuleById" : req.params.id
    })
  });

  module.exports = {
    getAllModules,
    getModuleByprofId,
    getModuleByClass,
    getModuleById
  }