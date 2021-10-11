import requests
from testdata.api_enpoints import forgot_password_endpoint
from testdata.parameters_and_payload import reset_password_details_invalid
from testdata.headers import headers_post


response = requests.request("POST", forgot_password_endpoint, headers=headers_post, data=reset_password_details_invalid)
response_body = response.json()
print(response_body["errors"][0]["message"])
print(response.status_code)
print(response.text)
