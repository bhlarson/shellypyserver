
function Control() {
    fetch('/command')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log('GET response:');
        console.log(text); 
    });
 }

