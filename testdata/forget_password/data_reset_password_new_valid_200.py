import requests
from testdata.api_enpoints import reset_password_new_endpoint
from testdata.parameters_and_payload import reset_password_new_details_valid
from testdata.headers import headers_post


response = requests.request("POST", reset_password_new_endpoint, headers=headers_post, data=reset_password_new_details_valid)
response_body = response.json()
print(response.status_code)
print(response.text)
