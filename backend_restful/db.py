import pymongo

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

client = pymongo.MongoClient(mongodb_url)
db = client.test
users = db.users