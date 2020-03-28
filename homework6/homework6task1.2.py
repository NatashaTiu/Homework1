
import requests

# 1.2.1 Создаём роль POST /roles/,  запоминаем его id.
book_id = 215
base_url = "http://pulse-rest-testing.herokuapp.com/"
role_data = {
    "name": "Vasya Pupkin",
    "type": "super hero",
    "level": 101,
    "book": base_url+"books/"+str(book_id)
        }
create_role = requests.post(base_url +"roles/", role_data)
assert create_role.status_code == 201, "Test 1.2.1 failed. Role was not created"
json_role = create_role.json()
role_id = json_role["id"]
print(role_id)

# 1.2.2 Проверяете, что она создалась и доступна по ссылке GET/roles/[id]
check_creating = requests.get(base_url+"roles/"+str(role_id))
assert check_creating.status_code == 200, "Test 1.2.2 failed. Cannot find role on direct link"
json_check_creating = check_creating.json()
flag3 = False
if role_id == json_check_creating["id"] and json_check_creating["name"] == role_data["name"] and\
        json_check_creating["type"] == role_data["type"] and json_check_creating["level"] == role_data["level"] and\
        json_check_creating["book"] == role_data["book"]:
    flag3 = True
assert flag3 == True, "Test 1.2.2 failed. Check all parameters of role"


# 1.2.3 Проверяете, что она есть в списке ролей по запросу GET /roles/

check_creating_in_list = requests.get(base_url+"roles/")
assert check_creating_in_list.status_code == 200, "Status code is not 200"
json_check_role_in_l = check_creating_in_list.json()
flag4 = False
for index in range(len(json_check_role_in_l)):
    item = json_check_role_in_l[index]
    if role_id == item["id"] and item["name"] == role_data["name"] and item["type"] == role_data["type"] and\
            item["level"] == role_data["level"] and item["book"] == role_data["book"]:
        flag4 = True
assert flag4 == True, "Test 1.2.3 failed. Cannot find new role in list of roles"


# 1.2.4 Изменяете данные этой роли методом PUT /roles/[id]/
role_changed_data = {
    "name": "Vasyliy Pupkin",
    "type": "super-puper hero",
    "level": 102,
    "book": base_url + "books/" + str(book_id)
        }
change_role = requests.put(base_url+"roles/"+str(role_id), role_changed_data)
assert change_role.status_code == 200, "Test 1.2.4 is failed"

# 1.2.5 Проверяете, что она изменилась и доступна по ссылке /roles/[id]
check_changed_role = requests.get(base_url+"roles/"+str(role_id))
assert check_changed_role.status_code == 200, "Test 1.2.5. cannot find role on direct link"
json_changed_role = check_changed_role.json()
flag5 = False
if role_id == json_changed_role["id"] and json_changed_role["name"] == role_changed_data["name"] and\
        json_changed_role["type"] == role_changed_data["type"] and json_changed_role["level"] == role_changed_data["level"] and\
        json_changed_role["book"] == role_changed_data["book"]:
    flag5 = True
assert flag5 == True, "Test 1.2.5. failed. Cannot find changed role "

# 1.2.6 Проверяете, что она есть в списке ролей по GET /roles/ с новыми данными.

check_changed_role_in_list = requests.get(base_url+"roles/")
assert check_changed_role_in_list.status_code == 200, "Test 1.2.6 cannot get list of roles"
json_changed_role_in_l = check_changed_role_in_list.json()
flag6 = False
for item in range(len(json_changed_role_in_l)):
    item = json_changed_role_in_l[index]
    if role_id == item["id"] and item["name"] == role_changed_data["name"] and item["type"] == role_changed_data["type"] and \
            item["level"] == role_changed_data["level"] and item["book"] == role_changed_data["book"]:
        flag6 = True
assert flag6 == True, "Test 1.2.6 failed. Cannot find changed role in list of roles"

# 1.2.7 Удаляете эту role методом DELETE /roles/[id].

delete_role = requests.delete(base_url+"roles/"+str(role_id))