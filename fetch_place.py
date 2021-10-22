# Usage: fetch_place.py [FILENAME] [PLACE_ID] [ROBLOSECURITY_COOKIE]
# Example: fetch_place.py place.rbxl 123456789 _|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this...

import requests
import sys

filename = sys.argv[1] # place.rbxl
place_id = sys.argv[2] # 7795117711
auth_cookie = sys.argv[3]

url = f"https://assetdelivery.roblox.com/v1/asset/?id={place_id}"

cookies = {
	".ROBLOSECURITY": auth_cookie
}

def main():
	with requests.get(url, stream=True, cookies=cookies) as res:
		res.raise_for_status()
		with open(filename, "wb") as place_file:
			for chunk in res.iter_content(chunk_size=8192):
				place_file.write(chunk)

if __name__ == "__main__":
	main()
