import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["logs"]
collection = db["nginx"]

x_logs = collection.count_documents({})
print("{} logs".format(x_logs))

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    method_log = collection.count_documents({"method": method})
    print("\t method {}: {}".format(method, method_log))

status_check = collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(status_check))