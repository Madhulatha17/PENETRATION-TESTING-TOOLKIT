import requests

def analyze_headers(url):
    response = requests.get(url)

    print("\nHTTP Headers\n")

    for key, value in response.headers.items():
        print(f"{key}: {value}")
