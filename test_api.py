import requests
import pytest

base_url = 'https://reqres.in'

def test_get_users():
    response = requests.get(f'{base_url}/api/users?page=2')
    assert response.status_code == 200
    json_data = response.json()
    assert 'data' in json_data
    assert len(json_data['data']) > 0
    assert 'id' in json_data['data'][0]

def test_post_login_success():
    payload = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(f'{base_url}/api/login', json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert 'token' in json_data

def test_post_login_failure():
    payload = {'email': 'invalid@reqres.in'}
    response = requests.post(f'{base_url}/api/login', json=payload)
    assert response.status_code == 400
    json_data = response.json()
    assert 'error' in json_data
    assert json_data['error'] == 'Missing password'