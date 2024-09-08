import requests
from tqdm import tqdm
import multiprocessing
import json
import argparse

def get_sub_domains(domain,filepath):
  url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
  querystring = {"children_only":"false"}
  headers = {
  'accept': "application/json",
  'apikey': "BLS45ZYenmltYCwAHIHeEljnqn_Cxt_W"
  }
  API_response = requests.get(url, headers=headers, params=querystring)

  result_json=json.loads(API_response.text)

  sub_domains=[i+'.'+domain for i in result_json['subdomains']]
  f=open(filepath,'w+')
  for i in sub_domains:
    f.write(i+'\n')
  f.close()

  with open(filepath, 'r') as f:
    links_all = f.read().splitlines()

  return links_all

def get_resp(link):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        requests.packages.urllib3.disable_warnings()
        response = requests.get(link, timeout=3, verify=False, headers=headers)
        status_code = str(response.status_code)
        values = link + " returns " + status_code
    except:
        values = link + " returns nothing"
    return values

def run(dom, file):
    results=[]
    links = get_sub_domains(dom,file)

    with multiprocessing.Pool() as pool:
        for result in tqdm(pool.imap(get_resp, links), total=len(links)):
            if "200" in result: 
                temp = result.strip().split(" ")
                results.extend([temp[0]])
    #print(results)      
    output_file = "response_code.txt"
    with open(output_file,'w') as tfile:
         tfile.write('\n'.join(results))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find sub-domains and get their response codes.")
    parser.add_argument('domain', type=str, help="Domain name to find its sub-domains")
    parser.add_argument('output_file', type=str, help="Output filename to save all domain names from API response")
    args = parser.parse_args()

    dom = args.domain
    output_file = args.output_file
    print(dom, output_file)
    run(dom, output_file)

