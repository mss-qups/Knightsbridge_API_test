import requests
from testdata.api_enpoints import logged_in_user_endpoint
from testdata.parameters_and_payload import params_with_fixed_email_password, params_with_only_password
from testdata.headers import headers


def get_data_current_logged_in(method="", endpoint="", headers=None, params=""):
    # pull current logged in user data
    return requests.request(method, endpoint, headers=headers, params=params)


# response saved to variable to reuse
response = get_data_current_logged_in("GET", logged_in_user_endpoint, headers, params_with_fixed_email_password)
response_body = response.json()


def assert_response_status(code=200, valid=True):
    if valid:
        assert response.status_code == code
    else:
        invalid_response = get_data_current_logged_in("GET", logged_in_user_endpoint, params_with_only_password)
        assert invalid_response.status_code == code


def assert_body_not_none():
    # validate body not none
    assert response.json() is not None


def assert_key_in_response(key):
    # validate key in response body
    assert key in response_body['user']
