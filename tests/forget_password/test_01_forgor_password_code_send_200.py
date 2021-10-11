import allure
from testdata.forget_password.data_new_code_200 import response, response_body


@allure.step('Forget User Response Code')
def test_01_forget_password_response():
    assert response.status_code == 200


@allure.step('Forget User Response Code')
def test_01_forget_password_message():
    assert 'a code has been sent' in response_body['message']
