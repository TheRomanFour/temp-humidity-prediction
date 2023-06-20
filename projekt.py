import pymongo
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


 # Replace <Atlas_Connection_String> with your actual connection string
atlas_connection_string = 'mongodb+srv://bruno:SIfrajedan1@apvo.jufhzrn.mongodb.net/?retryWrites=true&w=majority'

# Connect to MongoDB Atlas
client = pymongo.MongoClient(atlas_connection_string)
database = client['climate']
collection = database['temperature_data']

def plot_temperature_graph():
   

    # Retrieve all date and temperature data from the collection
    documents = collection.find({}, {'time': 1, 'temp': 1})

    # Extract date and temperature values
    dates = []
    temperatures = []
    for doc in documents:
        dates.append(doc['time'])
        temperatures.append(doc['temp'])

    # Convert dates to proper datetime format
    dates = [datetime.strptime(date, "%Y-%m-%dT%H:%M") for date in dates]

    # Create a line plot of dates and temperatures
    plt.plot(dates, temperatures)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Data')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d %H:%M"))
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_linear_regression():
     # Retrieve all date and temperature data from the collection
    documents = collection.find({}, {'time': 1, 'temp': 1})

    # Extract date and temperature values
    dates = []
    temperatures = []
    for doc in documents:
        dates.append(doc['time'])
        temperatures.append(doc['temp'])

    # Convert dates to proper datetime format
    dates = [datetime.strptime(date, "%Y-%m-%dT%H:%M") for date in dates]

    # Create a linear regression model
    model = LinearRegression()

    # Prepare the data for training
    X = [[date.timestamp()] for date in dates]
    y = temperatures

    # Train the model
    model.fit(X, y)

    # Get the coefficients and intercept of the linear regression line
    slope = model.coef_[0]
    intercept = model.intercept_

    # Create the formula string for the linear regression line
    formula = f"Temperature = {slope:.2f} * Date + {intercept:.2f}"

    # Predict the temperature for the existing dates
    predictions = model.predict(X)

    # Create a line plot of dates, temperatures, and linear regression line
    plt.plot(dates, temperatures, label='Actual')
    plt.plot(dates, predictions, label='Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Linear Regression')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    plt.grid(True)
    plt.legend()

    # Print the formula for the linear regression line
    plt.text(dates[0], min(temperatures), formula, fontsize=12)

    plt.tight_layout()
    plt.show()




def perform_polynomial_regression(connection_string):
    documents = collection.find({}, {'time': 1, 'temp': 1})
    # Extract date and temperature values
    dates = []
    temperatures = []
    for doc in documents:
        dates.append(doc['time'])
        temperatures.append(doc['temp'])

    # Convert dates to proper datetime format
    dates = [datetime.strptime(date, "%Y-%m-%dT%H:%M") for date in dates]

    # Prepare the data for training
    X = [[date.timestamp()] for date in dates]
    y = temperatures

    # Perform polynomial regression
    degree = 3  # Set the degree of the polynomial
    polynomial_features = PolynomialFeatures(degree=degree)
    X_poly = polynomial_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    # Predict the temperature for the existing dates
    predictions = model.predict(X_poly)

    # Create a line plot of dates, temperatures, and polynomial regression line
    plt.plot(dates, temperatures, label='Actual')
    plt.plot(dates, predictions, label='Polynomial Regression')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Polynomial Regression')
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Perform polynomial regression and plot the graph
perform_polynomial_regression(atlas_connection_string)


# Call the function to plot the linear regression graph
plot_linear_regression()


# Call the function to plot the temperature graph
plot_temperature_graph()
