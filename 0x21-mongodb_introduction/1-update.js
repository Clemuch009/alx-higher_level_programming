use Users_db

db.users.updateOne({name: "clement"}, {$set: {email: "clement@gmail.com", password:1234}})
