



from conftest import client

# import os
# import tempfile

# import pytest
from flask import *
# from flask import url_for


# # @pytest.fixture
# # def client():
# #     flaskr.app.config['TESTING'] = True

# #     with flaskr.app.test_client() as client:
# #         with flaskr.app.app_context():
# #             flaskr.init_db()
# #         yield client



# # from flask import Flask
# # from views.market_api import market_apis
# # app=Flask(__name__)
# # from index import configure_routes
# # app.register_blueprint(market_apis)

# def test_valid_marketsummary_header():
#     # client=app.test_client()
#     url='/market_summaries'
#     headers={'x-api-token':''}
#     response=client.get(url,headers=headers)
#     assert response.status_code == 200

# def test_invalid_marketsummary_header():
#     # client=app.test_client()
#     url='/market_summaries'
#     response=client.get(url)
#     assert response.status_code == 200
#     #getting 200 as status code

# def test_valid_market_details_header():
#     #Payload is Invalid
#     url='/getmarketsummary'
#     response =client.get(url)
#     assert response.success =='false'

# def test_invalidmethod_marketdetails():
#     url='/getmarketsummary'
#     response=client.get(url)
#     assert response.status_code ==405

# app=create_app()

def test_hello(client):
    # client =app.test_client()
    assert client.get(url_for('index')).status_code == 200
    # response =request.get(url='/')
    # assert response.status_code ==200