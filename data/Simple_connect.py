import cluster as cluster
import pymongo
from pymongo import MongoClient
from data.mongo_setup import global_init

def pcinfo():
    try:
        client = MongoClient("mongodb+srv://AgentUsr:Logiologio1998@cluster0.7bqpr.mongodb.net/UserData?retryWrites=true&w=majority")
        db = client.get_database("test")
        col = db.get_collection("user")
        col.delete_many({})
        data = global_init()
        col.insert_one(data)
        print("success")
    except:
        print("error")

#if db.mycollection.find({'UserIDS': { "$in": newID}}).count() > 0