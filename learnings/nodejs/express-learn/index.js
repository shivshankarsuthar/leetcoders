const express = require('express')
const app = express()
const port = 3000

app.use('/media',express.static('static'))
app.use('h',)

app.route('/')
.get((req,res) => {
    res.send(req.headers)
})
.post((req,res)=>{
    res.send(req.body)
})

app.listen(port, ()=>{
    console.log(`App is listening on port ${port}`);
})

