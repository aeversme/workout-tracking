import secrets
import data
import requests

user_data = data.lookup_user_data()

exercise_input = input('Tell me which exercises you did: ')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': secrets.APP_ID,
    'x-app-key': secrets.API_KEY,
    'x-remote-user-id': 0
}

request_body = {
    'query': f'{exercise_input}',
    'gender': 'male',
    'weight_kg': 81.6,
    'height_cm': 185.4,
    'age': 39,
}
