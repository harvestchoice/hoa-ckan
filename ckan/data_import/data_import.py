#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint
from time import sleep

# Put the details of the dataset we're going to create into a dict.
dataset_dict = [{
	'title': 's sdoarbondioxidewemissionsee',
#	'organization': {'name': 'international-livestock-research-institute'},
	'country_code': ['Ethiopia'],
	'coverage_code': ['Country'],
	'time_start': '1990',
#	'time_end': '2007',
#	'notes': 'Total CO2 emissions divided by the total value of the gross domestic product (GDP) expressed in purchasing power parities (PPPs).For the computation of CO2 emissions, metric tons of CO2 per capita and CO2 emissions in kg CO2 per $1 GDP (PPP) both national and international data are used. National data for CO2 emissions and international data for population estimates (United Nations Population Division, 2007, "World population prospects: The 2006 revision") and GDP (World Bank, 2009, "World Development Indicators 2009")',
#	'resource':[{'name':'UNSD_MDG_2010 Global Monitoring Data'}],
}


]

for i in range(len(dataset_dict)):
	# Use the json module to dump the dictionary to a string for posting.
	data_string = urllib.quote(json.dumps(dataset_dict[i]))

	# We'll use the package_create function to create a new dataset.
	request = urllib2.Request(
	    'http://127.0.0.1/api/3/action/package_create')

	# Creating a dataset requires an authorization header.
	# Replace *** with your API key, from your user account on the CKAN site
	# that you're creating the dataset on.
	request.add_header('Authorization', '3794d926-1fc7-4a55-b30d-d752c2951864')

	# Make the HTTP request.
	response = urllib2.urlopen(request, data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())
	assert response_dict['success'] is True

	# package_create returns the created package as its result.
	created_package = response_dict['result']
	pprint.pprint(created_package)
	
	response.close()
	# sleep(1)
