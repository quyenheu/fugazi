#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 -d domain"
    exit 1
fi

domain=""
name=""
root_domain=""

while getopts "d:n:r:" opt; do
  case $opt in
    d) domain="$OPTARG"
    ;;
    n) name="$OPTARG"
    ;;
    r) root_domain="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
        exit 1
    ;;
  esac
done

if [ -z "$domain" ] || [ -z "$name" ] || [ -z "$root_domain" ]; then
    echo "All of -d (domain), -n (name), and -r (root_domain) are required."
    exit 1
fi

###backup

cp list_domain/output/subdomain.txt list_domain/backup_domain/$domain.txt

echo '' > ./list_domain/output/subdomain.txt
echo '' > ./list_domain/output/out_ffuf.txt
echo '' > ./list_domain/output/out_ffuf.json
echo '' > ./list_domain/output/out_projectdiscovery.txt
echo '' > ./list_domain/output/out_sectrail.txt
echo '' > ./list_domain/output/out_subfinder.txt
echo '' > ./list_domain/output/out_sublist3r.txt
echo '' > ./list_domain/output/out_amass.txt

### start projectdiscovery trước

python3 projectdiscovery_api/create_projectdiscovery.py -d $domain -n $name -rd $root_domain

####sec_trail || python3 sec_trail.py {domain} output/out_sec.txt

python3 sec_trail/sec_trail.py $root_domain list_domain/output/out_sectrail.txt

###amass /////// amass enum -d kaopiz.com -o out.txt 

amass enum -d $root_domain -o list_domain/output/out_amass.txt

## clean output amass

sed 's/\x1B\[[0-9;]*[mK]//g' list_domain/output/out_amass.txt | grep -Eo '([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}' | sort -u > list_domain/output/out_amass.txt

while read -r line; do
    if [[ "$line" != *"$root_domain"* ]]; then
        sed -i "/$line/d" list_domain/output/out_amass.txt
    fi
done < list_domain/output/out_amass.txt

###subfinder  || theem https://vaof out file

subfinder -d $root_domain -o list_domain/output/out_subfinder.txt

###Sublist3r

sublist3r -d $root_domain -o list_domain/output/out_sublist3r.txt

####ffuf data json xấu -> clean lại 

ffuf -w wordlist/min.txt -u https://FUZZ.$root_domain -mc 200,204,202,301,302,401,403 -o list_domain/output/out_ffuf.json 

python3 clean_up/clean_ffuf.py

#### get list domain từ prjectdiscovery (cái get_result_projectdiscovery.py này sẽ tùy chính theo giá trị để lấy dữ liệu)

python3 projectdiscovery_api/get_result_projectdiscovery.py -t host

### clean up 

python3 clean_up/clean_domain.py ### xử lý duplicate
## base on là trên kết quả con projectdiscovery 

##httpx
## cái này sẽ chuyển sang mục status_code

#cat output/res_subdomain.txt | httpx -silent > output/httpx.txt
