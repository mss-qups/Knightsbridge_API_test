import requests
from testdata.headers import headers_post
from testdata.api_enpoints import signup_endpoint
from testdata.parameters_and_payload import payload_with_only_email

response = requests.request("POST", signup_endpoint, headers=headers_post, data=payload_with_only_email)
response_body = response.json()
# print(response_body)
