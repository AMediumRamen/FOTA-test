import flask
from flask import jsonify
from flask import request

application = flask.Flask(__name__)
application.config["DEBUG"] = True

@application.route('/',methods=['GET'])
def testConnection():
    return "FOTA test connection made successfully"


@application.route('/api/test',methods=['GET'])
def returnHelloWorld():
    return "Hello World"

application.run()