import pymongo
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def plot_polynomial_regression(dates, temperatures, humidity, degree=2):
    # Convert lists to numpy arrays
    dates = np.array(dates)
    temperatures = np.array(temperatures)
    humidity = np.array(humidity)

    # Convert dates to proper datetime format
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

    # Reshape the arrays
    temperatures = temperatures.reshape(-1, 1)
    humidity = humidity.reshape(-1, 1)

    # Create polynomial features
    poly_features = PolynomialFeatures(degree=degree)
    X = poly_features.fit_transform(np.concatenate((temperatures, humidity), axis=1))

    # Create and fit the polynomial regression model
    model = LinearRegression()
    model.fit(X, temperatures)

    # Generate data points for the polynomial regression line
    temperature_range = np.linspace(min(temperatures), max(temperatures), 100).reshape(-1, 1)
    humidity_range = np.linspace(min(humidity), max(humidity), 100).reshape(-1, 1)
    X_range = poly_features.transform(np.concatenate((temperature_range, humidity_range), axis=1))
    predictions = model.predict(X_range)

    # Plot the graph with dates and temperature
    plt.plot(dates, temperatures, label='Actual Data')
    plt.plot(dates, predictions, color='red', label='Polynomial Regression')

    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Polynomial Regression with Temperature and Humidity')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# Replace <Atlas_Connection_String> with your actual connection string
atlas_connection_string = 'mongodb+srv://bruno:SIfrajedan1@apvo.jufhzrn.mongodb.net/?retryWrites=true&w=majority'

# Connect to MongoDB Atlas
client = pymongo.MongoClient(atlas_connection_string)
database = client['climate']
collection = database['temperature_data_daily']

# Retrieve date, temperature, and humidity data from the collection
documents = collection.find({}, {'time': 1, 'temp': 1, 'humidity': 1})

# Extract date, temperature, and humidity values
dates = []
temperatures = []
humidity = []
for doc in documents:
    dates.append(doc['time'])
    temperatures.append(doc['temp'])
    humidity.append(doc['humidity'])

plot_polynomial_regression(dates, temperatures, humidity, degree=2)
