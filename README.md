# market_tracker
This repo will keep track of all the markets. It will refer to the data made available by bitrix.


Login api- Will generate JWT token using the username entered by the user and encode it with a SECRET KEY.


MARKET_SUMMARIES - This api will return all the market details via a GET call.
But user will need to be authenticated via JWT token passed in the request header


GET_MARKET_DETAILS - This api will return details of a specific market passed in the request param

Run pip install -r requirements.txt to install dependencies to your local repo 

#To run via docker ###
Install docker and docker-compose on your machine and then 
RUN docker-compose up

#To run testcases use below command 
pytest -c tests/pytest.ini 
