import data
import requests
import secrets
import datetime as dt


def user_inputs():
    user_name = input('Enter your name to search for your data: ').lower()
    user_data = data.lookup_user_data(user_name)
    exercise_input = input('Tell me which exercises you did: ')
    return user_data, exercise_input


def nutritionix_api(user_data, exercise_input):
    exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    headers = {
        'x-app-id': secrets.APP_ID,
        'x-app-key': secrets.API_KEY,
        'x-remote-user-id': '0'
    }
    request_body = {
        'query': f'{exercise_input}',
        'gender': user_data[0],
        'weight_kg': user_data[1],
        'height_cm': user_data[2],
        'age': user_data[3],
    }

    nutrutionix_api_response = requests.post(url=exercise_endpoint, headers=headers, json=request_body)
    exercises_list = nutrutionix_api_response.json()['exercises']
    return exercises_list


def sheety_api(exercises_list):
    today = dt.datetime.now()
    today_date = today.strftime('%d/%m/%Y')
    now_time = today.strftime('%X')

    sheety_endpoint = 'https://api.sheety.co/4b0869518e0351cf4d4a00ef6134a7b7/myWorkouts/workouts'
    sheety_header = {
        'Authorization': secrets.BEARER_KEY,
        'Content-Type': 'application/json'
    }

    for exercise in exercises_list:
        row_input = {
            'workout': {
                'date': today_date,
                'time': now_time,
                'exercise': exercise['name'].title(),
                'duration': exercise['duration_min'],
                'calories': round(exercise['nf_calories'])
            }
        }

        sheety_api_response = requests.post(url=sheety_endpoint, headers=sheety_header, json=row_input)
        print('Your workout has been uploaded to your Google Sheet.')
