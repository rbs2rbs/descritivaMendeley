import requests
import requests.auth
import urllib
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost/' # or whatever you've set it to in your API
AUTHORIZE_URL = 'https://api-oauth2.mendeley.com/oauth/authorize'
TOKEN_URL = 'https://api-oauth2.mendeley.com/oauth/token'


client_auth = requests.auth.HTTPBasicAuth('6757', 'aeJToGCAnxNPYyQq')
post_data = {"grant_type": "authorization_code",
                "code": 'unUY0fPyv_bSkhiQKmG0SgaRJYM',
                "redirect_uri": 'https://www.glmrconsultoria.com.br'}
response = requests.post(TOKEN_URL,
                            auth=client_auth,
                            data=post_data)
token_json = response.json()


print(token_json)