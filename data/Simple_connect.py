import keyword

from pymongo import MongoClient
import subprocess, sys
import json
import io
# Importa tutta la roba
def powershell():
    dataps = subprocess.Popen(["powershell.exe",
              "C:\\Users\\Kitsu\\PycharmProjects\\Agent\\data\\Get-ComputerInfo.ps1"],
              stdout=sys.stdout)
    return dataps
#questo fà partire lo script powershell che crea un file json nella cartella di esecuzione dello script.

 # MERDA #def openJson():
    #datajson = json.load(io.open('C:\\Users\\Kitsu\\PycharmProjects\\Agent\\data\\psjsonUTF8.json', 'r', encoding='utf-8-sig'))
    #print(datajson)
    #return datajson

#Questo prende le info e le carica sul DB
def pcinfo():
    print("error prima try")
    try:
        client = MongoClient("mongodb+srv://AgentUsr:Logiologio1998@cluster0.7bqpr.mongodb.net/UserData?retryWrites=true&w=majority")
        db = client.get_database("AgentData")
        col = db.get_collection("AgentDataCollected")
        print("error prima caricamento json")
        datajson = json.load(io.open('C:\\Users\\Kitsu\\PycharmProjects\\Agent\\data\\psjsonUTF8.json', 'r', encoding='utf-8-sig'))
        print("error prima caricamento insertid")
        col.insert_one(datajson).inserted_id()
        print("error dopo caricamento insertid")
        print("success")
    except:
        print("error")

#if db.mycollection.find({'UserIDS': { "$in": newID}}).count() > 0

