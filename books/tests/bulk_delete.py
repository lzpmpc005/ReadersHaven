import requests

url = "http://localhost:8000/books/bulk_delete"

data = {
    "book_ids": [11, 12, 13, 14, 15, 16, 17, 18, 19],
}
response = requests.delete(url, json=data)
print(response.json())