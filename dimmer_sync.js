// From https://github.com/ShellyUSA/Scripts/blob/main/plus-wall-dimmer-sync-actions/plus-wall-dimmer-sync-actions.js

console.log('Start dimmer sync')


let CONFIG = {
  server_url: "http://192.168.0.155:5000",  // Change these to reflect your dimmer group
  wifi_ip: "", // You do not need to fill in this line, the script will fill it in
};

// get local IP
Shelly.call("WiFi.GetStatus", null, function (status) {
  if (status.status === "got ip") {
    CONFIG.wifi_ip = status.sta_ip;
    CONFIG.server_devices = CONFIG.server_url + '/devices'
  }
  console.log("Device IP address: ",status.sta_ip)
  console.log("server_devices: ",CONFIG.server_devices)
});

/*
let CONFIG = {
  Group: ["192.168.0.132"],  // Change these to reflect your dimmer group
  wifi_ip: "", // You do not need to fill in this line, the script will fill it in
};

//  You should not need to modify anything past here

// get local IP
Shelly.call("WiFi.GetStatus", null, function (status) {
  print("Saving Wifi IP: ",status.sta_ip)
  if (status.status === "got ip
*/

// {"component":"light:3","name":"light","id":3,"now":1725254619.40591621398,"info":{"component":"light:3","id":3
//     22:23:39,"event":"toggle","state":true,"ts":1725254619.41000008583}

Shelly.addStatusHandler(
  function (event, userData) {
    // print("addStatusHandler :",JSON.stringify(event));

    // if 'delta' in request_data and 'brightness' in request_data['delta']:
    if ("delta" in event && "brightness" in event.delta){ 
        call_params = {'url': CONFIG.server_devices, body: event};

        Shelly.call('HTTP.POST', call_params, function(result) {
            // print(JSON.stringify(result));        
        });
    }
  }
);

//  Someone pressed the local light switch

Shelly.addEventHandler(
  function (event, userData) {
    // print("addEventHandler :",JSON.stringify(event));
    if ("delta" in event && "brightness" in event.delta){ 
        call_params = {'url': CONFIG.server_devices, body: event};

        Shelly.call('HTTP.POST', call_params, function(result) {
            // print(JSON.stringify(result));
        });
    }

  }
);