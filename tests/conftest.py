
from flask import Flask
import pytest,os
from market_tracker.app import create_app
from market_tracker.settings import SECRET_KEY

@pytest.fixture
def app():
    app=create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()
