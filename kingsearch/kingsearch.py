# all the imports
import os
import sqlite3
from flask import Flask, jsonify, json, request

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

app.config.from_envvar('KINGSEARCH_SETTINGS', silent=True)
