// task one - babel and es6
// import redis, connect to server
import { createClient } from 'redis';
const client = createClient();

// log connection failure message
client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

// log connection success message
client.on('connect', () => console.log('Redis client connected to the server'));
