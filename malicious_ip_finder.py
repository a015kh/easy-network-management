import re
from collections import Counter

white_list_regex = r'192.168.[0-9]{1,3}\.[0-9]{1,3}'

def extract_invalid_ips(log_file_path):
    invalid_ips = []
    pattern = r'Invalid user (\w+) from'
    ip_regex = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(pattern, line)
            match_ip = re.search(ip_regex, line)
            if match_ip and match:
                # find invalid user and its IP
                ip = match_ip.group()
                invalid_ips.append(ip)

    return invalid_ips

# Provide the path to your SSH journal log file
log_file_path = 'journal_ssh.log'
invalid_ips = extract_invalid_ips(log_file_path)

ip_counter = Counter(invalid_ips)

# Print the list of invalid IP
print("Invalid IPs:")
for k, v in ip_counter.items():
    if not re.search(white_list_regex, k) and v > 5:
        # five times tolerance of invalid login
        print(k)
