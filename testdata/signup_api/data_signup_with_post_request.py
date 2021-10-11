import requests
from testdata.headers import headers_post
from testdata.api_enpoints import signup_endpoint
from testdata.parameters_and_payload import new_user, payload_with_new_email_password
from utils.user_credential_utils import write_new_valid_user_credential

response = requests.request("POST", signup_endpoint, headers=headers_post, data=payload_with_new_email_password)
response_body = response.json()
# print(response_body)

# Write valid user to excel
if response.status_code == 201:
    write_new_valid_user_credential([new_user, "Asdfgh123!"])
