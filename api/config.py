"""
This file contains all of the configuration values for the application.
"""
import getpass

username = getpass.getuser()

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'
DB_URI = 'mongodb://user:password2@ds147659.mlab.com:47659/parking_spaces'
