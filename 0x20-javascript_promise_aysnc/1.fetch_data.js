const userPromise = new Promise((resolve, reject) => {
	console.log("loading...");
	setTimeout(()=> {
		fetch('https://jsonplaceholder.typicode.com/users/1')
		.then(response => response.json())
		.then(data => {
			resolve(data);
		})
		.catch(err => reject(err));
	}, 5);
});
userPromise
    .then(user => {
	    console.log(user);
    })
    .catch(err => {
	    console.log(err)
    });
		
