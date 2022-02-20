
from .conftest import client
from flask import url_for
import json,os

class TestScenarios:
    def test_valid_marketsummary_header(self,client):
        headers={'x-api-token':os.environ.get('JWT_TOKEN')}
        response = client.get(url_for('market_apis.marketsummary'),headers=headers)
        assert response.status_code ==200
        assert json.loads(response.data)['success'] == True

    def test_invalid_marketsummary_header(self,client):
        response = client.get(url_for('market_apis.marketsummary'))
        assert response.status_code == 400
        assert json.loads(response.data)['message']=='Token is Missing'
        assert json.loads(response.data)['success'] == 'False'

    def test_valid_marketdetails_empty_payload(self,client):
        #Payload is Emoty
        headers={'x-api-token':os.environ.get('JWT_TOKEN')}
        response =client.post(url_for('market_apis.marketsummary'),headers=headers)
        assert response.status_code ==  400
        assert json.loads(response.data)['message'] == 'MARKET_NOT_PROVIDED'
        assert json.loads(response.data)['success'] == False


    def test_valid_marketdetails_invalid_payload(self,client):
        #Payload With Invalid market data
        payload={'market':'a'}
        headers={'x-api-token':os.environ.get('JWT_TOKEN')}
        response =client.post(url_for('market_apis.marketsummary'),headers=headers,query_string=payload)
        assert response.status_code ==  400
        assert json.loads(response.data)['message'] == 'INVALID_MARKET'
        assert json.loads(response.data)['success'] == False 

    def test_home(self,client):
        ''' This to verify index page'''
        # mock_paylod={"username":"Abhishek","password":"@admin123"}
        assert client.get(url_for('index.home')).status_code == 200

    def test_login(self,client):
            payload={'username': os.environ.get('username') , 'password':os.environ.get('password')}
            response = client.post(url_for('index.login'),data = payload)
            assert response.status_code ==200
            assert json.loads(response.data)['success'] == True
            assert json.loads(response.data)['message'] =='Logged in Successfully'
