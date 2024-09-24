const express = require('express')
const http = require('http')
const app = express()
const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/starter').then(() => console.log('MongoDB Connected!'))
.catch((err)=>console.log(`Found error ${err}`));

const userSchema = new mongoose.Schema({
    firstName:{
        type:String,
        require:true
    },
    lastName:{
        type: String,
    },
    email:{
        type:String,
        required:true,
        unique:true
    }
});

const User = mongoose.model("user", userSchema);

app.use(express.urlencoded({extended:false}));

app.post('/api/users',async (req, res) =>{
    const body = req.body;
    await User.create({firstName:body.first_name,lastName:body.last_name, email:body.email});
    res.send("User created successfully!");
});

app.listen(8000,() => console.log('Server started!'));

