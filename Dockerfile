FROM python:alpine3.7
COPY . /market_tracker
WORKDIR /market_tracker
EXPOSE 7000
RUN pip install -r requirements.txt
RUN pytest -c tests/pytest.ini 
