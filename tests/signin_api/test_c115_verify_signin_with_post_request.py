import allure
from testdata.signin_api.data_signin_with_post_request import response, response_body


@allure.step('Signin api, status code validation')
def test_c115_01_status_code_is_200():
    assert response.status_code == 200


@allure.step("Signin api, body not none validation")
def test_c115_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin api, body field token validation")
def test_c115_03_body_field_email():
    assert 'email' in response_body


@allure.step("Signin api, body field token validation")
def test_c115_04_body_field_token():
    assert 'token' in response_body
