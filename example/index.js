var express = require('express');
var app = express();
var fs = require('fs');

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