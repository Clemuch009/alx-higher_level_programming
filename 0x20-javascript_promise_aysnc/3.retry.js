async function retry() {
	const retry = new Promise((resolve, reject) => {
		const try_again = (url) => {
			if (status_code != 200){
				for (let i = 0; i < 4; i++)
				{
					setInterval(fun, 3000);
				}
			}
			const url = 'https://jsonplaceholder.typicode.com/users/1'
			const user = fetch(url)
			.then(res => {
				if (res.status != 200) {
					user = try_again(url);
				}
			})
			.then
