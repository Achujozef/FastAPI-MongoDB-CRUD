from pymongo import MongoClient

client = MongoClient("mongodb+srv://achujozefsl0709:KWQu2T2vSQZbPkDk@cluster0.pzwhnjm.mongodb.net/?retryWrites=true&w=majority")


db=client.todo_db

collection_name = db["todo_collection"]