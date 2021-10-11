import requests
from testdata.api_enpoints import forgot_password_endpoint
from testdata.parameters_and_payload import reset_password_details
from testdata.headers import headers_post


response = requests.request("POST", forgot_password_endpoint, headers=headers_post, data=reset_password_details)
response_body = response.json()
print(response.status_code)
print(response.text)
