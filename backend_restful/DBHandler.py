import pymongo

class DBHandler:
    @staticmethod
    def get_database_client():
        mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"
        return pymongo.MongoClient(mongodb_url)
