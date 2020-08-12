# import asyncio
# import websockets
#
#
# async def message():
#     async with websockets.connect("ws://localhost:1234") as socket:
#         while(True):
#             msg = input("What do you want to send: ")
#             await socket.send(msg)
#             print(await socket.recv())
#
# asyncio.get_event_loop().run_until_complete(message())
# asyncio.get_event_loop().run_forever()


#!/usr/bin/env python3.6

import asyncio
import websockets

async def msg():
    async with websockets.connect('ws://localhost:8765') as websocket:

        await websocket.send('test message')
        msg = await websocket.recv()
        print(msg)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(msg())
    asyncio.get_event_loop().run_forever()