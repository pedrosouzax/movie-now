from  flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_movie():
    return render_template('index.html')