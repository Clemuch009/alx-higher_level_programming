use products_db
db.products.find({price: {$gte:50}}, {name:1, price: 1, _id: 0})
