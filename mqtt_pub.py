import os, sys
import json , yaml
import argparse
import paho.mqtt.client as mqtt
from datetime import datetime

request_id = 0
devices = [
    {'topic': 'kitchen-north-scene', 'id': 0, 'output': False, 'brightness': 0},
    {'topic': 'kitchen-south-scene', 'id': 0, 'output': False, 'brightness': 0},
    {'topic': 'kitchen-lights', 'id': 0, 'output': False, 'brightness': 0},
    {'topic': 'sink-light', 'id': 0, 'output': False, 'brightness': 0},
    {'topic': 'cabinet-windows', 'id': 0, 'output': False, 'brightness': 0},
    {'topic': 'under-cabinet', 'id': 0, 'output': False, 'brightness': 0},
]

# Parse startup arguments 
def parse_arguments():
    parser = argparse.ArgumentParser(description="Shelly Python Server")

    parser.add_argument('-d', action='store_true',help='Wait for debuggee attach')   
    parser.add_argument('-debug', type=bool, default=False, help='Wait for debuggee attach')
    parser.add_argument('-debug_port', type=int, default=3000, help='Debug port')
    parser.add_argument('-debug_address', type=str, default='0.0.0.0', help='Debug port')
    parser.add_argument('--verbose', '-v', action='store_true',help='Extended output')

    parser.add_argument('-creds', type=str, default='./config/creds.yaml', help='Credentials file')
    parser.add_argument('-env', type=str, default='config/config.sh', help='Output environment file')
    parser.add_argument("--cert-file", default="server/certificate.crt", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", default="server/privateKey.key", help="SSL key file (for HTTPS)")
    parser.add_argument("--host", default="192.168.1.55", help="Host for HTTP server (default: 192.168.1.55)")
    parser.add_argument("--port", type=int, default=1883, help="Port for HTTP server (default: 1883)")
 
    args = parser.parse_args()

    if args.d:
        args.debug = args.d


    return args

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topics = []
    for device in devices:
          topic = f"{device['topic']}/events/rpc"
          topics.append((topic,0))    

    client.subscribe(topics)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
    except Exception as e:
        print(f"Couldn't parse raw data:{msg.payload} {e}")
    else:
        dt = datetime.now()

        if 'params' in payload:
            if payload['src'] == 'shellyplusrgbwpm-b0a732417bbc':

                msg_data = payload['params'][list(payload['params'].keys())[-1]]

                if 'output' in msg_data:

                    global request_id
                    request_id += 1

                    device  = devices[2]

                    topic = f"{device['topic']}/rpc"
                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Switch.Set', 'params':{'id': 0,'on':msg_data['output']}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1

                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Switch.Set', 'params':{'id': 1,'on':msg_data['output']}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1

                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Switch.Set', 'params':{'id': 2,'on':msg_data['output']}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1

                    device  = devices[3]
                    topic = f"{device['topic']}/rpc"
                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Light.Set', 'params':{'id': 0,'on':msg_data['output'], "brightness":100}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1

                    device  = devices[4]
                    topic = f"{device['topic']}/rpc"
                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Light.Set', 'params':{'id': 0,'on':msg_data['output'], "brightness":100}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1

                    device  = devices[5]
                    topic = f"{device['topic']}/rpc"
                    data = {'id':request_id, 'src':'mqtt_pub', 'method':'Light.Set', 'params':{'id': 0,'on':msg_data['output'], "brightness":100}}
                    client.publish(topic, json.dumps(data), 0)
                    request_id += 1


            # if 'output' in msg_data and 'brightness' in msg_data:
            #     res = next((sub for sub in devices if sub['topic'] == payload['src'] and msg_data['id'] == sub['id']), None)                
            #     if res is not None:

            #         if res['output'] != msg_data['output'] or res['brightness'] != msg_data['brightness']:
            #             res['output'] = msg_data['output']
            #             res['brightness'] = msg_data['brightness']
            #             for device in devices:
            #                 if device['topic'] != res['topic'] or device['id'] != res['id']:
            #                     if device['output'] != res['output'] or device['brightness'] != res['brightness']:
            #                         device['output'] = res['output']
            #                         device['brightness'] != res['brightness']
            #                         topic = f"{device['topic']}/rpc"
            #                         global request_id
            #                         if device['topic'] == 'kitchen-south-scene':
            #                             data = {'id':request_id, 'src':'mqtt_pub', 'method':'Light.Set', 'params':{'id': device['id'],'on':res['output'], 'brightness':res['brightness']}}
            #                         elif device['topic'] == 'kitchen-north-scene':
            #                             data = {'id':request_id, 'src':'mqtt_pub', 'method':'Light.Set', 'params':{'id': device['id'],'on':res['output'], 'brightness':res['brightness']}}
            #                         elif device['topic'] == 'kitchen-lights':
            #                             data = {'id':request_id, 'src':'mqtt_pub', 'method':'switch:'+device['id'], 'params':{'id': device['id'],'on':True}}
            #                         request_id += 1
            #                         print(f"{topic} {json.dumps(data)}")
            #                         client.publish(topic, json.dumps(data), 0)

            # print(f"{dt} topic: {msg.topic} {msg_data}")

def main(args):
    # client = paho.Client()

    # if client.connect(args.host, args.port, 60) != 0:
    #     print("Couldn't connect to the mqtt broker")
    #     sys.exit(1)

    # client.subscribe("test_topic")
    # client.publish("test_topic", "Hi, paho mqtt client works fine!", 0)

    # try:
    #     print("Press CTRL+C to exit...")
    #     client.loop_forever()
    # except Exception:
    #     print("Caught an Exception, something went wrong...")
    # finally:
    #     print("Disconnecting from the MQTT broker")
    #     client.disconnect()

    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.connect(args.host, args.port, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    mqttc.loop_forever()

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