import pytest
import json
import unittest
from main import create_app
#nu stiu dc trebuie


@pytest.fixture(scope="session", autouse=True)
def client():
    local_app = create_app()
    client = local_app.test_client()

    yield client

def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert 'Welcome to SmartLight!' in html
    assert landing.status_code == 200

def test_music_get_not_existing_id(client):
        not_existing_id = '123456789436364215'
        landing = client.get(f'/song/{not_existing_id}', follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["error"]["message"] == "invalid id"

def test_music_get_succesfull(client):
        existing_id = '11dFghVXANMlKmJXsNCbNl'
        landing = client.get(f'/song/{existing_id}', follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["id"] == existing_id


if __name__ == '__main__':
    unittest.main()

