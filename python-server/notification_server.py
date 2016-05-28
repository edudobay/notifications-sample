#!/usr/bin/env python3
# asyncio is required (use Python >= 3.4)

from autobahn.asyncio.websocket import (
    WebSocketServerProtocol, WebSocketServerFactory)

import json
from math import ceil
from base64 import b64encode

def int_to_nicestr(value):
    return b64encode(value.to_bytes(ceil(value.bit_length() / 8), 'big'), b'_$')\
            .decode('ascii').replace('=', '')

class TestProtocol(WebSocketServerProtocol):
    def get_id(self):
        return int_to_nicestr(id(self))
        
    def send_json(self, obj):
        self.sendMessage(json.dumps(obj).encode('utf-8'), False)

    def onConnect(self, request):
        print("{0}: Connection requested".format(self.get_id()))

    def onOpen(self):
        print("{0}: Connection open".format(self.get_id()))

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("{0}: Binary message received: {1} bytes".format(self.get_id(), len(payload)))
        else:
            message = payload.decode('utf-8')
            print("{0}: Text message received: {1}".format(self.get_id(), message))

        self.send_json({'success': True})

    def onClose(self, wasClean, code, reason):
        print("{0}: Connection closed: {1}".format(self.get_id(), reason))

def main():
    import asyncio

    PORT = 8765

    factory = WebSocketServerFactory('ws://localhost:%d' % PORT)
    factory.protocol = TestProtocol

    loop = asyncio.get_event_loop()
    start_server = loop.create_server(factory, '127.0.0.1', PORT)
    server = loop.run_until_complete(start_server)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()

if __name__ == '__main__':
    main()
