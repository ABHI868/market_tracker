from flask import Flask,request,session,render_template,jsonify,Blueprint,make_response
import jwt
from datetime import datetime,timedelta
from .settings import SECRET_KEY
from flask_restful import Resource,Api

main = Blueprint('index',__name__)
api=Api(main)

class Home(Resource):
    def get(self):
        ''' This function will render Default page '''
        if not session.get('logged_in'):
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('login.html'),headers)
        else:
            return "You are already Logged In"


class Login(Resource):
    def post(self):
        ''' This function will allow user to login and generate a JWT token for \
        authentication in further api calls'''
        username=request.form.get('username','Abhishek')
        password=request.form.get('password',None)
        jwt_token=jwt.encode({'user':username,'exp':datetime.utcnow()+timedelta(minutes=30)},SECRET_KEY)
        response =jsonify({'x-api-token':jwt_token})
        response.set_cookie('x-api-token',jwt_token)    #Saving token inside cookie to protect from XSS attacks
        session["logged_in"]=True
        return response

api.add_resource(Login,'/login')
api.add_resource(Home, '/home')

