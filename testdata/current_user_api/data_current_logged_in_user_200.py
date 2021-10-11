import requests
from testdata.api_enpoints import logged_in_user_endpoint
from testdata.parameters_and_payload import params_with_fixed_email_password
from testdata.headers import headers

response = requests.request("GET", logged_in_user_endpoint, headers=headers, params=params_with_fixed_email_password)
response_body = response.json()
print(response_body)
