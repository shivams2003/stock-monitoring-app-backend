from django.conf import settings
from pymongo import MongoClient

client = MongoClient(settings.MONGODB_URI)
db = client.get_database(settings.MONGO_DB_NAME)
