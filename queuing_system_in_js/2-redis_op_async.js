// task three - my little redis server
import redis from 'redis';
import { promisify } from 'util';
import { createClient } from 'redis';
const client = createClient();

// log connection failure message
client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

// log connection success message
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value){
  // set key schoolName to value
  // display a confirmation message using redis.print
  client.set(schoolName, value, redis.print)
};

const displaySchoolValue = async (schoolName) => {
  // bind promisify to client
  const promise = promisify(client.get).bind(client);
  const value = await promise(schoolName); // pass key to client
  console.log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
