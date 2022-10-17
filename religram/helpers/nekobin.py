import requests

def nekobin(data, title="", author=""):
	BASE_URL = "https://nekobin.com"
	PATH_URL = "/api/documents"
	r = requests.post(BASE_URL + PATH_URL, json={"content": data, "title": title, "author": author})
	if r.status_code not in [200, 201]:
		return "Failed to reach nekobin"
	try:
		return "https://nekobin.com/" + r.json()['result']['key']
	except:
		return "Failed to get API key"
