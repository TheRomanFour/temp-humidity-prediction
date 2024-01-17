# Temperature Analysis with MongoDB and Regression Models
Made as a UNI Project
This script connects to a MongoDB Atlas database containing temperature data and performs linear and polynomial regression analysis. It visualizes the data using matplotlib.

## Prerequisites

- Python 3.x
- pymongo
- matplotlib
- scikit-learn

## Usage

1. Run the script:

    ```bash
    python temperature_analysis.py
    ```

2. View the generated graphs:
    - Temperature vs. Date
    - Linear Regression
    - Polynomial Regression

## Functionality

### 1. Temperature vs. Date

- Retrieves temperature data from the MongoDB Atlas collection.
- Plots a line graph of temperature against date.

### 2. Linear Regression

- Retrieves temperature data from the MongoDB Atlas collection.
- Performs linear regression analysis.
- Plots the actual temperatures and the linear regression line.

### 3. Polynomial Regression

- Retrieves temperature data from the MongoDB Atlas collection.
- Performs polynomial regression analysis (adjustable degree).
- Plots the actual temperatures and the polynomial regression line.

## Customization

- Modify the `atlas_connection_string` variable with your actual MongoDB Atlas connection string.
- Adjust the degree of the polynomial in the `degree` variable for polynomial regression.

