from pymongo import ASCENDING, MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["taskdb"]

task_collection = db["tasks"]
task_collection.create_index([("priority", ASCENDING)])