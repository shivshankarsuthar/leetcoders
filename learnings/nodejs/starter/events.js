let events = require('events');
let stream = new events.EventEmitter();

stream.on('used',(args) => {
    console.log('used event fired with args:'+args.data);
})

stream.emit('used',{'data':true});