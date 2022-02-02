
from flask import Flask
import pytest,os
from market_tracker.app import create_app
from market_tracker.settings import SECRET_KEY

@pytest.fixture
def app():
    app=create_app()
    app.config['username']='Abhishek'
    app.config['password']='@admin123'
    app.config['SECRET_KEY']='9065a0c8a518421fbdbf67802f9db2b9'
    return app


@pytest.fixture
def secret_key():
    return os.environ.get('SECRET_KEY')


from os import getenv
@pytest.fixture
def client(app):
    SECRET_KEY = getenv('SECRET_KEY',None)
    return app.test_client()
