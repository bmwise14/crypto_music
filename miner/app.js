const express = require('express')
const request = require('superagent');
const fs = require('fs');

var SerialPort = require('serialport'); // serial library

const app = express()
const port = 3000

var Readline = SerialPort.parsers.Readline; // read serial data as lines

var serial_port = '/dev/ttyUSB0'

const serial = new SerialPort(serial_port, {baudRate: 9600});


app.get('/', (req, res) => res.send('We are mining '))

// setInterval(()=>{ sendToServer }, 1000)

setInterval(()=>{ writeToSerial }, 1000)

readFromSerial()

function writeToSerial(){
  
  serial.write('main screen turn on\n', function(err) {
    if (err) {
      return console.log('Error on write: ', err.message);
    }
    console.log('message written');
  });
}

function readFromSerial(){
  
  const parser = new Readline({
    delimiter: '\r\n'
  });
  
  // Read data that is available on the serial port and send it to the websocket
  serial.pipe(parser);
  parser.on('data', function(data) {
    console.log('Data:', data);
  });
}

/*
  Send stuff to server
 */
function sendToServer(){
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
}

app.listen(port, () => console.log(`Example app listening on port ${port}!`))