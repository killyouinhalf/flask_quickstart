# This is the main app
from flask import Flask

# Create an instance of the Flask object
app = Flask(__name__)

# import the URL routes, after app
# is created
import bottoms_up.views
