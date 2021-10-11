import allure
from testdata.signin_api.data_signin_with_get_request import response, response_body


@allure.step('Signin api, status code validation')
def test_c116_01_status_code_is_404():
    assert response.status_code == 404


@allure.step("Signin api, body not none validation")
def test_c116_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin api, error message validation")
def test_c116_03_error_message():
    assert response_body['errors'][0]["message"] == "Not found"
