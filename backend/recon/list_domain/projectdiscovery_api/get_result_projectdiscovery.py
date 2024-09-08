import requests
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Process domain and project name.')
parser.add_argument('-t', '--type', required=True, help='type of get data')

args = parser.parse_args()
type = args.type

sys.stdout.reconfigure(encoding='utf-8')

url = "https://api.projectdiscovery.io/v1/asset/enumerate/cre83tcvsktc73ckqpjg/contents"


headers = {"X-API-Key": "dfea01db-6b9d-44f3-9a95-ec961adbd8ca"}

if type == "host":

    querystring = {"limit":"10000","type":"hosts"}
    response = requests.request("GET", url, headers=headers, params=querystring)

    result_json = json.loads(response.text)


    with open("list_domain/output/out_projectdiscovery.txt", "w") as wf:
        for i in range(len(result_json["data"])):
            wf.write(result_json["data"][i]["host"].strip()+'\n')

# elif type == "technology":

# ['technology_details']

# elif type == "ip":

# ['ip']

# elif type == ""

#template example

# {
# 'created_at':'2024-09-07T03:42:17.082091Z',
# 'enumeration_id':'crdskbnfls8s73aobi30',
# 'host':'enterpriseenrollment.mbbank.com.vn',
# 'id':217670766,
# 'ip':'20.91.147.72',
# 'is_new':False,
# 'name':'enterpriseenrollment.mbbank.com.vn:80',
# 'port':80,
# 'technology_details':{
# },
# 'type':'ports',
# 'updated_at':'2024-09-07T03:42:17.082091Z'
# }
