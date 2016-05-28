const socket = new WebSocket('ws://localhost:8765/data');

function sendJSON(obj) {
    socket.send(JSON.stringify(obj));
}

const socketAccessor = {
    sendEvent: (name, params) => sendJSON({type: 'event', name, params}),

    onopen:    (callback) => socket.onopen = callback,
    onmessage: (callback) => socket.onmessage = callback,
    onclose:   (callback) => socket.onclose = callback,
    onerror:   (callback) => socket.onerror = callback
};

module.exports = socketAccessor;
