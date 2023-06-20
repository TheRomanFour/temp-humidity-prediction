import requests
import json
import pymongo
# Make the API request
response = requests.get('https://archive-api.open-meteo.com/v1/archive?latitude=45.41&longitude=13.97&start_date=2003-01-01&end_date=2023-01-01&hourly=temperature_2m&hourly=relativehumidity_2m')

# Check the response status code
if response.status_code == 200:
    data = response.json()

    # Write the data to a JSON file
    with open('weather_data.json', 'w') as file:
        json.dump(data, file)

    print("Data saved to weather_data.json successfully.")
else:
    print('Error - status code is not 200!')

count = 0

# Iterate over the dictionary items
for key, value in data.items():
    print(key, value)
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
collection = database['temperature_data']


for i in range (len(data['hourly']['time'])):
    temp_data = {
                "time" : data['hourly']['time'][i],
                "temp" : data['hourly']['temperature_2m'][i],
                "humidity" : data['hourly']['relativehumidity_2m'][i]

                }
    collection.insert_one(temp_data)

print("Data stored to mongoDB atlas successfully.")
