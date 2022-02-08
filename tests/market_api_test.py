
from .conftest import client
from flask import url_for

def test_valid_marketsummary_header(client):
    headers={'x-api-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWJoaXNoZWsiLCJleHAiOjEyNDQzODExMTcyfQ.TgQEYemJOOzPEfI2p_m394JJ33HHAYdtMR_axPRjnks'}
    assert client.get(url_for('market_apis.market_summary'),headers=headers).status_code ==200

def test_marketsummary_invalid_header(client):
    assert client.get(url_for('market_apis.market_summary')).status_code == 400

def test_valid_marketdetails_invalid_payload(client):
    #Payload is Emoty
    headers={'x-api-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWJoaXNoZWsiLCJleHAiOjEyNDQzODExMTcyfQ.TgQEYemJOOzPEfI2p_m394JJ33HHAYdtMR_axPRjnks'}
    response =client.post(url_for('market_apis.get_market_details'),headers=headers)
    assert response.status_code ==400

def test_marketdetails_invalidmethod(client):
    '''Verify response if used GET instead of POST '''
    headers={'x-api-token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWJoaXNoZWsiLCJleHAiOjEyNDQzODExMTcyfQ.TgQEYemJOOzPEfI2p_m394JJ33HHAYdtMR_axPRjnks'}
    response =client.get(url_for('market_apis.get_market_details'),headers=headers)
    assert response.status_code == 405

def test_index(client):
    ''' This to verify index page'''
    # mock_paylod={"username":"Abhishek","password":"@admin123"}
    assert client.get(url_for('index.index')).status_code == 200