import requests
from testdata.api_enpoints import logged_in_user_endpoint
from testdata.parameters_and_payload import params_with_fixed_email_password, params_with_email_password_invalid
from testdata.headers import headers


def get_data_current_logged_in(method, endpoint, headers, params):
    # pull current logged in user data
    return requests.request(method, endpoint, headers=headers, params=params)


# response saved to variable to reuse
response = get_data_current_logged_in("GET", logged_in_user_endpoint, headers, params_with_fixed_email_password)
response_body = response.json()


def assert_status_200():
    # validate get successful
    assert response.status_code == 200


def assert_body_not_none():
    # validate body not none
    assert response.json() is not None


def assert_body_field_user():
    # validate "user" as key in user data
    assert "user" in response_body['user']


def assert_body_field_id():
    # validate "id" as key in user data
    assert "id" in response_body['user']


def assert_body_field_email():
    # validate "email" as key in user data
    assert "email" in response_body['user']


def assert_body_field_iat():
    # validate "iat" as key in user data
    assert "iat" in response_body['user']
