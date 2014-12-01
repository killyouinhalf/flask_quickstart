# This is IMO the heart of the app
# Import the app
from bottoms_up import app
from flask import render_template

# Create URL routing
@app.route('/')
def index():
    return render_template('index.html')
