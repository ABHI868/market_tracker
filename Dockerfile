FROM python:alpine3.7
COPY . /market_tracker
WORKDIR /market_tracker
EXPOSE 7000
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
