import requests
from testdata.api_enpoints import forgot_password_endpoint
from testdata.parameters_and_payload import play_load_sever_error
from testdata.headers import headers

response = requests.request("POST", forgot_password_endpoint, headers=headers, params=play_load_sever_error)
response_body = response.json()
print(response.status_code)
# print(response_body)