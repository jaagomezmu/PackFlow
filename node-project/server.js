const express = require('express');
const app = express();
const routes = require('./routes');

const port = 3000;

app.use('/', routes);

app.listen(port, () => {
  console.log(`Servidor escuchando en el puerto ${port}`);
});
