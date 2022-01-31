from middlewares.auth import check_for_token
from flask import request,Blueprint
import requests
from constants import GET_MARKET_SUMMARIES,GET_MARKET_DETAILS

market_apis=Blueprint('market_apis',__name__)

@market_apis.route("/market_summaries")
@check_for_token
def market_summary():
    response=requests.get(GET_MARKET_SUMMARIES).json()
    return response

@market_apis.route('/getmarketsummary',methods=['POST'])
@check_for_token
def get_market_details():
    params={key:request.args.get(key) for key in request.args.keys()}
    response=requests.post(url=GET_MARKET_DETAILS,params=params).json()
    return response
