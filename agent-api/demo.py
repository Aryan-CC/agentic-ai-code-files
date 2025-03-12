import requests
BING_SEARCH_KEY = "c3610a34f9774568ac06ddc0467286f9"
BING_SEARCH_URL = "https://api.bing.microsoft.com/"
headers = {"Ocp-Apim-Subscription-Key": BING_SEARCH_KEY}
params = {"q": "test query", "mkt": "en-US", "count": 5}
response = requests.get(BING_SEARCH_URL, headers=headers, params=params)
print(response.status_code)
print(response.text)