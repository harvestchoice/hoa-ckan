#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

# Use the json module to dump a dictionary to a string for posting.
data_string = urllib.quote(json.dumps({'name': 'Kenya', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))

# We'll use the package_create function to create a new tags
request = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

data_string2 = urllib.quote(json.dumps({'name': 'Somalia', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request2 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request2.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response2 = urllib2.urlopen(request2, data_string2)
assert response2.code == 200

data_string3 = urllib.quote(json.dumps({'name': 'Ethiopia', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request3 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request3.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response3 = urllib2.urlopen(request3, data_string3)
assert response3.code == 200

data_string4 = urllib.quote(json.dumps({'name': 'Uganda', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request4 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request4.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response4 = urllib2.urlopen(request4, data_string4)
assert response4.code == 200

data_string5 = urllib.quote(json.dumps({'name': 'Eritrea', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request5 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request5.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response5 = urllib2.urlopen(request5, data_string5)
assert response5.code == 200

data_string6 = urllib.quote(json.dumps({'name': 'Dijbuti', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request6 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request6.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response6 = urllib2.urlopen(request6, data_string6)
assert response6.code == 200

data_string7 = urllib.quote(json.dumps({'name': 'Sudan', 'vocabulary_id':'0dfb5e91-966d-450d-8046-6a7614217607'}))
request7 = urllib2.Request('http://127.0.0.1/api/3/action/tag_create')
request7.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')
response7 = urllib2.urlopen(request7, data_string7)
assert response7.code == 200

