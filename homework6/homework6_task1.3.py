import requests

# 1.1 Создаём книгу POST /books/ без имени и автора

base_url = "http://pulse-rest-testing.herokuapp.com/"
data = {
    "title": 3,
    "author": ""
        }
post_req = requests.post(base_url+"books/", data)
print(post_req.status_code)
assert post_req.status_code == 201, "Test #1.1 failed: adding new book"

json_body = post_req.json()
book_id = json_body['id']