use Users_db
db.users.deleteOne({name: "clement"})
db.users.deleteMany({$or: [{name:"Victor"}, {name:"Mark"}]})
