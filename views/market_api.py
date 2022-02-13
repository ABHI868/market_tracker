
from market_tracker.authentication.jwt_token import check_for_token
from flask import request,Blueprint,Response,json
import requests
from market_tracker.constants import GET_MARKET_SUMMARIES,GET_MARKET_DETAILS
from flask_restful import Api,Resource

market_apis=Blueprint('market_apis',__name__)

api=Api(market_apis)

class MarketSummary(Resource):

    # @check_for_token
    method_decorators=[check_for_token]
    def get(self):
        data=requests.get(GET_MARKET_SUMMARIES).json()
        return data

    # @check_for_token
    def post(self):
        ''' Will return details of a specific market passed as a query param in POST call'''
        try:
            params={key:request.args.get(key) for key in request.args.keys()}
            data=requests.post(url=GET_MARKET_DETAILS,params=params).json()
            status =200 if data.get('success') else 400
        except Exception as e:
                data['error_msg']=str(e)
        return Response(json.dumps(data), status=status or 400)


api.add_resource(MarketSummary,"/market_summaries")
