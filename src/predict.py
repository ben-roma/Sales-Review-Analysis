from model import train_model
from load_data import load_sales_data

def predict_sales(model, review_rating):
    """Predict sales based on the provided review rating using the trained model."""
    return model.predict([[review_rating]])

if __name__ == "__main__":
    data = load_sales_data()
    model, _, _ = train_model(data)

    new_review = 4.5
    predicted_sales = predict_sales(model, new_review)

    print(f"Predicted sales for a review rating of {new_review}: {predicted_sales[0]}")

