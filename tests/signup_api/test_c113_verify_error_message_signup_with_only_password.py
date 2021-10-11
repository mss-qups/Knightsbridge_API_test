import allure
from testdata.signup_api.data_signup_with_only_password import response, response_body


@allure.step('Signin api, status code validation')
def test_c113_01_status_code_is_400():
    assert response.status_code == 400


@allure.step("Signin api, response body not none validation")
def test_c113_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin api, error message validation")
def test_c113_03_error_message():
    assert response_body['errors'][0]["message"] == "Email must be valid"


@allure.step("Signin api, required field email validation")
def test_c113_04_required_field_email():
    assert response_body['errors'][0]["field"] == "email"
