import json
import csv
import os


is_existed = False


def conditions_complete(users) -> dict:
    for data in users:
        if "phoneNumber" in data and "userAgent" in data:
            phone = data["phoneNumber"]
            browser = data["userAgent"]
            is_american = phone.startswith('+1') or phone.startswith('1')
            is_safari = '4.0 Safari' in browser
            if is_american and is_safari:
                yield {
                    "name": data["name"],
                    "address": data["address"],
                    "email": data["email"]
                }


def extract_file() -> dict:
    global is_existed
    while not is_existed:
        path_to_file = input("Укажите директорию файла \'in.json\',"
                             "или оставьте строку пустой,если файл находится в этой же директории \n")
        path_to_file = path_to_file + "in.json"
        if not os.path.exists(path_to_file):
            print(f"Указанного пути не существует. Попробуйте ещё раз")
        else:
            is_existed = True
    with open(path_to_file, "r") as input_file:
        user_data = json.load(input_file)
        return user_data


def save_to_CSV(valid_list):
    path_to_file = input("Укажите директорию для создания файла \'out.csv\',"
                 "или оставьте строку пустой,если файл находится в этой же директории \n")
    path_to_file = path_to_file + "out.csv"
    with open(path_to_file, "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['name', ' address', ' mail'])
        for user in valid_list:
            writer.writerow([user['name'], user['address'], user['email']])


users_data = extract_file()
valid_users = conditions_complete(users_data)
save_to_CSV(valid_users)
