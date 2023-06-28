const axios = require('axios');

async function getCustomers(req, res) {
  try {
    const response = await axios.get('http://127.0.0.1:8000/logistics/api/customers/');
    const customers = response.data;
    res.json(customers);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
}

async function getPackages(req, res) {
  try {
    const response = await axios.get('http://127.0.0.1:8000/logistics/api/packages/');
    const packages = response.data;
    res.json(packages);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
}

async function getCarriers(req, res) {
  try {
    const response = await axios.get('http://127.0.0.1:8000/logistics/api/carriers/');
    const carriers = response.data;
    res.json(carriers);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
}

async function updatePackage(req, res) {
  const { id } = req.params;
  const { deliveryStatus } = req.body;

  try {
    const response = await axios.put(`http://127.0.0.1:8000/logistics/api/packages/${id}/`, { deliveryStatus });
    const updatedPackage = response.data;
    res.json(updatedPackage);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
}

module.exports = {
  getCustomers,
  getPackages,
  getCarriers,
  updatePackage,
};
