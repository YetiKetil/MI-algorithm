from flask import Flask
from webapp.config import Config

app = Flask(__name__, static_url_path="", static_folder="static")
#app = Flask(__name__)
app.config.from_object(Config)

from webapp.app import routes, models
