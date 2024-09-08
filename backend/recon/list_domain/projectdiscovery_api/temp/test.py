import requests
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

url = "https://api.projectdiscovery.io/v1/asset/enumerate/crdskbnfls8s73aobi30/contents"


headers = {"X-API-Key": "97f3d5b0-0c72-4bdb-9021-ca7a99ed79a9"}

response = requests.request("GET", url, headers=headers)

result_json = json.loads(response.text)


print(result_json)


