# Usage: /usr/bin/python3.6 <URL>

''' Import 'requests' module '''
import time
import sys
import requests

def parse_and_show_date(resp):
	print("'date' : '" + resp.headers.get('date') + "'")

def http_call(url):
	print("HTTP request to URL: " + url)
	response = requests.get(url)
	return response

def main():
	# url = "https://webhook.site/3e70a89a-af69-48d6-955a-eeb88d169442"
	start = time.time()
	url = sys.argv[1]
	for i in range(3):
		print("\n");
		response = http_call(url)
		parse_and_show_date(response)
	end = time.time()
	print("Total time: {}".format(end - start))

main()
