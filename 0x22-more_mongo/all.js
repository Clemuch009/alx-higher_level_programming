use products_db
db.products.find({price: {$lt: 50}})
