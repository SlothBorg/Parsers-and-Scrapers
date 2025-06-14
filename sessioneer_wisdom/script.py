import json
import os
import requests

BASE_URL = "https://api.sessioneer.cc/api/wisdom/"
DEFAULT_LOCATION = "json_data"

def call_json_api(url=BASE_URL + "tree"):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.sessioneer.cc/",
        "Content-Type": "application/json",
        "Origin": "https://www.sessioneer.cc",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4",
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    return response.json()


def extract_paths(data):
    paths = []

    def walk(node):
        if "path" in node:
            paths.append(node["path"])
        if "children" in node and node["children"]:
            for child in node["children"]:
                walk(child)

    for item in data.get("value", []):
        walk(item)

    return paths


def save_json_to_file(data, filename):
    os.makedirs(DEFAULT_LOCATION, exist_ok=True)

    file_path = os.path.join(DEFAULT_LOCATION, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    print("Getting JSON tree")
    json_data = call_json_api()

    print("Extracting PATH values")
    paths = extract_paths(json_data)

    for path in paths:
        print(f"Calling JSON api for {path}")
        data = call_json_api(BASE_URL + path)

        print(f"Saving {path}.json")
        save_json_to_file(data, path)
