import json


def record_personal_data():
    print('Tell me a bit about yourself.')
    user_name = input('Name: ')
    user_gender = input('Gender (male/female): ')
    user_weight = int(input('Weight (lbs): '))
    user_height = input('Height (ft,in; example: 5,10): ')
    user_age = int(input('Age: '))

    user_weight_kg = round(user_weight * 0.45359, 1)
    height_tuple = tuple(int(height) for height in user_height.split(','))
    user_height_in = (height_tuple[0] * 12) + height_tuple[1]
    user_height_cm = round(user_height_in * 2.54, 1)

    new_data = {
        user_name.lower(): {
            'gender': user_gender.lower(),
            'weight_kg': user_weight_kg,
            'height_cm': user_height_cm,
            'age': user_age
        }
    }

    try:
        with open('user_data.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        json_dump(new_data)
    else:
        existing_data.update(new_data)
        json_dump(existing_data)

    print('Your data has been saved and loaded.')
    return user_gender, user_weight_kg, user_height_cm, user_age


def json_dump(data):
    with open('user_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


def lookup_user_data(user_name):
    try:
        with open('user_data.json', 'r') as json_file:
            data_dict = json.load(json_file)
    except FileNotFoundError:
        print('No data file created yet.')
        user_data = record_personal_data()
    else:
        if user_name in data_dict.keys():
            user_gender = data_dict[user_name]['gender']
            user_weight_kg = data_dict[user_name]['weight_kg']
            user_height_cm = data_dict[user_name]['height_cm']
            user_age = data_dict[user_name]['age']
            print('Your data has been found and loaded.')
            user_data = (user_gender, user_weight_kg, user_height_cm, user_age)
        else:
            print(f'Oops! No entry exists for {user_name.title()}.')
            user_data = None
    return user_data
