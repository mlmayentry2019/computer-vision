var express = require('express');
var app = express();
var rp = require('request-promise');
var bodyParser = require("body-parser");

const host = 'localhost';

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.set('view engine', 'pug');
app.set('views','./views');

app.get('/', async function(req, res) {
   try {
      //var response = await rp(`http://${host}:5000/`);
      //obj = JSON.parse(response);
      res.render('index');
      //return 
   } catch(err) {
      console.error(err)
   }
});

app.listen(3000);