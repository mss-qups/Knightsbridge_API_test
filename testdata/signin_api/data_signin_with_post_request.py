import requests
from testdata.headers import headers_post
from testdata.api_enpoints import sign_in_endpoint
from testdata.parameters_and_payload import payload_with_fixed_valid_email_password

response = requests.request("POST", sign_in_endpoint, headers=headers_post, data=payload_with_fixed_valid_email_password)
response_body = response.json()
print(response_body)
