import flask
from flask import jsonify
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def testConnection():
    return "FOTA test connection made successfully"


@app.route('/api/test',methods=['GET'])
def returnHelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.run()