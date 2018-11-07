const express = require('express')
const request = require('superagent');
const fs = require('fs');

const app = express()
const port = 3000

app.get('/', (req, res) => res.send('We are mining '))

setInterval(()=>{
  var content = fs.readFileSync('./hashes.txt', 'utf8');

  console.log("--> HERE", content);

  request
    .post('localhost')
    .send({ val: content }) // sends a JSON post body
    .set('accept', 'json')
    .end((err, res) => {
      console.log(err, res);
    });
}, 1000)

app.listen(port, () => console.log(`Example app listening on port ${port}!`))