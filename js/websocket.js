const socket = new WebSocket('ws://localhost:8765/data');

function sendJSON(obj) {
    socket.send(JSON.stringify(obj));
}

const socketAccessor = {
    sendEvent: (name) => sendJSON({type: 'event', name: name}),

    onopen:    (callback) => socket.onopen = callback,
    onmessage: (callback) => socket.onmessage = callback,
    onclose:   (callback) => socket.onclose = callback,
    onerror:   (callback) => socket.onerror = callback
};

module.exports = socketAccessor;
