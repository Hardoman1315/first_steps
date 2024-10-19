import json
import csv


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


with open("in.json", "r") as input_file:
    user_data = json.load(input_file)

valid_users = conditions_complete(user_data)

with open("out.csv", "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['name', ' address', ' email'])
    for user in valid_users:
        writer.writerow([user['name'], user['address'], user['email']])
