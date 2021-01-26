**Google Sheets Workout Tracker**

A #100DaysofCode project

This app uses the natural language processing capabilities of nutritionix.com to process an input such as "ran 5 miles 
and cycled 15k" and upload the resulting workout data to a Google Sheet via the sheety.co API.

For testing, sensitive authentication information was stored in a separate secrets.py file (not uploaded). Personal 
data (gender, weight, height, age) are gathered at first run and stored in a JSON file. This information is utilized by 
the nutritionix API to more accurately calculate exercise data such as calories expended.