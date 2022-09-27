from json import load
import os 
import cocos
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    load_dotenv()

    return app 