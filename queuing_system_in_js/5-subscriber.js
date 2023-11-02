// task five - my little redis subscriber
import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

// log connection failure message
client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

// log connection success message
client.on('connect', () => console.log('Redis client connected to the server'));

// subscribe to the channel holberton school channel
// const listener = (message, channel)
(async () => {
  const subscriber = client.duplicate();
  await subscriber.connect();
  
  // When it receives message on the channel holberton school channel, 
  // it should log the message to the console
  await subscriber.subscribe('holberton school channel', (message) => {
    console.log(message); 
  })

  // When the message is KILL_SERVER, it should unsubscribe and quit
  if (message === KILL_SERVER) {
    subscriber.unsubscribe();
    subscriber.quit()
  }
})
