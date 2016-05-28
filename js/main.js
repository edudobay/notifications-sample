const $ = require('jquery');
const toastr = require('toastr');
require('!style!css!toastr/package/toastr.css');

const socket = require('./websocket');

function setupSocket() {
    socket.onopen(() => {
        toastr.info('Connected to websocket!');
        socket.sendEvent('connect');
    });

    socket.onmessage((msg) => toastr.info('Got a message. It reads: ' + msg.data));
}

function main() {
    setupSocket();

    const p = $('<p>hello world</p>');
    const counter = { times: 0 };
    p.appendTo('#content')
        .on('click', () =>
            toastr.info(`This paragraph has been clicked ${++counter.times} times`));
}

$(main);
