from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>We are programmers</h1>'
