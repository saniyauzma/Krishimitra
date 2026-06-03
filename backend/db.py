import os
from types import SimpleNamespace

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class InMemoryUsersCollection:
    """Minimal collection fallback so backend can run without Mongo."""

    def __init__(self):
        self._docs = []
        self._next_id = 1

    def create_index(self, *_args, **_kwargs):
        return "inmemory_email_index"

    def find_one(self, query):
        for doc in self._docs:
            if all(doc.get(k) == v for k, v in query.items()):
                return doc
        return None

    def insert_one(self, data):
        doc = dict(data)
        doc["_id"] = self._next_id
        self._next_id += 1
        self._docs.append(doc)
        return SimpleNamespace(inserted_id=doc["_id"])


MONGO_URL = os.getenv("MONGO_URL")
users_collection = None

try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=8000)
    client.admin.command("ping")
    db = client["krishi_mitra"]
    users_collection = db["users"]
    users_collection.create_index("email", unique=True)
    print("✅ MongoDB connected successfully!")
    print("✅ Email index created successfully!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    print("⚠️ Falling back to in-memory users store (data resets on restart).")
    users_collection = InMemoryUsersCollection()

