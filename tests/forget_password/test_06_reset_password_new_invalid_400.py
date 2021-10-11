import allure
from testdata.forget_password.data_reset_password_new_valid_200 import response, response_body


@allure.step('Reset password, Set new password status')
def test_01_reset_set_new_password_error():
    assert response.status_code == 400


@allure.step('Reset password, error message')
def test_02_reset_password_message_success():
    assert "Invalid Token" == response_body["errors"][0]["message"]
