import requests
import json
from testdata.api_enpoints import forgot_password_endpoint
from testdata.parameters_and_payload import play_load_code_send_sucessfully
from testdata.headers import headers_post


response = requests.request("POST", forgot_password_endpoint, headers=headers_post, data=play_load_code_send_sucessfully)
response_body = response.json()
print(response.status_code)
print(response_body['message'])
