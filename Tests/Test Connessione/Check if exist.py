from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://AgentUsr:Logiologio1998@cluster0.7bqpr.mongodb.net/UserData?retryWrites=true&w=majority")
db = client.get_database("AgentData")
col = db.get_collection("AgentDataCollected")

print(col.find_one({"_id": ObjectId("628a2a8ec37226af79d3f028")}))