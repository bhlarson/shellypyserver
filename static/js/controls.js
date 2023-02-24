function Devices() {

    const options = {
        method: 'GET' 
    };

    fetch('/devices', options)
    .then(function (response) {
        return response.json();
    }).then(function (status) {
        console.log('GET response:');
        console.log(status); 
    });
 }

// actions: 
// http://user:pass@[deviceIP]/relay/[channel]?[command]&[command]
// turn=on  - switch output ON
// turn=off - switch output OFF
// turn=toggle - reverese state 
// On and off can be combined with timer: 
// timer=X - where X is in seconds. Switch output will be turned On or OFF for X seconds and will be switched back to previews state after that. 
// Examples:
// relay/0?turn=on 
// relay/0?turn=on&timer=10 
// relay/0?turn=toggle 
function Control(device='christmas', action='relay/0?turn=toggle') {

    const params = {
        device: device,
        action: action
    };
    const options = {
        method: 'PUT',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify( params )  
    };

    fetch('/command', options)
    .then(function (response) {
        return response.json();
    }).then(function (status) {
        console.log('PUT response:');
        console.log(status); 
    });
 }

function State(device='christmas') {

    const params = {
        device: device
    };
    const options = {
        method: 'GET',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify( params )  
    };

    fetch('/command', options)
    .then(function (response) {
        return response.json();
    }).then(function (status) {
        console.log('GET response:');
        console.log(status); 
    });
 }

