#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import uuid
import json
import string
import random

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

normal_letters = {
u"a":[u"á",u"â",u"ä",u"à", u"Á",u"Â",u"Ä",u"À"],
u"e":[u"è",u"ê",u"é",u"ë", u"Ê",u"È",u"Ë",u"É"],
u"i":[u"ì",u"î",u"í",u"ï", u"Î",u"Ì",u"Ï",u"Í"],
u"o":[u"ò",u"ô",u"ó",u"ö", u"Ô",u"Ò",u"Ó",u"Ö"],
u"u":[u"ù",u"û",u"ú",u"ü", u"Û",u"Ù",u"Ú",u"Ü"],
u"ni":[u"ñ", u"Ñ"],
u"":[u".",u"*", u" "]

}


url = 'http://192.99.20.125/support/api/http.php/tickets.json'

key='494874603CD193B3BDDC98E93CE0E9B9'


def make_api_call(method, payload = None, parameters = None ):
  headers = {'X-API-Key': '{0}'.format(key), 
             'User-Agent': 'osTicket API Client v1.8'
             }
  
  response = None

  if (method.upper() == 'GET'):
      response = requests.get(url, headers = headers, params = parameters)
  elif (method.upper() == 'DELETE'):
      response = requests.delete(url, headers = headers, params = parameters)
  elif (method.upper() == 'PATCH'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.patch(url, headers = headers, data = json.dumps(payload), params = parameters)
  elif (method.upper() == 'POST'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.post(url, headers = headers, data = json.dumps(payload), params = parameters)

  return response



def make_api_call2(method, url, token, user_email, payload = None, parameters = None):
  # Send these headers with all API calls
  headers = { 'User-Agent' : 'localhost2/1.0',
              'Authorization' : 'Bearer {0}'.format(token),
              'Accept' : 'application/json'#,
              #'X-AnchorMailbox' : user_email 
              }

  # Use these headers to instrument calls. Makes it easier
  # to correlate requests and responses in case of problems
  # and is a recommended best practice.
  request_id = str(uuid.uuid4())
  instrumentation = { 'client-request-id' : request_id,
                      'return-client-request-id' : 'true' }

  headers.update(instrumentation)

  response = None

  if (method.upper() == 'GET'):
      response = requests.get(url, headers = headers, params = parameters)
  elif (method.upper() == 'DELETE'):
      response = requests.delete(url, headers = headers, params = parameters)
  elif (method.upper() == 'PATCH'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.patch(url, headers = headers, data = json.dumps(payload), params = parameters)
  elif (method.upper() == 'POST'):
      headers.update({ 'Content-Type' : 'application/json' })
      response = requests.post(url, headers = headers, data = json.dumps(payload), params = parameters)

  return response




def create_ticket(payload):

  payload = payload

  r = make_api_call('POST', payload, parameters = None)


  if r.ok:
    return r.json()
  else:
    raise Exception(_(u'Could not create ticket. Status code: {0} - Details: {1}'.format(r.status_code, r.text)))
    #raise ValidationError(_('create group function failed to retrieve an Office 365 group element.'), params={'get_groups status code': r.status_code, 'details':r.text},)
    #return "{0}: {1}".format(r.status_code, r.text)





"""
def get_me(access_token):
  get_me_url = graph_endpoint.format('/me')

  

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields
  query_parameters = {u'$select': u'displayName,mail,givenName'}

  r = make_api_call('GET', get_me_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def get_my_photo(access_token):
  get_my_photo_url = graph_endpoint.format('/me/photo/$value')

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields
  query_parameters = {}
  #query_parameters = {'$select': 'displayName,mail'}

  r = make_api_call('GET', get_my_photo_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok or 204):
    return r.content
  else:
    return "{0}: {1}".format(r.status_code, r.text)



def get_my_messages(access_token, user_email):
  get_messages_url = graph_endpoint.format('/me/mailfolders/inbox/messages')

  # Use OData query parameters to control the results
  #  - Only first 10 results returned
  #  - Only return the ReceivedDateTime, Subject, and From fields
  #  - Sort the results by the ReceivedDateTime field in descending order
  query_parameters = {u'$top': u'10',
                      u'$select': u'receivedDateTime,subject,from',
                      u'$orderby': u'receivedDateTime DESC'}

  r = make_api_call('GET', get_messages_url, access_token, user_email, parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    #i = Image.open(BytesIO(r.content))
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def get_users(access_token):

  get_users_url = graph_endpoint.format('/users')

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields
  query_parameters = {u'$select': u'displayName,mail,givenName'}

  r = make_api_call('GET', get_users_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)

def get_groups(nombre = None):
  get_groups_url = graph_endpoint.format('/groups')

  token = get_token_from_shared_secret()
  access_token = token["access_token"]

  if nombre == None:
    query_parameters = None
  else:

    query_parameters = {u'$filter': u"displayName eq '{0}'".format(nombre)}

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields

  r = make_api_call('GET', get_groups_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    raise Exception(_(u'get group function failed to retrieve an Office 365 group element. Status code: {0} - Details: {1}'.format(r.status_code, r.text)))
    #raise ValidationError(_('get group function failed to retrieve an Office 365 group element.'), params={'get_groups status code': r.status_code, 'details':r.text},)
    #return "{0}: {1}".format(r.status_code, r.text)


def check_member(user, group):



  check_member_url = graph_endpoint.format(u"/users/{0}/memberOf".format(user))
  token = get_token_from_shared_secret()
  access_token = token["access_token"]
  r = make_api_call('GET', check_member_url, access_token, "", parameters = None)

  r_json = r.json()
  try:

    for x in r_json["value"]:
      if x["id"] == group:
        return True
    else:
      return False
  except:
    return False



def user_to_group(user, group):
  user_to_group_url = graph_endpoint.format("/groups/{0}/members/$ref".format(group))

  token = get_token_from_shared_secret()
  access_token = token["access_token"]

  payload = {
  "@odata.id":"https://graph.microsoft.com/v1.0/users/{0}".format(user)
  }

  r = make_api_call('POST', user_to_group_url, access_token, "", payload, parameters = None)

  if (r.status_code == requests.codes.ok):
    return r.json
  else:
    raise Exception(_(u'user to group function failed to register the user {2} in the group {3}. Status code: {0} - Details: {1}'.format(r.status_code, r.text, user, group)))


def create_group(display_name, mail_nickname):
  get_groups_url = graph_endpoint.format("/groups")

  token = get_token_from_shared_secret()
  access_token = token["access_token"]

  payload = {
  "displayName":display_name,
  "mailEnabled": "true",
  "mailNickname":mail_nickname,
  "securityEnabled": "false",
  "groupTypes":["Unified"]
  }


  r = make_api_call('POST', get_groups_url, access_token, "", payload, parameters = None)



  if r.ok:
    return r.json()
  else:
    raise Exception(_(u'user to group function failed to create the group. Status code: {0} - Details: {1}'.format(r.status_code, r.text)))
    #raise ValidationError(_('create group function failed to retrieve an Office 365 group element.'), params={'get_groups status code': r.status_code, 'details':r.text},)
    #return "{0}: {1}".format(r.status_code, r.text)



def create_student(first_name, father_last_name, mother_last_name):
  email_domain = "@student.montebelloacademy.org"
  user = create_user(first_name, father_last_name, mother_last_name, email_domain)
  return user

def create_tutor(first_name, father_last_name, mother_last_name):
  email_domain = "@tutor.montebelloacademy.org"
  user = create_user(first_name, father_last_name, mother_last_name, email_domain)
  return user

def create_parent(first_name, father_last_name, mother_last_name):
  email_domain = "@tutor.montebelloacademy.org"
  user = create_user(first_name, father_last_name, mother_last_name, email_domain)
  return user



def create_user(first_name, father_last_name, mother_last_name, email_domain):

  token = get_token_from_shared_secret()
  access_token = token["access_token"]

  get_users_url = graph_endpoint.format('/users')



  password = ""
  for x in range(8):
      if x==0:
          password = "{}".format(random.choice(string.uppercase))
      elif x >= 4:
          password = "{0}{1}".format(password, random.choice(string.digits))
      elif x % 2 == 0:
          password = "{0}{1}".format(password, random.choice(string.lowercase))
      else:
          password = "{0}{1}".format(password, random.choice(["a","e","i","o","u"]))

  payload = {
  "accountEnabled":"true",
  "givenName": first_name,
  "surName": "{0} {1}".format(father_last_name, mother_last_name),
  "passwordProfile":{"forceChangePasswordNextSignIn":"true", "password": password}
  }

  display_name = "{0} {1} {2}".format(first_name, father_last_name, mother_last_name)


  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields


  #query_parameters = {'$select': 'displayName,mail,givenName'}
  first_name = first_name.lower()
  first_name = first_name.decode("utf-8")
  lista_name = first_name.split()
  start_len_name = len(lista_name[0])
  father_last_name = father_last_name.lower()
  father_last_name = father_last_name.decode("utf-8")
  mother_last_name = mother_last_name.lower()
  mother_last_name = mother_last_name.decode("utf-8")

  for x in normal_letters:
    for y in normal_letters[x]:
      first_name = first_name.replace(y,x)
      father_last_name = father_last_name.replace(y,x)
      mother_last_name = mother_last_name.replace(y,x)

  
  mail_nickname = "{0}.{1}".format(first_name[0:start_len_name], father_last_name)
  user_principal_name = "{0}{1}".format(mail_nickname, email_domain)

  payload["mailNickname"] = mail_nickname
  payload["userPrincipalName"] = user_principal_name
  #payload["mail"] = user_principal_name
  payload["displayName"] = display_name 

  r = make_api_call('POST', get_users_url, access_token, "", payload, parameters = None)


  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    data = r.json()

    counter_first = 0
    counter_last = 0
    counter_number = 0


    while "error" in data and data["error"]["message"] == "Another object with the same value for property userPrincipalName already exists.":


      mail_nickname = "{0}.{1}".format(first_name[0:start_len_name+counter_first+1], father_last_name)
      user_principal_name = "{0}{1}".format(mail_nickname, email_domain)
      
      payload["mailNickname"] = mail_nickname
      payload["userPrincipalName"] = user_principal_name
      #payload["mail"] = user_principal_name

      r = make_api_call('POST', get_users_url, access_token, "", payload, parameters = None)

      print mail_nickname
      print user_principal_name

      data = r.json()

      counter_first += 1

      if counter_first >= len(first_name)-start_len_name:
        while "error" in data and data["error"]["message"] == "Another object with the same value for property userPrincipalName already exists.":
          mail_nickname = "{0}.{1}{2}".format(first_name, father_last_name, mother_last_name[0:counter_last +1])
          user_principal_name = "{0}{1}".format(mail_nickname, email_domain)
          
          payload["mailNickname"] = mail_nickname
          payload["userPrincipalName"] = user_principal_name
          #payload["mail"] = user_principal_name

          r = make_api_call('POST', get_users_url, access_token, "", payload, parameters = None)

          print mail_nickname
          print user_principal_name

          data = r.json()

          counter_last += 1

          if counter_last >= len(mother_last_name):
            mail_nickname = "{0}.{1}{2}{3}".format(first_name, father_last_name, mother_last_name, counter_number+1)
            user_principal_name = "{0}{1}".format(mail_nickname, email_domain)
            payload["mailNickname"] = mail_nickname
            payload["userPrincipalName"] = user_principal_name
            #payload["mail"] = user_principal_name

            r = make_api_call('POST', get_users_url, access_token, "", payload, parameters = None)

            print mail_nickname
            print user_principal_name

            data = r.json()

            counter_number += 1

    return data


"""