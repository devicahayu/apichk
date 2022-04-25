from os import environ
from pymongo import MongoClient


class conect:
    @classmethod
    def getDb(cls):
        db = MongoClient("mongodb+srv://lorus1:Heryh111@lorustest.ieiof.mongodb.net")
        return db.teamkimori


