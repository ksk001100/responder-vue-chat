import responder

api = responder.API()

@api.route('/ws', websocket=True)
async def websocket(ws):
    await ws.accept()
    while True:
        msg = await ws.receive_text()
        await ws.send_text(msg)
    await ws.close()

if __name__ == '__main__':
    api.add_route('/', static=True)
    api.run()
