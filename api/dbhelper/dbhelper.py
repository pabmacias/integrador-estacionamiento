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

def find_coordinates():
    data = list(DATABASE.places.find())

    coordinates = []
    for d in data:
        coordinates.append([d['x'], d['y'], d['spaceID']])

    return coordinates

def find_free_spaces():
    data = list(DATABASE.places.find({'occupied': {'$eq': False}}, {'_id': 0}))

    return data

def find_occupied_spaces():
    data = list(DATABASE.places.find({'occupied': {'$eq': True}}, {'_id': 0}))

    return data

def occupy_space(spaceID):
    DATABASE.places.update({'spaceID': spaceID},
                           {'$set': {'occupied': True}})
    return

def free_space(spaceID):
    DATABASE.places.update({'spaceID': spaceID},
                           {'$set': {'occupied': False}})
    return
