import requests

API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "clap thanks",
})
print(output)