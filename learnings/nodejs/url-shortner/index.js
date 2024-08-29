const express = require('express');
const mongoose = require('mongoose');
const app = express()
port = 3000

const shortUrlSchema = new mongoose.Schema({
    url:{
        type:String,
        required:true,
        unique:true
    },
    short_url:{
        type:String,
        required:true,
        unique:true
    },
    timestamp:true
});

const ShortUrl = mongoose.model("ShortUrl",shortUrlSchema);

app.listen(port, ()=>{
    console.log(`App is running on ${port}`);
})