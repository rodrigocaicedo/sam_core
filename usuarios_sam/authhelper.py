from urllib import quote, urlencode
import base64
import json
import time
import requests

# Client ID and secret
client_id = '70f95f45-e135-43b8-a769-123ac6ceaae4'
client_secret = 'wq49Tp0Qxyab4hZehZH2yGM'

# Constant strings for OAuth2 flow
# The OAuth authority
authority = 'https://login.microsoftonline.com'

# The authorize URL that initiates the OAuth2 client credential flow for admin consent
authorize_url = '{0}{1}'.format(authority, '/montebelloacademy.onmicrosoft.com/oauth2/v2.0/authorize?{0}')

authorize_url_shared_secret = '{0}{1}'.format(authority, '/montebelloacademy.onmicrosoft.com/adminconsent?{0}')

# The token issuing endpoint
token_url = '{0}{1}'.format(authority, '/montebelloacademy.onmicrosoft.com/oauth2/v2.0/token')

# The token issuing endpoint for  user / pass function

user_pass_token_url = '{0}{1}'.format(authority, '/montebelloacademy.onmicrosoft.com/oauth2/token')



# The scopes required by the app
scopes_app = [ 'https://graph.microsoft.com/.default' ]

scopes = [ 'openid',
           'User.Read',
           'offline_access',
           'Mail.Read' ]

def get_signin_url(redirect_uri):
  # Build the query parameters for the signin url
  params = { 'client_id': client_id,
             'redirect_uri': redirect_uri,
             'response_type': 'code',
             'scope': ' '.join(str(i) for i in scopes)
            }

  signin_url = authorize_url.format(urlencode(params))

  return signin_url

def get_consent_url(redirect_uri):
  # Build the query parameters for the signin url
  params = { 'client_id': client_id,
             'redirect_uri': redirect_uri#,
             #'response_type': 'code',
             #'scope': ' '.join(str(i) for i in scopes_app)
            }

  signin_url = authorize_url_shared_secret.format(urlencode(params))

  return signin_url

def get_token_from_user_pass(username, password):
  post_data = { 'grant_type': 'password',
              'resource': 'https://graph.microsoft.com',
              #'client_id': '21b0a9ad-9328-4ae4-89bd-7bb86dd2e256',
              'client_id': client_id,
              'username': username,
              'password':password
              }

  r = requests.post(user_pass_token_url, data = post_data)

  try:
    return r.json()
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)



def get_token_from_shared_secret():
  post_data = { 'grant_type': 'client_credentials',
              'scope': ' '.join(str(i) for i in scopes_app),
              'client_id': client_id,
              'client_secret': client_secret
              }

  r = requests.post(token_url, data = post_data)

  try:
    return r.json()
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text) 


def get_token_from_code(auth_code, redirect_uri):
  post_data = { 'grant_type': 'authorization_code',
              'code': auth_code,
              'redirect_uri': redirect_uri,
              'scope': ' '.join(str(i) for i in scopes),
              'client_id': client_id,
              'client_secret': client_secret
              }

  r = requests.post(token_url, data = post_data)

  try:
    return r.json()
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)

def get_token_from_refresh_token(refresh_token, redirect_uri):
  # Build the post form for the token request
  post_data = { 'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
                'redirect_uri': redirect_uri,
                'scope': ' '.join(str(i) for i in scopes),
                'client_id': client_id,
                'client_secret': client_secret
              }

  r = requests.post(token_url, data = post_data)

  try:
    return r.json()
  except:
    return 'Error retrieving token: {0} - {1}'.format(r.status_code, r.text)

def get_access_token(request, redirect_uri):
  current_token = request.session['access_token']
  expiration = request.session['token_expires']
  now = int(time.time())
  if (current_token and now < expiration):
    # Token still valid
    return current_token
  else:
    # Token expired
    refresh_token = request.session['refresh_token']
    new_tokens = get_token_from_refresh_token(refresh_token, redirect_uri)

    # Update session
    # expires_in is in seconds
    # Get current timestamp (seconds since Unix Epoch) and
    # add expires_in to get expiration time
    # Subtract 5 minutes to allow for clock differences
    expiration = int(time.time()) + new_tokens['expires_in'] - 300

    # Save the token in the session
    request.session['access_token'] = new_tokens['access_token']
    request.session['refresh_token'] = new_tokens['refresh_token']
    request.session['token_expires'] = expiration

    return new_tokens['access_token']

