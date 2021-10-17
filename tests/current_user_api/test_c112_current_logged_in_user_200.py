import allure
from testdata.current_user_api.get_data_current import \
    assert_status_200, \
    assert_body_not_none, \
    assert_body_field_user, \
    assert_body_field_id, \
    assert_body_field_email, \
    assert_body_field_iat, \


@allure.step('Logged_in user details, status code validation')
def test_c112_01_status_code_is_200():
    assert_status_200()


@allure.step("Logged_in user details, body not none validation")
def test_c112_03_response_body_not_none():
    assert_body_not_none()


@allure.step("Logged_in user details, body field user validation")
def test_c112_04_body_field_id():
    assert_body_field_id()


@allure.step("Logged_in user details, body field id validation")
def test_c112_05_body_field_user():
    assert_body_field_user()


@allure.step("Logged_in user details, body field email validation")
def test_c112_06_body_field_email():
    assert_body_field_email()


@allure.step("Logged_in user details, body field iat validation")
def test_c112_07_body_field_iat():
    assert_body_field_iat()
