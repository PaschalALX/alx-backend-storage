import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["my_db"]
school_collection = db["school"]
# school_collection.update_one()
[print(doc) for doc in school_collection.find({"topics": "Python is great"})]
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