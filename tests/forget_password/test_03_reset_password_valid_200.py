import allure
from testdata.forget_password.data_reset_password import response, response_body


@allure.step('Reset password status')
def test_01_reset_password_status():
    assert response.status_code is 200



