import requests
import pytest

url = "https://stapi.technodom.kz/config-discovery/api/v1/cities"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)