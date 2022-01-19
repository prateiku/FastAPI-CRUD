"""
Test for the main page using fastapi.testclient.
"""
import sys
from starlette.testclient import TestClient
from app.app import app
import pytest
from httpx import AsyncClient

sys.path.append("C:/Users/HP/Desktop/gcc/Github/async-fastapi-mongo/app")

# Declaring test client
client = TestClient(app)


# Test for status code for get message
def test_get_message():
    response = client.get("/")
    assert response.status_code == 200


# Test for asserting put message
@pytest.mark.anyio
async def test_read():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.put("/read/")
    assert response.status_code == 200
