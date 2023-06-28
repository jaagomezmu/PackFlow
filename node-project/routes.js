const express = require('express');
const router = express.Router();
const controller = require('./controllers/controller');

router.get('/customers', controller.getCustomers);

router.get('/packages', controller.getPackages);

router.get('/carriers', controller.getCarriers);

router.put('/packages/:id', controller.updatePackage);

module.exports = router;
