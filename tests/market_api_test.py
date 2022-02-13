
from .conftest import client
from flask import url_for
import json,os

def test_valid_marketsummary_header(client):
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response = client.get(url_for('market_apis.marketsummary'),headers=headers)
    assert response.status_code ==200
    assert json.loads(response.data)['success'] == True

def test_invalid_marketsummary_header(client):
    response = client.get(url_for('market_apis.marketsummary'))
    assert response.status_code == 400
    assert json.loads(response.data)['message']=='Token is Missing'
    assert json.loads(response.data)['success'] == 'False'

def test_valid_marketdetails_empty_payload(client):
    #Payload is Emoty
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response =client.post(url_for('market_apis.marketsummary'),headers=headers)
    assert response.status_code ==  400
    assert json.loads(response.data)['message'] == 'MARKET_NOT_PROVIDED'
    assert json.loads(response.data)['success'] == False


def test_valid_marketdetails_invalid_payload(client):
    #Payload is Emoty
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response =client.post(url_for('market_apis.marketsummary'),headers=headers)
    assert response.status_code ==  400
    assert json.loads(response.data)['message'] == 'MARKET_NOT_PROVIDED'
    assert json.loads(response.data)['success'] == False 

def test_home(client):
    ''' This to verify index page'''
    # mock_paylod={"username":"Abhishek","password":"@admin123"}
    assert client.get(url_for('index.home')).status_code == 200