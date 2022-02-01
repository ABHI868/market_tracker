from market_tracker.settings import MARKET_BASE_URI
from os import getenv

MARKET_BASE_URI=getenv('MARKET_BASE_URI')
MARKET_BASE_URI='https://api.bittrex.com'
GET_MARKET_SUMMARIES=MARKET_BASE_URI+'/api/v1.1/public/getmarketsummaries'
GET_MARKET_DETAILS=MARKET_BASE_URI+'/api/v1.1/public/getmarketsummary'
