const http = require('http')
const fs = require('fs')
const myserver = http.createServer((req,res)=>{
    fs.writeFileSync('log.txt',Date.now().toString()+req.statusCode)
    res.end("Hello from server")
})

myserver.listen(8000,()=>console.log("server started!"))