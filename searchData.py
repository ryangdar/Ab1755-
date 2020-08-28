# Use 'from searchData import searchData' in main()
# Call by inputing a string
# Can change number of 'rows' returned and result offset 'start'
def searchData(searchTerm,rows=1000,start=0):

	# import json
	import requests
	import pandas as pd
	import numpy as np
	import re

	# import time
	# begin = time.time()

	# from ckanapi import RemoteCKAN
	# RemoteCKAN('https://data.cnra.ca.gov/')
	# test = demo.action.package_search(q = "spending water")
	# ckan.logic.action.get.package_search() <-- Need to use this?

	# Websites we search.
	cnraURL = "https://data.cnra.ca.gov/"
	caOpenDataURL = "https://data.ca.gov/"
	# Package search: this is what the default search is on both of the above sites.
	pkgSearch = "api/3/action/package_search?q="
	searchTerm = searchTerm.replace(" ", "%20")
	returnSize = "&rows=" + str(rows) + "&start=" + str(start)

	# Make request from API
	rCNRA = requests.get(cnraURL + pkgSearch + searchTerm + returnSize)
	rCAPortal = requests.get(caOpenDataURL + pkgSearch + searchTerm+ returnSize)

	if(rCNRA.status_code !=200 or rCAPortal.status_code !=200):
		print("There was an error connecting to the sites.")
		return

	if(rCNRA.json()['result']['count'] + rCAPortal.json()['result']['count'] == 0):
		print("No datasets found for: " + searchTerm)
		print("Please try another search.")
		return

	CNRAdf = pd.DataFrame.from_records(rCNRA.json()['result']['results'])
	CNRAdf = CNRAdf.loc[:,['title','name','notes','metadata_created']]
	CNRAdf['name'] = cnraURL + "dataset/" + CNRAdf['name']

	CAPortaldf = pd.DataFrame.from_records(rCAPortal.json()['result']['results'])
	CAPortaldf = CAPortaldf.loc[:,['title','name','notes','metadata_created']]
	CAPortaldf['name'] = caOpenDataURL + "dataset/" + CAPortaldf['name']

	# Removing html tags from 'notes' column
	# Credit: https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
	clean = re.compile('<.*?>')
	for i in range(len(CNRAdf['notes'])):
	    CNRAdf['notes'][i] = re.sub(clean, '', CNRAdf['notes'][i])
	for i in range(len(CAPortaldf['notes'])):
	    CAPortaldf['notes'][i] = re.sub(clean, '', CAPortaldf['notes'][i])

	# Combine and drop duplicates
	combined = pd.concat([CNRAdf, CAPortaldf]).sort_index(kind='merge')
	combined.drop_duplicates(['title'],inplace=True)
	combined = combined.reset_index()
	combined = combined.drop(['index'], axis='columns')

	# end = time.time()
	# print(str(end-begin))
	# This code takes ~5.5s to run for 1000 results from each site

	return combined
