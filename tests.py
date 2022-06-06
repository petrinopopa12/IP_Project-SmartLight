import pytest
import json
import unittest
from app import create_app





class OutcomeTests(unittest.TestCase):

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

    #teste de verificare
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

    #auth test
    def test_register_succesfull(client):
        payload = {'name':'TestName','password':'TestPassword','height':'190','hair_length':'long'}
        landing = client.post('/auth/register', data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == "user registered succesfully"


    #light test
    def test_get_weather(client):
        landing = client.get("/light/color")
        assert landing.status_code == 200

    def test_set_weather(client):
        payload = {'color': 'blue', 'time' : '01/27/22'}
        landing = client.put("/color/time", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == 'Light preference added successfully!'


    #music test
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


    #routine test
    def test_get_weather(client):
        landing = client.get("/light/routine")
        assert landing.status_code == 200

    def test_set_weather(client):
        payload = {'color': 'blue', 'time' : '01/27/22'}
        landing = client.put("/color/time", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == 'Light preference added successfully!'


    #users test
    def test_register(client):
        payload = {'name': 'test_username', 'country': 'Romania','password' : 'test_parola'}
        res = client.post('/auth/register', data=json.dumps(payload), follow_redirects=True)
        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert res_data["message"] == 'user registered succesfully'

        payload = {'name': 'test_username', 'country': 'Romania','password' : 'test_parola'}
        res = client.post('/auth/register', data=json.dumps(payload), follow_redirects=True)
        res_data = json.loads(res.data.decode())
        assert res.status_code == 403
        assert res_data["message"] == f'User {payload["name"]} is already registered.'

    def test_login_user_not_found(client):
        payload = {
            'name': 'NotExistingUser',
            'password':'NotExistingPassword'
        }
        landing = client.post("/auth/login", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 403
        assert res["message"] == "user not found"

    def test_login_user_wrong_password(client):
        payload = {
            'name': 'test_username',
            'password':'NotExistingPassword'
        }
        landing = client.post("/auth/login", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 403
        assert res["message"] == "password is incorrect"

    def test_login_succesful(client):
        payload = {
            'name': 'test_username',
            'password':'test_parola'
        }
        landing = client.post("/auth/login", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == "user logged in succesfully"

        landing = client.get("/light/color")
        assert landing.status_code == 200

    def test_get_users(client):
        landing = client.get("/users")
        assert landing.status_code == 200

    def test_add_user(client):
        payload = {'name': 'test_username', 'country': 'Romania','password' : 'test_parola'}
        res = client.post('/users', data=json.dumps(payload), follow_redirects=True)
        assert res.status_code == 200

        payload = {'country':'Romania'}
        res = client.post('/users', data=json.dumps(payload), follow_redirects=True)
        res_data = json.loads(res.data.decode())
        assert res_data["message"] == 'Fields must be nonempty!'

    def test_get_single_user(client):
        landing = client.get("/users/unit_test_name")
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["name"] == "unit_test_name"
        assert res["country"] == "Romania"
        assert res["password"] == "test_parola"

    def test_modify_user(client):
        payload = {'new_name': 'updated_unit_test_name', 'new_country':'not_Romania'}
        landing = client.put("/users/unit_test_name", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == 'User updated!'

    def test_delete_user(client):
        landing = client.delete("/users/updated_unit_test_name")
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == 'Successfully deleted!'


    #weather test
    def test_get_weather(client):
        landing = client.get("/weather/meteo")
        assert landing.status_code == 200

    def test_set_weather(client):
        payload = {'meteo': '40.5', 'time1' : '01/27/22'}
        landing = client.put("/weather/meteo", data=json.dumps(payload), follow_redirects=True)
        res = json.loads(landing.data.decode())
        assert landing.status_code == 200
        assert res["message"] == 'Weather parameters added successfully!'


    #usage test
    def test_get_usage(client):
        landing = client.get("/usage")
        assert landing.status_code == 200

if __name__ == '__main__':
    unittest.main()