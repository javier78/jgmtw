import flask
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
#@app.route('/hello/<name>')
def hello():
    return render_template('index.html')


@app.route('/getWeather')
def weather():
    myDict = {'currentHigh': 40, 'currentLow': 20}
    return flask.jsonify(**myDict)

if __name__ == '__main__':
    app.run()

    # return render_template('index.html', name=name)
