#!/usr/bin/env python3
# asyncio is required (use Python >= 3.4)

from autobahn.asyncio.websocket import (
    WebSocketServerProtocol, WebSocketServerFactory)

import asyncio
import json
from math import ceil
from base64 import b64encode
from itertools import count
from time import time
from random import normalvariate

def int_to_nicestr(value):
    return b64encode(value.to_bytes(ceil(value.bit_length() / 8), 'big'), b'_$')\
            .decode('ascii').replace('=', '')

def clamp(value, lbound, ubound):
    if ubound is not None and value > ubound:
        return ubound
    elif lbound is not None and value < lbound:
        return lbound
    else:
        return value

message_id = count(1)

def generate_message():
    return {'id': next(message_id), 'timestamp': time()}

class TestProtocol(WebSocketServerProtocol):

    connection_closed = False
    next_task = None

    def get_random_wait_interval(self):
        return clamp(normalvariate(4.0, 1.5), 0.5, None)

    def get_id(self):
        return int_to_nicestr(id(self))

    def send_json(self, obj):
        self.sendMessage(json.dumps(obj).encode('utf-8'), False)

    def schedule_next_message(self):
        timeout = self.get_random_wait_interval()
        self.next_task = asyncio.ensure_future(asyncio.sleep(timeout))
        self.next_task.add_done_callback(self.send_next_message)

    def send_next_message(self, future):
        if not (future.cancelled() or self.connection_closed):
            print('{0}: Sending message'.format(self.get_id()))
            self.send_json(generate_message())
            self.schedule_next_message()

    def onConnect(self, request):
        print("{0}: Connection requested".format(self.get_id()))

    def onOpen(self):
        print("{0}: Connection open".format(self.get_id()))
        self.schedule_next_message()

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("{0}: Binary message received: {1} bytes".format(self.get_id(), len(payload)))
        else:
            message = payload.decode('utf-8')
            print("{0}: Text message received: {1}".format(self.get_id(), message))

        self.send_json({'success': True})

    def onClose(self, wasClean, code, reason):
        print("{0}: Connection closed: {1}".format(self.get_id(), reason))
        self.connection_closed = True
        if self.next_task is not None:
            self.next_task.cancel()

def main():
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
