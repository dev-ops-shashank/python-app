# We are building 2 APIs using flask here. these APIs will be:
# '/api/v1/details'
# '/api/v1/healthz'


# Simple Flask application to serve two APIs

from flask import Flask,jsonify
from datetime import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    # return '<h1>Hello, World! from Shashank</h1>'
    return jsonify({
        "hostname": socket.gethostname(),
        'message': 'You are doing great, little human [UPDATED]!',
        "time" :  datetime.now().strftime("%d %B,%Y %H:%M:%S"),
        'deployed_on': 'Kubernetes'
        })

@app.route('/api/v1/healthz')
def healthz():
    # return '<h1>Hello, World! from Shashank</h1>'
    return jsonify({
        "status": "Up and running!"
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')