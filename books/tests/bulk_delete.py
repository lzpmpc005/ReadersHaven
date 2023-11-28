import requests

url = "http://localhost:8000/books/bulk_delete"
book_ids = []
for i in range(10, 25000):
    book_ids.append(i)
data = {
    "book_ids": book_ids,
}
response = requests.delete(url, json=data)
print(response.json())