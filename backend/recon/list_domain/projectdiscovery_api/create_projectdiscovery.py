import requests
import argparse

url = "https://api.projectdiscovery.io/v1/asset/enumerate"

parser = argparse.ArgumentParser(description='Process domain and project name.')
parser.add_argument('-d', '--domain', required=True, help='Input domain')
parser.add_argument('-n', '--name', required=True, help='Project name')
parser.add_argument('-rd', '--root_domain', required=True, help='Project name')


args = parser.parse_args()
GLOBAL_INPUT_DOMAIN = args.domain
GLOBAL_NAME_PROJECT = args.name
GLOBAL_ROOT_DOMAIN = args.root_domain

GLOBAL_INPUT_DOMAIN = GLOBAL_INPUT_DOMAIN.strip()
GLOBAL_NAME_PROJECT = GLOBAL_NAME_PROJECT.strip()
GLOBAL_ROOT_DOMAIN = GLOBAL_ROOT_DOMAIN.strip()

payload = {
    "root_domains": ["{}".format(GLOBAL_ROOT_DOMAIN)],
    "enrichment_inputs": ["{}".format(GLOBAL_INPUT_DOMAIN)],
    "name": "{}".format(GLOBAL_NAME_PROJECT),
    "steps": ["dns_resolve","http_probe","port_scan","dns_passive","dns_bruteforce","dns_permute"],
    "enumeration_ports": "top-1000",
    "enumeration_config": {"follow-redirect":True}
}

headers = {
    "X-API-Key": "dfea01db-6b9d-44f3-9a95-ec961adbd8ca",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.status_code)