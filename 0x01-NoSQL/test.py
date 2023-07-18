import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_db"]
school_collection = db["school"]

schools = [doc for doc in school_collection.find()]

print(schools)