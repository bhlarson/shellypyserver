# # Installation: pip install aioshelly
# import asyncio
# from aioshelly.rpc_device import RpcDevice

# async def main():
#     shelly_ip = "192.168.1.85"  # Replace with your Shelly device's IP address
#     device = RpcDevice(shelly_ip)

#     try:
#         await device.update_status()
#         print("Device Status:", device.status)

#         # Example: Get device information
#         device_info = await device.call("Shelly.GetDeviceInfo")
#         print("Device Info:", device_info)

#         # Example: Turn on a switch
#         # switch_on_result = await device.call("Switch.Set", {"id": 0, "on": True})
#         # print("Switch On Result:", switch_on_result)

#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         await device.close()

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from pprint import pprint

import aiohttp

from aioshelly.common import ConnectionOptions
from aioshelly.exceptions import DeviceConnectionError, InvalidAuthError
from aioshelly.rpc_device import RpcDevice, WsServer


async def test_rpc_device():
    """Test Gen2/Gen3 RPC (WebSocket) based device."""
    options = ConnectionOptions("192.168.1.85", "username", "password")
    ws_context = WsServer()
    await ws_context.initialize(8123)

    async with aiohttp.ClientSession() as aiohttp_session:
        try:
            device = await RpcDevice.create(aiohttp_session, ws_context, options)
        except InvalidAuthError as err:
            print(f"Invalid or missing authorization, error: {repr(err)}")
            return
        except DeviceConnectionError as err:
            print(f"Error connecting to {options.ip_address}, error: {repr(err)}")
            return

        pprint(device.status)

        device_info = await device.call_rpc("Shelly.GetDeviceInfo")
        print("Device Info:", device_info)


if __name__ == "__main__":
    asyncio.run(test_rpc_device())