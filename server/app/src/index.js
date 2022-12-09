const express = require('express');
const path = require('path');

const app = express();

app.disable('x-powered-by');

app.set('view engine', 'ejs');
app.set('views', path.resolve(__dirname, 'view'));

app.get('/', function (req, res) {
    res.send('Hello World!');
});

app.listen(80);
