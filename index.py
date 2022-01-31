from flask import Flask,request,session,render_template,jsonify
import jwt
from datetime import datetime,timedelta
from settings import SECRET_KEY
from views.market_api import market_apis

app=Flask(__name__)
app.register_blueprint(market_apis)
app.config['SECRET_KEY']=SECRET_KEY
app.config['PROPAGATE_EXCEPTIONS']=True

@app.route('/home')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "You are already Logged In"

@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username',None)
    password=request.form.get('password',None)
    
    #Registration part is not completed hence directly generating token for the user
    jwt_token=jwt.encode({'user':username,'exp':datetime.utcnow()+timedelta(minutes=30)},SECRET_KEY)
    response =jsonify({'x-api-token':jwt_token})
    response.set_cookie('x-api-token',jwt_token)    #Saving token inside cookie to protect from XSS attacks
    session["logged_in"]=True
    return response
