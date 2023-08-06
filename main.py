from pymongo import MongoClient

#Replace <url> with your mongodb atlas connection string
uri = "mongodb+srv://reader:reader123@cluster1.57jsnka.mongodb.net/"
client = MongoClient(uri)

#Replace <database-name> with the name of your database
db = client["Database1"]

#Replace <collection-name> with the name of your collection
collection = db["collec1"]



#check the connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to Mongodb")
except Exception as e:
    print(e)

document = {"name": "Danial","age":36}

#Insert the document into the collection
insert_result = collection.insert_one(document)

#print the ID of the inserted document
print("Inserted Document ID:", insert_result.inserted_id)

client.close()