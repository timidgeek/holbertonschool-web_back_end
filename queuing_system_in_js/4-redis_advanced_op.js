// task four - my little hash
import redis from 'redis';
import { createClient } from 'redis';
const client = createClient();

// log connection failure message
client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

// log connection success message
client.on('connect', () => console.log('Redis client connected to the server'));

// create hash
// use redis.print for each hset
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// display hash using hgetall
client.hgetall('HolbertonSchools', (err, response) => {
  if (err) {
    console.error('Error, hash is smashed', err);
  } else {
    console.log('Success, hash passed');
    console.log(response);
  }
});
