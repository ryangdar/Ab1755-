# Use 'from searchData import searchData' in main()
# Call by inputing a string
def searchData(searchTerm):

	import json
	import requests
	import pandas as pd
	import numpy as np

	# Websites we search.
	cnraURL = "https://data.cnra.ca.gov/"
	caOpenDataURL = "https://data.ca.gov/"
	# Package search: this is what the default search is on both of the above sites.
	pkgSearch = "api/3/action/package_search?q="
	size = "&rows=100"
	# print("Please input a search term: ")
	# Need to replace spaces with '+'
	# searchTerm = input()
	# searchTerm = searchTerm.replace(" ", "+")
	# print(searchTerm)
	# searchTerm = str(searchTerm)
	# Make request from API
	rCNRA = requests.get(cnraURL + pkgSearch + searchTerm +size)
	rCAPortal = requests.get(caOpenDataURL + pkgSearch + searchTerm +size)

	if(rCNRA.json()['result']['count'] + rCAPortal.json()['result']['count'] == 0):
		print("No datasets found for: " + searchTerm)
		print("Please try another search.")
		return

	maxCNRA = 100 # Want to print 10 or less results.
	if(rCNRA.json()['result']['count'] < maxCNRA):
		maxCNRA = rCNRA.json()['result']['count']
	maxCAData = 100 # Want to print 10 or less results.
	if(rCAPortal.json()['result']['count'] < maxCAData):
		maxCAData = rCAPortal.json()['result']['count']

	# This prints results from data.cnra.ca.gov.
	# Prints database's title, URL, description and date it was updated. This is
	# what is displayed using search on the actual websites.
	CNRAdata = []
	for i in range(0, maxCNRA):
		temp = []
		temp.append(rCNRA.json()['result']['results'][i]['title'])
		temp.append(cnraURL + "dataset/" + rCNRA.json()['result']['results'][i]['name'])
		temp.append(rCNRA.json()['result']['results'][i]['notes'])
		temp.append(rCNRA.json()['result']['results'][i]['metadata_created'])
		CNRAdata.append(temp)
	CNRAdf = pd.DataFrame(CNRAdata, columns = ['title','name','notes','metadata_created']) 
	# print(CNRAdf.count())
	# This prints results from data.ca.gov.
	# Prints database's title, URL, description and date it was updated. This is
	# what is displayed using search on the actual websites.
	CAPortaldata = []
	for i in range(0, maxCAData):
		temp = []
		temp.append(rCAPortal.json()['result']['results'][i]['title'])
		temp.append(caOpenDataURL + "dataset/" + rCAPortal.json()['result']['results'][i]['name'])
		temp.append(rCAPortal.json()['result']['results'][i]['notes'])
		temp.append(rCAPortal.json()['result']['results'][i]['metadata_created'])
		CAPortaldata.append(temp)
	CAPortaldf = pd.DataFrame(CAPortaldata, columns = ['title','name','notes','metadata_created']) 
	# print(CAPortaldf.count())

	return CNRAdf


# print(rCNRA.json()['result']['results'][i]['title'])
# print(cnraURL + "dataset/" + rCNRA.json()['result']['results'][i]['name'])
# print(rCNRA.json()['result']['results'][i]['notes'])
# print(rCNRA.json()['result']['results'][i]['metadata_created']+"\n")

# 	print(rCAPortal.json()['result']['results'][i]['title'])
# 	print(caOpenDataURL + "dataset/" + rCAPortal.json()['result']['results'][i]['name'])
# 	print(rCAPortal.json()['result']['results'][i]['notes'])
# 	print(rCAPortal.json()['result']['results'][i]['metadata_created']+"\n")