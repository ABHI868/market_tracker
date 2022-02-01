from flask import Flask
import pytest


@pytest.fixture
def client():
    app=Flask(__name__)
    app=app.test_client()
    return app