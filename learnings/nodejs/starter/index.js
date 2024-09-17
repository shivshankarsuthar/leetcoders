const http = require('http');
const currTime = require('./helpers');
const fs = require('fs');
const url = require('url');


const server = http.createServer((req,res)=>{
    fs.readFile('log.txt',(err,data) => {
        res.end(data);
    });
    fs.writeFile('log2.txt','This is second log file',(err)=>{
        if(err){
            throw err;
        }
    })
    fs.appendFile('log2.txt',"\nAppending something",(err)=>{
        if(err){
            throw err;
        }
    });
    fs.renameSync('log2.txt','logNew.txt',(err) => {
        if(err){
            throw err;
        }
    })
    // fs.unlink('logNew.txt',(err) => {
    //     if(err){
    //         throw err;
    //     }
    // })
    const q = url.parse(req.url,true);
    console.log(q.query.sample);
    // res.writeHead(200,{'Content-Type':'text/html'});
    // res.end(currTime.currTime());
});
server.listen(8000);

