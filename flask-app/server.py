from flask import Flask, render_template, request, redirect, url_for
import os
import json
import datetime
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath("__FILE__"))
DATA_DIR = os.path.join(BASE_DIR, "Data")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

storage = os.path.join(DATA_DIR, "posts.json")
if not os.path.exists(storage):
    os.mknod(storage)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home/')
def home():
    posts = None
    try:
        with open(storage, 'r') as file:
            posts = json.load(file)
    except:
        pass
    if posts:
        return render_template('home.html', posts=posts)
    else:
        return render_template('home.html')

@app.route('/create/' , methods=['GET', 'POST'])
def write_post():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        posts = []
        with open(storage, 'r') as file:
            try:
                posts = json.load(file)
            except: # first time when file is blank
                posts = []

        s = dict(request.form)
        today = datetime.datetime.now()
        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")
        s['timestamp'] = date_time
        posts.append(s)
        with open(storage, 'w') as file:
            json.dump(posts, file)
        return redirect(url_for('home'))