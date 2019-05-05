from flask import jsonify
from pymongo import MongoClient
from config import DB_URI
import requests
import json
import numpy as np
from dateutil.parser import parse

URI = DB_URI
CLIENT = MongoClient(URI,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None)
DATABASE = CLIENT.get_database()

def find_coordinates(parking):
    data = list(DATABASE.places.find({'parking': {'$eq': parking}}, {'_id': 0}))

    coordinates = []
    for d in data:
        coordinates.append([d['x'], d['y'], d['spaceID']])

    return coordinates

def find_free_spaces(parking):
    # data = list(DATABASE.places.find({'occupied': {'$eq': False}}, {'_id': 0}))
    data = list(DATABASE.places.find({"$and": [
        {"occupied": False},
        {"parking": parking}
    ]}, {'_id': 0}))

    return data

def find_occupied_spaces(parking):
    # data = list(DATABASE.places.find({'occupied': {'$eq': True}}, {'_id': 0}))
    data = list(DATABASE.places.find({"$and": [
        {"occupied": True},
        {"parking": parking}
    ]}, {'_id': 0}))

    return data

def occupy_space(spaceID, parking):
    DATABASE.places.update({"$and": [
                            {'spaceID': spaceID},
                            {"parking": parking}
                           ]}, {'$set': {'occupied': True}})
    return

def free_space(spaceID, parking):
    DATABASE.places.update({"$and": [
                            {'spaceID': spaceID},
                            {"parking": parking}
                           ]}, {'$set': {'occupied': False}})
    return
