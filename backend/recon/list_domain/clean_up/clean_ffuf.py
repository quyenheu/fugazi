import json

with open('list_domain/output/out_ffuf.json', 'r') as file:
    temp = json.load(file)

length = len(temp["results"])

with open('list_domain/output/out_ffuf.txt', 'w') as wf:
    for i in range(length) :
        wtemp = temp["results"][i]["host"]
        wf.write(wtemp.strip()+'\n')