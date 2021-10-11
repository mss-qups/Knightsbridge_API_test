import allure
from testdata.forget_password.data_reset_password_invalid import response, response_body


@allure.step('Reset password status for invalid details')
def test_01_reset_password_status():
    assert response.status_code == 400


@allure.step('Reset password status for invalid details returned message')
def test_02_reset_password_message_error():
    assert "This email is not registered" == response_body["errors"][0]["message"]
