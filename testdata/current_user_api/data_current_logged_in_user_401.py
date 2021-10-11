import requests
from testdata.api_enpoints import logged_in_user_endpoint
from testdata.parameters_and_payload import params_with_only_password

response = requests.request("GET", logged_in_user_endpoint, params=params_with_only_password)
response_body = response.json()
# print(response_body)
