# from flask import Flask
# from market_tracker.settings import SECRET_KEY
# from market_tracker.views.market_api import market_apis as market_api_blueprint

# def create_app():
#     app=Flask(__name__)
    
#     from .index import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#     app.register_blueprint(market_api_blueprint)
#     app.config['SECRET_KEY']=SECRET_KEY
#     return app