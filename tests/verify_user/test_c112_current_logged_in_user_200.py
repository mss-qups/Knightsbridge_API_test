import allure
from testdata.current_user_api.data_current_logged_in_user_200 import response, response_body


@allure.step('Logged_in user details, status code validation')
def test_c112_01_status_code_is_200():
    assert response.status_code == 200


@allure.step("Logged_in user details, body not none validation")
def test_c112_02_response_body_not_none():
    assert response_body is not None


@allure.step("Logged_in user details, body field user validation")
def test_c112_03_body_field_user():
    assert 'user' in response_body


@allure.step("Logged_in user details, body field id validation")
def test_c112_04_body_field_id():
    assert 'id' in response_body['user']


@allure.step("Logged_in user details, body field email validation")
def test_c112_05_body_field_email():
    assert 'email' in response_body['user']


@allure.step("Logged_in user details, body field iat validation")
def test_c112_06_body_field_iat():
    assert 'iat' in response_body['user']
