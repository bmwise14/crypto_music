const express = require('express')
const request = require('superagent');
const fs = require('fs');
const { exec } = require('child_process');
var action;

var SerialPort = require('serialport'); // serial library
var Readline = SerialPort.parsers.Readline; // read serial data as lines
var serial_port = '/dev/ttyUSB0'

const serial = new SerialPort(serial_port, {});

const app = express()
const port = 3000

var isOff = true;

app.get('/', (req, res) => res.send('We are mining '))

// setInterval( sendToServer , 1000)

// readFromSerial()

var config = {
  cwd: "/home/pi/cpuminer-multi"
}

function readFromSerial(){
  const parser = new Readline({
    delimiter: '\r\n'
  });

  // Read data that is available on the serial port and send it to the websocket
  serial.pipe(parser);

  parser.on('data', function(data) {
	console.log('data', data);

    if (data == "turn_off" && !isOff){

      console.log("TURNING OFF", isOff)

      isOff = true;

      try {
        action.kill('SIGINT');
      } catch (error) {
        console.log("already off");
      }

    } else if (data == "turn_on" && isOff) {

      console.log("TURNING On", isOff)

      isOff = false;
	  action = exec(
        "./cpuminer --algo qubit \
              --url stratum+tcp://digihash.co:3012 \
              --user DJMczFzdq2NeBPhBxrFbMJxg98mgWeRWyo \
              --pass anything", config,
        (error, stdout, stderr) => {
          if (error){
            console.error(error);
          }
          console.log(stdout);
        });
    }

    if (!isOff){
      // console.log('Data:', data);
    }
  });
}

/*
  Send stuff to server
 */

var prevHash = ""

function sendToServer(){
  
  const URL = "http://610c3bae.ngrok.i"

  if (isOff){
    return
  }

  if (fs.existsSync('../hashes.txt') && fs.existsSync('../result.txt')) {

    var found_hashes = fs.readFileSync('../hashes.txt', 'utf8');
    var result_hashes = fs.readFileSync('../result.txt', 'utf8');

    console.log("--> hash", found_hashes);
    console.log("--> result", result_hashes);

    var hash = found_hashes.split(",")[1];

    if (hash != undefined) {
      console.log("Found");
      writeToSerial("found_hash")
    } else {
      console.log("hash");
      hash = result_hashes.split(",")[1]
      prevHash = hash;
    }

    if (hash == "" || hash == undefined || hash == prevHash){
      hash = "" +  Math.floor(Math.random() * (1936711552 - 1) + 1)
    }

    sendToMidi(URL, hash)

    writeToSerial(hash)
    
    console.log(hash);
  } else {
    console.log("Files not found");
  }

  sendToMidi(URL, hash)

}

function writeToSerial(num){
  serial.write(num, (err) => {
    if (err) {
      return console.log('Error on write: ', err.message);
    }
    console.log('message written', num);
  });
}

/**
 * 
 * TESTING
 */
setInterval(sendToMidi, 300);

function sendToMidi(url, hash){
  console.log("sending");
  
  url = url || "http://610c3bae.ngrok.io/postjson"
  hash = hash || "8173245892345"
  
  request
    .post(url)
    .send({ hash: hash }) // sends a JSON post body
    .set('accept', 'json')
    .end((err, res) => { // console.log(err, res);
      if (res != undefined){
        console.log("sent", err, res);
      }
    });
}

app.listen(port, () => console.log(`Example app listening on port ${port}!`))