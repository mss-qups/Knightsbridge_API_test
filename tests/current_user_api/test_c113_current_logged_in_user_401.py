import allure
from testdata.current_user_api.data_current_logged_in_user_401 import response, response_body


@allure.step('Logged_in user details, status code validation')
def test_c112_01_status_code_is_400():
    assert response.status_code == 401


@allure.step("Logged_in user details, body not none validation")
def test_c112_02_response_body_not_none():
    assert response_body is not None


@allure.step("Logged_in user details, error field validation")
def test_c112_03_error_field():
    assert 'errors' in response_body


@allure.step("Logged_in user details, error message validation")
def test_c112_04_error_message():
    assert response_body['errors'][0]["message"] == "You are unauthorized"
