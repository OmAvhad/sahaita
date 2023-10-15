import requests

url = "https://all-serp.p.rapidapi.com/all-serp-website"

querystring = {"keyword":"DoctersNearMe","location":"us","language":"en","search_engine":"google","page_limit":"1","search_type":"All"}

payload = {
	"key1": "value",
	"key2": "value"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "7c1a60fef4mshd626de822882eb6p1dfcf8jsn6efae269683a",
	"X-RapidAPI-Host": "all-serp.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())