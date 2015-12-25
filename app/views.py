from app import app
import config

from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from flask import send_file
from flask import make_response
from flask import send_from_directory

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/getLine', methods=['GET','POST'])
def getLine():
    return jsonify({'points': [0,0,0,0.2,0.2,0,0.5,0.3,0]})
