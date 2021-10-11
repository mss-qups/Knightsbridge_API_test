import allure
from testdata.signin_api.data_signin_without_email_password import response, response_body


@allure.step('Signin api, status code validation')
def test_c114_01_status_code_is_400():
    assert response.status_code == 400


@allure.step("Signin api, response body not none validation")
def test_c114_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin api, error message validation")
def test_c114_03_error_message():
    assert response_body['errors'][0]["message"] == "Email must be valid"


@allure.step("Signin api, required field email validation")
def test_c114_04_required_field_email():
    assert response_body['errors'][0]["field"] == "email"


@allure.step("Signin api, error message validation")
def test_c114_05_error_message():
    assert response_body['errors'][1]["message"] == "You must supply a password"


@allure.step("Signin api, required field password validation")
def test_c114_06_required_field_password():
    assert response_body['errors'][1]["field"] == "password"
