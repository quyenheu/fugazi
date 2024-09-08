##### xử lý duplicate 

def merge_unique_subdomains(output_file, *input_files):
    unique_subdomains = set() # tạo set chống duplicate subdomain

    for input_file in input_files:
        with open(input_file, 'r') as f:
            for line in f:
                subdomain = line.strip() 
                if subdomain: 
                    unique_subdomains.add(subdomain)

    with open(output_file, 'w') as f_out:
        for subdomain in sorted(unique_subdomains):
            f_out.write(subdomain + '\n')

merge_unique_subdomains(
    'list_domain/output/res_subdomain.txt', 
    'list_domain/output/out_amass.txt', 
    'list_domain/output/out_ffuf.txt', 
    'list_domain/output/out_projectdiscovery.txt', 
    'list_domain/output/out_sectrail.txt', 
    'list_domain/output/out_subfinder.txt', 
    'list_domain/output/out_sublist3r.txt'
)
