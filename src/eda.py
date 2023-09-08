import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Visualize the distribution of review ratings
def plot_review_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='Review_Rating', palette="viridis")
    plt.title("Distribution of Review Ratings")
    plt.xlabel("Review Rating")
    plt.ylabel("Count")
    plt.show()

# Visualize the relationship between review ratings and sales the next day
def plot_sales_vs_reviews(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Review_Rating', y='Sales_Next_Day', color="purple", s=100, alpha=0.6)
    sns.lineplot(data=data, x='Review_Rating', y='Sales_Next_Day', color="blue")
    plt.title("Relationship between Review Ratings and Sales Next Day")
    plt.xlabel("Review Rating")
    plt.ylabel("Sales Next Day")
    plt.show()

if __name__ == "__main__":
    data_path = "../data/reviews_sales_data.csv"
    data = load_data(data_path)

    plot_review_distribution(data)
    plot_sales_vs_reviews(data)

