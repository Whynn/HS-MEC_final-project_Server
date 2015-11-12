var express = require('express');
var app = express();
var fs = require('fs');
var sensorLib = require('./node_modules/node-dht-sensor/build/Release/node-dht-sensor');

app.listen(process.env.PORT, process.env.IP, 0, function () {
  console.log('Example app listening!');
});

app.get('/', function (req, res) {
  fs.readFile('index.html', function(err, data){
    if(err) {
        console.log(err);   
    } else {
        res.writeHead(200, {'Content-Type':'text/html'});
        res.end(data);
    }
  });
  //res.send('Hello World!');
});

var sensor = {
    initialize: function() {
        return sensorLib.initialize(22, 4);
    },
    read: function() {
        var readout = sensorLib.read();
        var temp = readout.temperature.toFixed(2);
        var humid = readout.humidity.toFixed(2);
        
        console.log('Temperature: ' + temp + 'C, ' + 'Humidity: ' + humid + '%');
        setTimeout(function () {
            sensor.read();
        }, 2000);
    }
};

if (sensor.initialize()){
    sensor.read();
} else {
    console.warn('Failed to initialize sensor');
}