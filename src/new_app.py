from flask import Flask, jsonify, request,make_response
import flask_cors
from flask import request
from firebase_admin import auth
import firebase_admin

default_app = firebase_admin.initialize_app({
    apiKey: "AIzaSyDdDhcmZfmc-pRGMvO7O5IjqJxW4sqz1-s",
    authDomain: "careerpathmap.firebaseapp.com",
    projectId: "careerpathmap",
    storageBucket: "careerpathmap.appspot.com",
    messagingSenderId: "965135340240",
    appId: "1:965135340240:web:25c35ec695d3518b7c84d5",
    measurementId: "G-0D0HYDTRLE"
})
print(default_app.name)  # "[DEFAULT]"

cors = flask_cors.CORS()
app = Flask(__name__)
cors.init_app(app)

@app.route('/login', methods=['POST','GET'])
def login():
    data = request.get_json(silent=True)
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    return uid

@app.route('/register', methods=['POST','GET'])
def register():
    return "hehe"
if __name__ == '__main__':
    app.run(port=5000)
