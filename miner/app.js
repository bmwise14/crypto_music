const express = require('express')
const request = require('superagent');
const fs = require('fs');

const app = express()
const port = 3000

app.get('/', (req, res) => res.send('We are mining '))

setInterval(()=>{
  // var hash = fs.readFileSync('../hashes.txt', 'utf8');
  // var result = fs.readFileSync('../result.txt', 'utf8');

  console.log("--> hash", hash);
  // console.log("--> hash", result);

  var hash = ''
  if (hash == ''){
    hash = "12389345"
    hash = "" +  Math.floor(Math.random() * (12389345 - 1) + 1)
  }
  console.log(hash);
  

  request
    .post('http://f3c4c62a.ngrok.io/postjson')
    .send({ hash: hash }) // sends a JSON post body
    .set('accept', 'json')
    .end((err, res) => {
      // console.log(err, res);
    });
   
  // var success = result.split(',')[0]
  // var hashes_computed = result.split(',')[1]
  // console.log("--> hash", success, hashes_computed);

}, 1000)

app.listen(port, () => console.log(`Example app listening on port ${port}!`))