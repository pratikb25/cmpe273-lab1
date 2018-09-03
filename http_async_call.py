# Usage: python3.6 <URL>

import asyncio
import requests
import random
import time
import sys

BASE_URL = sys.argv[1]

async def http_call(url):
	response = requests.get(url)
	print("Date: " + response.headers.get('date'))

def main():
	start = time.time()
	evt_loop = asyncio.get_event_loop()
	http_calls = [  asyncio.ensure_future(http_call(BASE_URL)), asyncio.ensure_future(http_call(BASE_URL)), asyncio.ensure_future(http_call(BASE_URL)), ]
	evt_loop.run_until_complete(asyncio.wait(http_calls))
	evt_loop.close()
	end = time.time()
	print("Total time: {}".format(end - start))

main()
