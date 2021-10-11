import allure
from testdata.signup_api.data_signup_with_options_request import response, response_body


@allure.step('Signin api, status code validation')
def test_c119_01_status_code_is_204():
    assert response.status_code == 204


@allure.step("Signin api, response body empty validation")
def test_c119_02_response_body_empty():
    assert response_body is ''
