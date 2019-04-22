from app import app
from flask import render_template, flash, redirect
from app.forms.postForm import PostForm
import requests
from func_pack import create_rec_hash, get_current_time, get_api_info
from config import Config


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about-us', methods=['GET'])
def about_us():
    return render_template('about_us.html')


