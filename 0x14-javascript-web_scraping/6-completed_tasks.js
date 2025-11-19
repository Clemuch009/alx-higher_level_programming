#!/usr/bin/node
const request = require('request');

request.get('https://jsonplaceholder.typicode.com/todos', (error, res, body) => {
	if (error) {
		console.log(error);
		return;
	}
	if (res.statusCode === 200) {
		const tasks = JSON.parse(body);
		const task_status = {};
		for (let task of tasks) {
			let usrid = task.userId;
			let total = 0;
			if (task.userId  === usrid && task.completed === true) {
				total += 1;
			}
			task_status[usrid] = total;
		}
		console.log(task_status);
	}
})
