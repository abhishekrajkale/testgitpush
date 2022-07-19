import pymongo
client = pymongo.MongoClient("mongodb+srv://abhishekkale:abhi#8411@abhirajk0.gakaogi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "abhishek",
    "email" : "abhishek@ineuron.ai",
    "surname": "kale"

}
db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)