from os import getenv

SECRET_KEY = getenv('SECRET_KEY',None)
MARKET_BASE_URI=getenv('MARKET_BASE_URI',None)