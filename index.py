from flask import Flask,request,session,render_template,jsonify,Blueprint
import jwt
from datetime import datetime,timedelta
from .settings import SECRET_KEY

main = Blueprint('index',__name__)

@main.route('/home')
def index():
    ''' This function will render Default page '''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You are already Logged In"

@main.route('/login',methods=['POST'])
def login():
    ''' This function will allow user to login and generate a JWT token for \
        authentication in further api calls'''
    username=request.form.get('username','Abhishek')
    password=request.form.get('password',None)

    #Registration part is not completed hence directly generating token for the user
    
    jwt_token=jwt.encode({'user':username,'exp':datetime.utcnow()+timedelta(minutes=30)},SECRET_KEY)
    response =jsonify({'x-api-token':jwt_token})
    response.set_cookie('x-api-token',jwt_token)    #Saving token inside cookie to protect from XSS attacks
    session["logged_in"]=True
    return response
