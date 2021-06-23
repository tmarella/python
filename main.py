import requests
import json
import os

github_url = "https://api.github.com/user"
github_headers = { 
    "Accept" : "application/vnd.github.v3+json",
    "Authorization" : "token " + os.getenv("GH_TOKEN")
    }
response = requests.request("GET",headers=github_headers,url=github_url)
print(response.status_code)
print(response.json())

