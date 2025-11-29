import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_foto(photo_id):
    url = f"https://jsonplaceholder.typicode.com/photos/{photo_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    start = time.perf_counter()

    photos = []

    with ThreadPoolExecutor(max_workers=30) as executor:
        future_tasks = [executor.submit(fetch_foto, x) for x in range(1, 5000)]

        for task in future_tasks:
            photos.append(task.result())

    with open("photos.json", "w") as file:
        json.dump(photos, file, indent=4)

    finish = time.perf_counter()
    print(f"Finished in {finish - start} seconds.")

main()