from functools import wraps
from flask import request,jsonify
from market_tracker.settings import SECRET_KEY
import jwt

def check_for_token(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        token=request.headers.get('x-api-token') if request.cookies.get('x-api-token') is None \
                else request.cookies.get('x-api-token')
        if not token:
            return jsonify({"message":"Token is Missing"},401)
        try:
            jwt.decode(token,SECRET_KEY,'HS256')
        except:
            return jsonify({'message':"Invalid Token" }, 401)
        return f(*args, **kwargs)
    return wrapped