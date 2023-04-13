from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>We are programmers</h1>'

@app.route('/itdp', methods=['GET'])
def itdp():

    return render_template('itdp.html')

@app.route('/interns', methods=['GET'])
def interns():

    return render_template('interns.html')
