from flask import Flask
from apispec_webframeworks.flask import FlaskPlugin
from market_tracker.settings import SECRET_KEY
from market_tracker.views.market_api import market_apis as market_api_blueprint
from .index import main as main_blueprint

from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app=Flask(__name__)
    cors = CORS(app)

    # SWAGGER CONFIG
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,API_URL,
        config={
            'app_name': "Python-Flask-REST"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    
    app.register_blueprint(main_blueprint,url_prefix='/api/v1')
    app.register_blueprint(market_api_blueprint,url_prefix='/api/v1')
    
    app.config['SECRET_KEY']=SECRET_KEY
    app.config['CORS_HEADERS'] = 'Content-Type'
    return app

    
    

