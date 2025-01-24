import { createClient } from "redis";

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.message)
})