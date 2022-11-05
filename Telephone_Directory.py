import random

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
MyDb = client['TelephoneDirectory']

MyCollection = MyDb['UserDetails']

def inserData(startVal , endVal):
    row = {}
    for n in range(startVal,endVal):
        num = str(3 + n)
        street = num, "nth street"
        row = {'_id': n, 'Name':'abcd'+str(n), 'phNo': random.randrange(1, 10**10), 'Address': street }
        A= MyCollection.insert_one(row)

        print("Number of rows inserted:" ,A.inserted_id)
        return A.inserted_id

def readData():
    data = MyCollection.find();
    for r in data:
        print(r)

def updateData():
    updated = MyCollection.update_one({'Name' : 'abcd2'}, {'$set' : {'Name' : 'abcde2'}} )
    print("Number of rows updated: ", updated.modified_count)

def delete():
    id = inserData(20 , 21)
    deleted = MyCollection.delete_one({'_id': id})
    print("Number of rows deleted: ",deleted.deleted_count)

inp = int(input(("Enter\n1. Insert:\n2. Read:\n3.Update\n4.Delete")))
if(inp ==1):
    inserData()
elif(inp==2):
    readData()
elif(inp==3):
    updateData()
elif(inp ==4):
    delete()
else:
    print("Enter correct value")
