import requests
import json
import pymongo
from datetime import datetime


# Make the API request
response = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=45.41&longitude=13.97&start_date=2003-01-01&end_date=2023-01-01&hourly=temperature_2m&hourly=relativehumidity_2m')

# Check the response status code
if response.status_code == 200:
    data = response.json()

count = 0

# Iterate over the dictionary items
for key, value in data.items():
    count += 1
    # Break the loop after printing the first 10 rows
    if count == 8:
        break

keys_to_delete = list(data.keys())[:8]

# Delete the entries from the dictionary
for key in keys_to_delete:
    del data[key]


atlas_connection_string = 'mongodb+srv://bruno:SIfrajedan1@apvo.jufhzrn.mongodb.net/?retryWrites=true&w=majority'
    # Connect to MongoDB Atlas
client = pymongo.MongoClient(atlas_connection_string)
database = client['climate']
collection = database['temperature_data_daily']


for i in range (0,len(data['hourly']['time']),24 ):
    daily_average_temp = 0
    daily_average_humidity =0
    for j in range(0,24,1):
        daily_average_temp = data['hourly']['temperature_2m'][i+j]+daily_average_temp
        daily_average_humidity =data['hourly']['relativehumidity_2m'][i+j]+daily_average_humidity

    daily_average_temp = daily_average_temp/24
    daily_average_humidity = daily_average_humidity/24
    formatted_date = datetime.strptime(data['hourly']['time'][i], "%Y-%m-%dT%H:%M").strftime("%Y-%m-%d")

    temp_data = {
                "time" : formatted_date,
                "temp" :     daily_average_temp,
                "humidity": daily_average_humidity,

                }
    collection.insert_one(temp_data)

print("Data stored to mongoDB atlas successfully.")