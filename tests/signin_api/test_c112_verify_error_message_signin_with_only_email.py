import allure
from testdata.signin_api.data_signin_with_only_email import response, response_body


@allure.step('Signin api, status code validation')
def test_c112_01_status_code_is_400():
    assert response.status_code == 400


@allure.step("Signin api, response body not none validation")
def test_c112_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin api, error message validation")
def test_c112_03_error_message():
    assert response_body['errors'][0]["message"] == "You must supply a password"


@allure.step("Signin api, required field password validation")
def test_c112_04_required_field_password():
    assert response_body['errors'][0]["field"] == "password"
