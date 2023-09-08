import pandas as pd

def load_sales_data():
    """Load the sales review dataset from the specified path."""
    data_path = "../data/reviews_sales_data.csv"
    return pd.read_csv(data_path)

