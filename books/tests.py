import requests
import time

start = time.time()
url = "http://127.0.0.1:8000/books/bulk_add"
data = {
    # path of csv file
    "csv_file": "E:\LU_Leipzig\ProgramClinic\ReadersHaven_Li\\books.csv",
    # size of each batch
    "chunk_size": 10000,
}
response = requests.post(url, json=data)
print(response.json())
# test how different chunk_size influence the processing time
end = time.time()
time = end - start
print(f'time used: {time:.2f} seconds')
# result is almost no influence, interesting... why?
