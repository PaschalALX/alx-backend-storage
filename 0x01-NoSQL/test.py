import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_db"]
school_collection = db["school"]

me = school_collection.insert_one({"name":"Paschal", "age": 30})
for x in me:
    print(x)

# def insert_school(mongo_collection, **kwargs):
#     mongo_collection.insert_one(kwargs)


# insert_school(school_collection, name="Paschal", age=30)