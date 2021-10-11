import allure
from testdata.forget_password.data_reset_password_new_valid_200 import response, response_body


@allure.step('Reset password, Set new password')
def test_01_reset_set_new_password():
    assert response.status_code == 200


@allure.step('Reset password, returned message')
def test_02_reset_password_message_success():
    assert "Password Updated successfully" == response_body["message"]
