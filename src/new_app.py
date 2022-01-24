from flask import Flask, jsonify, request,make_response
import flask_cors
from flask import request

cors = flask_cors.CORS()


# Initialize flask app for the example
app = Flask(__name__)
cors.init_app(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms="HS256")
            values = cursor.execute("SELECT id,email,password FROM users where email=%(email)s;",{"email":data['public_id']})
            user=cursor.fetchall()
        except:
            print("invalid")
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  f(user, *args, **kwargs)
  
    return decorated

@app.route('/login', methods=['POST','GET'])
def login():
    return "hehe"
@app.route('/register', methods=['POST','GET'])
def register():
    return "hehe"
@app.route("/handleform",methods=["POST","GET"])
@token_required
def protected(current_user):
    return "hehe"
if __name__ == '__main__':
    app.run(port=5000)
