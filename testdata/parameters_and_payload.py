import json
from utils.user_credential_utils import new_user_generate

new_user = new_user_generate()

# parameter get request
params_with_fixed_email_password = {
    "email": "user@mail.com",
    "password": "Asdfgh123!"
}

params_with_email_password_invalid = {
    "email": "invalidemail@mail.com",
    "password": "invalidpasswordD@"
}

params_with_only_password = {
    'email': '',
    'password': 'Asdfgh123!'
}

# api payloads

payload_with_only_email = json.dumps({
    "email": "user@mail.com",
    # "password": ""
})

payload_with_only_password = json.dumps({
    # "email": "",
    "password": "Asdfgh123!"
})

payload_without_email_password = json.dumps({
})

payload_with_fixed_valid_email_password = json.dumps({
    "email": "user@mail.com",
    "password": "ndsfG@jJdf4325sg"
})

payload_with_new_email_password = json.dumps({
    "email": new_user,
    "password": "Asdfgh123!"
})

play_load_code_send_sucessfully = json.dumps({
    "email": "user@mail.com"
})

forgot_user = json.dumps({
    "email": "user@mail.com"
})

forgot_user_invalid = json.dumps({
    "email": "invalid@mail.com"
})

reset_password_details = json.dumps({
        "email": "user@mail.com",
        "code": 4512
})

reset_password_details_invalid = json.dumps({
        "email": "nas@mail.com",
        "code": 4512
})

reset_password_new_details_valid = json.dumps(
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxNjI3YmUxOWFhYWFhZWE2YmQ2ZGYxMSIsImVtYWlsIjoidXNlckBtYWlsLmNvbSIsInJvbGUiOiJ1c2VyIiwidmVyaWZpZWQiOmZhbHNlLCJpYXQiOjE2MzM5MzYxMjN9.kH2EldG4GoFsFxBgHam1KZ60UAyuGzU6k77SW6Q0H6M",
  "password": "ndsfGjJdf4325sg@"
}
)

reset_password_new_details_invalid = json.dumps(
{
  "token": "MzIzMzF9.-Fz593T-0IPb5kcISRtELF5c3_gFHUwhamQZeIO-1x0",
  "password": "ndsfGjJdf4325sg@"
}
)
