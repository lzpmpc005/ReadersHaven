import requests

url = "http://localhost:8000/books/booklist/"
data = {
    "page": 1,
    "num_per_page": 20,
}
response = requests.get(url, params=data)
print(response.json())