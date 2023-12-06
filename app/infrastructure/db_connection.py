from pymongo import MongoClient
import os

print("Hola")

user_name = "DirtyDann"
password = "Hola123"

mongo_url: str = f"mongodb+srv://{user_name}:{password}@databasecluster.1ry5d.mongodb.net/"
#mongo_atlas_url: str = os.environ['MONGO_URL']

#client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
client = MongoClient(mongo_url)

data_base = client.inventory_app
product_collection = data_base.products