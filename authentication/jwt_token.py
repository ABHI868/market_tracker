from functools import wraps
from flask import request,jsonify,Response
from market_tracker.settings import SECRET_KEY
import jwt,json,os


def check_for_token(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        token = request.headers.get('x-api-token') if request.cookies.get('x-api-token') is None \
                else request.cookies.get('x-api-token')
        if not token:
            data={"message":"Token is Missing",'success':'False'}
            return Response(json.dumps(data), status=400)
        try:
            c=jwt.decode(token,SECRET_KEY,'HS256')

        except:
            data ={'message':"Invalid Token",'success':'False'}
            return Response(json.dumps(data),status=401)
            
        return f(*args, **kwargs)
    return wrapped