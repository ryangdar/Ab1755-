import json
import requests

# Websites we search.
cnraURL = "https://data.cnra.ca.gov/"
caOpenDataURL = "https://data.ca.gov/"
# Package search: this is what the default search is on both of the above sites.
pkgSearch = "api/3/action/package_search?q="

print("Please input a search term: ")
searchTerm = input()

# Make request from API
rCNRA = requests.get(cnraURL + pkgSearch + searchTerm)
rCAPortal = requests.get(caOpenDataURL + pkgSearch + searchTerm)

if(rCNRA.json()['result']['count'] + rCAPortal.json()['result']['count'] == 0):
	print("No datasets found for: " + searchTerm)
	print("Please try another search.")
	# return

maxCNRA = 10 # Want to print 10 or less results.
if(rCNRA.json()['result']['count'] < maxCNRA):
	maxCNRA = rCNRA.json()['result']['count']
maxCAData = 10 # Want to print 10 or less results.
if(rCAPortal.json()['result']['count'] < maxCAData):
	maxCAData = rCAPortal.json()['result']['count']

# This prints results from data.cnra.ca.gov.
# Prints database's title, URL, description and date it was updated. This is
# what is displayed using search on the actual websites.
for i in range(0, maxCNRA):
	print(rCNRA.json()['result']['results'][i]['title'])
	print(cnraURL + "dataset/" + rCNRA.json()['result']['results'][i]['name'])
	print(rCNRA.json()['result']['results'][i]['notes'])
	print(rCNRA.json()['result']['results'][i]['metadata_created']+"\n")

# This prints results from data.ca.gov.
# Prints database's title, URL, description and date it was updated. This is
# what is displayed using search on the actual websites.
for i in range(0, maxCAData):
	print(rCAPortal.json()['result']['results'][i]['title'])
	print(caOpenDataURL + "dataset/" + rCAPortal.json()['result']['results'][i]['name'])
	print(rCAPortal.json()['result']['results'][i]['notes'])
	print(rCAPortal.json()['result']['results'][i]['metadata_created']+"\n")
