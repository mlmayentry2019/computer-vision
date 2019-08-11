var express = require('express');
var app = express();
var rp = require('request-promise');
const fileUpload = require('express-fileupload');

const host = 'localhost';

// default options
app.use(fileUpload());

app.set('view engine', 'ejs');
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

app.post('/upload', function(req, res) {
   console.log(req.files.image.name)
   return res.status(200).send({
      prediction: "pumkin", probability: 60
   });
});

app.listen(3000);