# Usage: publish_place.py [FILENAME] [UNIVERSE_ID] [PLACE_ID] [AUTH_KEY]
# Example: fetch_place.py place.rbxl 123456789 123456789 abcdefg

import requests
import sys
import json
from pathlib import Path

filename = sys.argv[1] # place.rbxl
universe_id = sys.argv[2] # 123456789
place_id = sys.argv[3] # 7795117711
auth_key = sys.argv[4] # abcdefg

url = f"https://apis.roblox.com/universes/v1/${universe_id}/places/${place_id}/versions"

def main():
	with open(filename, 'rb') as place:
		data = place.read()
	headers = {
		'Content-Type': 'application/octet-stream',
		'x-api-key': auth_key
	}
	res = requests.post(
		url,
		headers=headers,
		data=data
	)
	res.raise_for_status()
	res_data = res.json() # e.g. {"versionNumber":1}
	with open(Path(filename).with_suffix('.json'), 'w') as place_response:
		place_response.write(json.dumps(res_data, indent=2))

if __name__ == "__main__":
	main()
