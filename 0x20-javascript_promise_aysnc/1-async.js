async function fetchdata() {
	try {
		const data = await fetch('https://jsonplaceholder.typicode.com/todos');
		if (data.status != 200) {
			throw new Error("failed");
		}
		const result = await data.json();
		for (let task of result) {
			console.log(task);
		}
	}
	catch {
		(err) => {
			console.log(err);
		}
	}
}
fetchdata();
