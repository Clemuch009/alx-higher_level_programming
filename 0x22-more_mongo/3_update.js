use products_db

db.products.updateMany({price: {$lt: 50}}, {$set: {release: ISODate()}})
