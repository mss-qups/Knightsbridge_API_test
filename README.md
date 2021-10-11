# KNIGHTSBRIDGE_API_Testing

This project is a starting point for `KNIGHTSBRIDGE` API testing.

### API Routes:

Base URL : `http://47.251.2.96:3000`<br />
Sign up : `/api/users/signup`<br />
Sign in : `/api/users/signin`<br />
Current_user: `/api/users/currentuser`<br />

### Sing Up

Route is tested for different combination of payload :

`with only email`,
`with only password`,
`without email & password`

Route is tested for different request methods:

`GET`, `POST`, `PUT` , `Delete`, `Options`

Response code, body, field & messages are asserted according to test scenarios:

`200`,`201`,`204` for successful request. Fields from response body asserted for successful request.

`400`,`404`  for bad or failed request. Error messages from response body asserted for failed or bad request.

N.B: Successfully created user credentials are stored in an Excel file.

### Sing In

Route is tested for different combination of payload :

`with only email`,
`with only password`,
`without email & password`

Route is tested for different request methods:

`GET`, `POST`, `PUT` , `Delete`, `Options`

Response code, body, field & messages are asserted according to test scenarios:

`200`,`201`,`204` for successful request. Fields from response body asserted for successful request.

`400`,`404`  for bad or failed request. Error messages from response body asserted for failed or bad request.

### Current User

Route is tested for different combination of payload :

`with Bearer token`,
`without Bearer token`

Route request method:

`PUT`

Response code, body, field & messages are asserted according to test scenarios:

`200` for successful request. Fields from response body asserted for successful request.

`400` for bad request. Error messages from response body asserted for bad request.

## Project Structure

`data`: Data files are stoted here <br />
`testcases`: All testcases belongs here<br />
`testdata`: All methods & data related to testcases belongs here<br />
`testconf`: Project settings configuration & run commands are stored her<br />
`utils`: Utility functions are stored here.

## Installation

##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ run: pip3 install -r requirements.txt

## Run Project

    $ cd to the "Test" directory
    $ run: python3 testconf/runtest.py
