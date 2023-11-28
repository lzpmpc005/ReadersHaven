import requests

url = "http://localhost:8000/books/booklist/"
data = {
    "page": 1000,
    "num_per_page": 10,
}
response = requests.get(url, params=data)
print(response.json())