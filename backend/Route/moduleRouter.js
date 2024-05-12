const moduleRouter = require('express').Router();

const express = require("express");
const {
  getAllModules,
  getModuleByClass,
  getModuleByprofId,
  getModuleById
} = require("../controllers/moduleControllers");


moduleRouter.route("/").get(getAllModules);

moduleRouter.route("/:id").get(getModuleByprofId).get(getModuleByClass).get(getModuleById);

module.exports = moduleRouter;