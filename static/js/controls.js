
function Control(device) {

    const params = {
        device: device,
        action: 'relay/0?turn=toggle'
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
        console.log('GET response:');
        console.log(status); 
    });
 }

