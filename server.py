import os, sys
import requests
import json
import yaml
import argparse
from urllib import request
from flask import Flask, jsonify, request, render_template

global args

def parse_arguments():
    parser = argparse.ArgumentParser(description="Shelly Python Server")

    parser.add_argument('-d', action='store_true',help='Wait for debuggee attach')   
    parser.add_argument('-debug', type=bool, default=False, help='Wait for debuggee attach')
    parser.add_argument('-debug_port', type=int, default=3000, help='Debug port')
    parser.add_argument('-debug_address', type=str, default='0.0.0.0', help='Debug port')
    parser.add_argument('--verbose', '-v', action='store_true',help='Extended output')

    parser.add_argument('-args', type=str, default='serverconfig.yaml', help='Configuration')
    parser.add_argument('-env', type=str, default='config/config.sh', help='Output environment file')
    parser.add_argument("--cert-file", default="server/certificate.crt", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", default="server/privateKey.key", help="SSL key file (for HTTPS)")
    parser.add_argument("--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=5000, help="Port for HTTP server (default: 8888)")
    
 
    args = parser.parse_args()

    if args.d:
        args.debug = args.d


    return args

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/command', methods=["GET", "PUT"])
def command():
    data = {}
    if request.method == "PUT":
        print('/command put')
    elif request.method == "GET":
        print('/command get')
        'http://192.168.0.119/relay/0?turn=toggle'

    return jsonify(data)



def main(args):
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