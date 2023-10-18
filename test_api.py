# https://restful-booker.herokuapp.com/apidoc/index.html
import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200


@pytest.fixture(scope='function')
def get_id():
    payload = {
        "firstname": "Mike",
        "lastname": "SDET",
        "totalprice": 987,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    id = response.json()['bookingid']
    yield id, response, payload


def test_get_booking():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK
    assert "Connection" in response.headers, f"Headers is missing in {response.headers}"


def test_get_by_id():
    response = requests.get(f"{BASE_URL}/1")
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    for item in expected_keys:
        assert item in response_data.keys(), f"key {item} is missing from response data"


def test_create_booking():
    payload = {
        "firstname": "Mike",
        "lastname": "SDET",
        "totalprice": 987,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(BASE_URL, json=payload)
    print(response.json())
    assert response.status_code == STATUS_OK

    # testing for user id if it contains new firstname, lastname and total price

    id = response.json()['bookingid']

    user_check = requests.get(f"{BASE_URL}/{id}")

    for k, v in payload.items():
        print(user_check.json()[k])
        assert v == user_check.json()[k], f"{v} is missing"


def test_create_booking_with_fixture(get_id):
    response = get_id[1]

    assert response.status_code == STATUS_OK

    # testing for user id if it contains new firstname, lastname and total price

    user_check = requests.get(f"{BASE_URL}/{get_id[0]}")

    for k, v in get_id[2].items():
        print(user_check.json()[k])
        assert v == user_check.json()[k], f"{v} is missing"


@pytest.fixture(scope='function')
def post_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


def test_delete_booking(get_id, post_token):
    headers = {'Cookie': f'token={post_token}'}
    response = requests.delete(f"{BASE_URL}/{get_id[0]}", headers=headers)
    print(get_id, response)
    assert response.status_code == 201
    get_response = requests.get(f"{BASE_URL}/{get_id}")
    assert get_response.status_code == 404
