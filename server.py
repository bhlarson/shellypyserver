import os, sys
import json , yaml
import argparse

from flask import Flask, render_template, jsonify, request
import requests
from requests.auth import HTTPBasicAuth

global args
devices = {}

# Parse startup arguments 
def parse_arguments():
    parser = argparse.ArgumentParser(description="Shelly Python Server")

    parser.add_argument('-d', action='store_true',help='Wait for debuggee attach')   
    parser.add_argument('-debug', type=bool, default=False, help='Wait for debuggee attach')
    parser.add_argument('-debug_port', type=int, default=3000, help='Debug port')
    parser.add_argument('-debug_address', type=str, default='0.0.0.0', help='Debug port')
    parser.add_argument('--verbose', '-v', action='store_true',help='Extended output')

    parser.add_argument('-creds', type=str, default='creds.yaml', help='Credentials file')
    parser.add_argument('-env', type=str, default='config/config.sh', help='Output environment file')
    parser.add_argument("--cert-file", default="server/certificate.crt", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", default="server/privateKey.key", help="SSL key file (for HTTPS)")
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=5000, help="Port for HTTP server (default: 8888)")
 
    args = parser.parse_args()

    if args.d:
        args.debug = args.d


    return args

# Create the Flask server
app = Flask(__name__)

# Utility function to read YAML text file into a python dictionary
def ReadDictYaml(filepath):
    yamldict = {}
    try:
        with open(filepath) as yaml_file:
            yamldict = yaml.safe_load(yaml_file)
        if not yamldict:
            print('Failed to load {}'.format(filepath))
    except ValueError:
        print('Failed to load {} error {}'.format(filepath, ValueError))
    return yamldict

# Utility function to convert device list into a device dictionary
def DeviceDict(creds_path):
    creds = ReadDictYaml(creds_path)
    devices = {}
    for device in creds['shelly']:
        devices[device['name']] = device
    return devices

# HTMl rout handling functions
@app.route("/")
def index(name=None):
    return render_template('index.html', name=name) # Serving static intex.html file on /

@app.route('/command', methods=["GET", "PUT"])
def command():
    global devices
    result = {}
    request_data = request.json

    if 'device' in request_data:
        device = devices[request_data['device']]

        if request.method == 'PUT':
            if 'action' in request_data:
                cmd = '{}{}'.format(device['url'],request_data['action'])
            else:
                cmd = '{}relay/0?turn=toggle'.format(device['url'])
                
            auth = HTTPBasicAuth(device['username'], device['password'])
            response = requests.get(cmd, auth = auth)
            result = json.loads(response.text)

        if request.method == 'GET':
            cmd = '{}relay/0'.format(device['url'])
                
            auth = HTTPBasicAuth(device['username'], device['password'])
            response = requests.get(cmd, auth = auth)
            result = json.loads(response.text)

    print('/command response {} return {}'.format(response.reason, result))

    return jsonify(result)

@app.route('/devices', methods=["GET"])
def devices():
    global devices
    result = []

    if request.method == 'GET':
        for device in devices:
            result.append({'name':devices[device]['name'], 
                           'device':devices[device]['device'], 
                           'group':devices[device]['group']})

    return jsonify(result)

def main(args):
    global devices
    devices =  DeviceDict(args.creds) 
    print("enter main")
    app.run (host=args.host, port=args.port, debug=False)

    return 0

if __name__ == '__main__':
    global args
    args = parse_arguments()

    if args.debug:
        print("Wait for debugger attach on {}:{}".format(args.debug_address, args.debug_port))
        import debugpy
        debugpy.listen(address=(args.debug_address, args.debug_port))
        # Pause the program until a remote debugger is attached

        debugpy.wait_for_client()
        print("Debugger attached")

    result = main(args)
    print("exit {}".format(result))    
    sys.exit(result)