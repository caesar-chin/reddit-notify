import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DISCORDBOT_TOKEN = os.environ.get("DISCORDBOT_TOKEN")
DATABASE = os.environ.get("DATABASE")
HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
PORT = os.environ.get("PORT")