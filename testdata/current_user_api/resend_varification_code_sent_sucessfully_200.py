import requests
from testdata.api_enpoints import resend_endpoint
from testdata.parameters_and_payload import play_load_resend_message
from testdata.headers import headers

response = requests.request("POST", resend_endpoint, headers=headers, params=play_load_resend_message)
response_body = response.json()
print(response.status_code)
