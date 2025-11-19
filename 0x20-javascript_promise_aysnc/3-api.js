async function fetchproducts() {
	const raw = await new Promise((resolve, reject) => {
		fetch('https://dummyjson.com/products')
		.then(resp => {
			if (resp.status != 200)
			{
				rejetct("failed");
			}else {
				resolve(resp);
			}
		})
	}
		return raw;
}
fetchproducts()
    .then(res => res.json())
    .then(products => {
	    for (let product of products)
	    {
		    console.log(prduct)
	    }
    })
    .catch(err => console.error(err)
