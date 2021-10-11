import allure
from testdata.forget_password.data_new_code_send_400 import forgot_user_invalid, response_body, response


@allure.step('Forget User Response Code')
def test_01_forget_password_response():
    assert response.status_code == 400


@allure.step('Forgot password error message')
def test_02_forget_password_error_message():
    assert 'errors' in response_body
