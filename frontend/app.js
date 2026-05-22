const socket = new WebSocket("ws://localhost:8001/ws");

socket.onmessage = (event) => {
    console.log(event.data);
};

function startVoice() {
    socket.send("Book appointment tomorrow");
}
