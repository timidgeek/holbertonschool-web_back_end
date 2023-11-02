// task five - my little redis publisher
import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

// log connection failure message
client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

// log connection success message
client.on('connect', () => console.log('Redis client connected to the server'));

function publishMessage (message, time) {
  // after time millisecond, log message and publish to channel
  setTimeout(() => {
    console.log(`About to send ${message}`)
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);