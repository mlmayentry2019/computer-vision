var express = require('express');
var app = express();
var rp = require('request-promise');
const fileUpload = require('express-fileupload');

const host = process.env.API_HOST ? process.env.API_HOST : 'api';

// default options
app.use(fileUpload());

app.set('view engine', 'ejs');
app.set('views','./views');

app.get('/', async function(req, res) {
   return res.render('index');
});

app.post('/upload', async function(req, res) {
   var options = {
      method: 'POST',
      uri: `http://${host}:5000/image/predict`,
      formData: {
          image: {
              value: req.files.image.data,
              options: {
                  filename: 'image',
                  contentType: 'image/jpg'
              }
          }
      },
      headers: {
          /* 'content-type': 'multipart/form-data' */ // Is set automatically
      }
  };
  try {
     const result =  await rp(options);
     console.log(result);
     var jsonContent = JSON.parse(result);
     return res.status(200).send({
      prediction: jsonContent.object, probability: jsonContent.probability
   });
  } catch(err) {
     console.log(err);
     res.status(500).send()
  }
   
});

app.listen(3000);