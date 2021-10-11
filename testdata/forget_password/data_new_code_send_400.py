import requests
from testdata.api_enpoints import forgot_password_endpoint
from testdata.parameters_and_payload import forgot_user_invalid
from testdata.headers import headers_post

response = requests.request("POST", forgot_password_endpoint, headers=headers_post, params=forgot_user_invalid)
response_body = response.json()
print(response.status_code)
print(response_body)
