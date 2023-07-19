import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_db"]
school_collection = db["school"]

[print(doc) for doc in school_collection.find()]
# school_collection.update_many({
#     "name": "Paschal"
# }, 
# {
#     "$set":{
#         "topics": [
#         "Is PHP dead?", "Python is great"
#     ]}
# }
# )