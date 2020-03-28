import requests

# 1.1 Создаём книгу POST /books/, вы запоминаете его id.

base_url = "http://pulse-rest-testing.herokuapp.com/"
data = {
    "title": "XXX!",
    "author": "Vasya Oblomov"
        }
post_req = requests.post(base_url+"books/", data)
assert post_req.status_code == 201, "Test #1.1 failed: adding new book"

json_body = post_req.json()
book_id = json_body['id']

# 1.2 Проверяете, что она создалась и доступна по ссылке GET/books/[id]

check_book_creating = requests.get(base_url+"books/"+str(book_id))
assert check_book_creating.status_code == 200, "Test #1.2 failed: cannot find new book on direct link"

# 1.3 Проверяете, что она есть в списке книг по запросу GET /books/

book_in_list = requests.get(base_url + "books/")
assert book_in_list.status_code == 200, "Test 1.3 status code not = 200"
json_check_book_body = book_in_list.json()
flag = False
for index in range(len(json_check_book_body)):
    item = json_check_book_body[index]
    if item['id'] == book_id:
        flag = True
assert flag == True, "Test 1.3 failed. Book with such id is not found"

# for index, item in enumerate(json_check_book_body):
#     if item['id'] == book_id:
#         print('Yes', item)

# 1.4 Изменяете данные этой книги методом PUT /books/[id]/
changed_data = {
    "title": "changed title",
    "author": "Unknown author"
}
check_book_creating = requests.put(base_url+"books/"+str(book_id), changed_data)
assert check_book_creating.status_code == 200, "Test 1.4 failed: status code not = 200"

# 1.5 Проверяете, что она изменилась и доступна по ссылке /books/[id]

check_changed_book = requests.get(base_url+"books/"+str(book_id))
assert check_changed_book.status_code == 200, "Test 1.5 failed. cannot find book on direct link"
json_check_changed_book = check_changed_book.json()
flag1 = False
if json_check_changed_book['id'] == book_id and json_check_changed_book['title'] == changed_data["title"] and\
        json_check_changed_book["author"] == changed_data["author"]:
    flag1 = True
assert flag1 == True, "Test 1.5 failed. Book is not found"

# 1.6 Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
changed_book_in_list = requests.get(base_url+"books/")
assert changed_book_in_list.status_code == 200, "Test 1.6 Status code is not 200"
json_changed_book_in_list = changed_book_in_list.json()
flag2 = False
for index in range(len(json_changed_book_in_list)):
    item = json_changed_book_in_list[index]
    if item['id'] == book_id and item['title'] == changed_data["title"] and item["author"] == changed_data["author"]:
        flag2 = True
assert flag2 == True, "Test 1.6 failed. Book is not found in the list of books"

# 1.7 Удаляете эту книгу методом DELETE /books/[id].
delete_book = requests.delete(base_url+"books/"+str(book_id))
assert delete_book.status_code ==204, "Test 1.7 status code is not 204, book isn`t deleted"
check_del_book = requests.get(base_url+"books/"+str(book_id))
assert check_del_book.status_code == 404, "Test 1.7 status code is not 404"

