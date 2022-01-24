from flask import Flask,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app , resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})

@app.route('/register', methods=['GET', 'POST'])
def register():
    return "hehe"
@app.route('/login',methods=["GET","POST"])
def login():
    return "hehe"

if __name__ == '__main__':
	app.run()
