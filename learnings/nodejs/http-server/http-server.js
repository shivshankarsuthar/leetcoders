const http = require('http');
const fs = require('fs');
const url = require('url')
const server = http.createServer((req,res)=>{
    //res.end(url.parse(req.url).query);
    console.log(url.parse(req.url,true).query['a']);
});

server.listen(8000)