#!/usr/bin/node

const request = require('request');

// API URL
const apiUrl = process.argv[2];

// Make a request to the API
request(apiUrl, (error, response, body) => {
  const tasks = {};
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const todos = JSON.parse(body);

    // Compute the number of completed tasks by user id
    const completedTasksByUserId = todos.reduce((result, todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        result[userId] = (result[userId] || 0) + 1;
      }
      return result;
    }, {});

    // Print users with completed tasks
    Object.entries(completedTasksByUserId).forEach(([userId, count]) => {
      tasks[`${userId}`] = count;
    });
  }
  console.log(tasks);
});
