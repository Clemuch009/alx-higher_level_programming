use products_db

db.products.aggregate([
	{
		$match: {
			price: {$gte: 50},
			category: "Electronics"
		}
	},
	{
		$sort: {price: 1}
	},
	{
		$limit: 3}
]);
