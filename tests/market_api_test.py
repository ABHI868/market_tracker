
from .conftest import client
from flask import url_for
import json,os

def test_valid_marketsummary_header(client):
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response = client.get(url_for('market_apis.market_summary'),headers=headers)
    assert response.status_code ==200
    assert json.loads(response.data)['success'] == True

def test_invalid_marketsummary_header(client):
    response = client.get(url_for('market_apis.market_summary'))
    assert response.status_code == 400
    assert json.loads(response.data)['message']=='Token is Missing'
    assert json.loads(response.data)['success'] == 'False'

def test_valid_marketdetails_empty_payload(client):
    #Payload is Emoty
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response =client.post(url_for('market_apis.get_market_details'),headers=headers)
    assert response.status_code ==  400
    assert json.loads(response.data)['message'] == 'MARKET_NOT_PROVIDED'
    assert json.loads(response.data)['success'] == False

# def test_valid_marketdetails_invalid_payload(client,invalid_params):
#     #Payload is Emoty
#     headers={'x-api-token':os.environ.get('JWT_TOKEN')}
#     response =client.post(url_for('market_apis.get_market_details'),headers=headers,data=json.dumps({'test':'value'}))
#     assert response.status_code ==  400
#     assert json.loads(response.data)['message'] == 'INVALID_MARKET'
#     assert json.loads(response.data)['success'] == False 

def test_marketdetails_invalidmethod(client):
    '''Verify response if used GET instead of POST '''
    headers={'x-api-token':os.environ.get('JWT_TOKEN')}
    response =client.get(url_for('market_apis.get_market_details'),headers=headers)
    assert response.status_code == 405

def test_index(client):
    ''' This to verify index page'''
    # mock_paylod={"username":"Abhishek","password":"@admin123"}
    assert client.get(url_for('index.index')).status_code == 200