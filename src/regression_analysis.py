import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load the dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Perform linear regression
def perform_regression(data):
    # Defining the dependent variable (y) and the independent variable (X)
    y = data['Sales_Next_Day']
    X = data['Review_Rating']
    X = sm.add_constant(X)  # Adds a constant term to the predictor

    model = sm.OLS(y, X)
    results = model.fit()
    
    return results

# Visualize regression results
def plot_regression_results(data, results):
    print(results.summary())

    # Plotting regression line
    plt.scatter(x=data['Review_Rating'], y=data['Sales_Next_Day'], color='blue', alpha=0.6)
    plt.plot(data['Review_Rating'], results.predict(), color='red')
    plt.title('Regression Line of Sales against Review Ratings')
    plt.xlabel('Review Ratings')
    plt.ylabel('Sales Next Day')
    plt.show()

if __name__ == "__main__":
    data_path = "../data/reviews_sales.csv"
    df = load_data(data_path)
    
    regression_results = perform_regression(df)
    plot_regression_results(df, regression_results)

