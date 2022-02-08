
from market_tracker.authentication.jwt_token import check_for_token
from flask import request,Blueprint,Response,json
import requests
from market_tracker.constants import GET_MARKET_SUMMARIES,GET_MARKET_DETAILS

market_apis=Blueprint('market_apis',__name__)

@market_apis.route("/market_summaries")
@check_for_token
def market_summary():
    ''' Will return summary of all the markets '''
    data=requests.get(GET_MARKET_SUMMARIES).json()
    return data

@market_apis.route('/getmarketsummary',methods=['POST'])
@check_for_token
def get_market_details():
    ''' Will return details of a specific market passed as a query param in POST call'''
    try:
        params={key:request.args.get(key) for key in request.args.keys()}
        data=requests.post(url=GET_MARKET_DETAILS,params=params).json()
        status =200 if data.get('success') else 400
    except Exception as e:
            data['error_msg']=str(e)
    return Response(json.dumps(data), status=status or 400)
