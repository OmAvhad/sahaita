const WebSocket = require('websocket').w3cwebsocket;
const readline = require('readline');

const socket = new WebSocket('wss://smart-watch-socket.onrender.com');

// Connection opened
socket.addEventListener('open', (event) => {
  console.log('Connected to WebSocket');
  // Send a message to the server
  socket.send('Hello, server! This is the client.');
  // Set up readline interface to read input from the terminal
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  // Continuously prompt the user for input and send it as a message to the server
  rl.on('line', (input) => {
    // Send the message to the server
    socket.send(input);
  });
});

// Listen for messages from the server
socket.addEventListener('message', (event) => {
  console.log('Received message from server:', event.data);
});

// Connection closed
socket.addEventListener('close', (event) => {
  console.log('WebSocket connection closed:', event);
});

// Error handling
socket.addEventListener('error', (event) => {
  console.error('WebSocket error:', event);
});
