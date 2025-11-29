import csv
import requests
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

domains = []
with open("domains.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1:
            domains.append(row[1])  

def check_domain(domain):
    url = f"https://{domain}"
    start = time.time()
    try:
        requests.get(url, timeout=3)
        response_time = round(time.time() - start, 3)

        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = "N/A"

        return domain, response_time, ip

    except:
        return domain, "N/A", "N/A"
    
start_time = time.time()
results = []
max_workers = 50
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(check_domain, d): d for d in domains}
    for future in as_completed(futures):
        results.append(future.result())
with open("result.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")