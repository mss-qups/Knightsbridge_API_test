import requests
from testdata.api_enpoints import resend_endpoint
from testdata.parameters_and_payload import play_load_user_not_found
from testdata.headers import headers

response = requests.request("POST", resend_endpoint, headers=headers, params=play_load_user_not_found)
response_body = response.json()
# print(response.status_code)
print(response_body)