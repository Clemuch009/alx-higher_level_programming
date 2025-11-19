use Users_db
db.users.find({}, {name:1, email:1, _id: 0}, {age: {$gt: 18}})
