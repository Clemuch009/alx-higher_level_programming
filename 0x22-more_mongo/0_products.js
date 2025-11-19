use products_db

db.createCollection("products", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			required:["name", "category", "price", "stock", "description"],
			properties: {
				name: {
					bsonType: "string",
					description: "Product name must be a string"
				},
				 category: {
					 bsonType: "string",
					 description: "Category must be a string"
				 },
				price: {
					bsonType: "double",
					description: "Price must be a number"
				},
				stock: {
					bsonType: "int",
					description: "Stock quantity must be an integer"
				},
				description: {
					bsonType: "string",
					description: "Description must be a string"
				},
			}
		}
	}
})
