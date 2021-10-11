from testdata.get_token import token

bearer_token = 'Bearer ' + str(token)
headers = {'Authorization': bearer_token}
headers_post = {'Content-Type': 'application/json'}
print(token)

