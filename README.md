# Impact of Customer Reviews on Sales

An analysis exploring the influence of customer reviews on subsequent product sales.

## Dataset

### Review_ID
 A unique identifier for each review.
### Date
The date the review was posted.
### Review_Rating
A rating score from 1 to 5.
### Sales_Next_Day
Sales of the product on the day following the review.
### Review_Text
Brief text feedback on the product.

The dataset used in this project is simulated but follows realistic distributions based on observed real-world behavior. You can find the dataset in the data/ directory under the name reviews_sales.csv.

## Analysis Overview

1. Exploratory Data Analysis (EDA):

Distribution of review ratings.
Relationship between review ratings and sales the next day.

2. Statistical Analysis:

Linear regression modeling to quantify the relationship between reviews and sales.
Visualization
Various visualizations have been utilized throughout the analysis process to better understand the data and the patterns within. These include histograms, scatter plots, and regression line plots.

## Requirements
To reproduce the analysis, the following Python libraries are needed:

pandas
numpy
seaborn
matplotlib
scikit-learn

You can install these using the provided requirements.txt file.

## Usage
To replicate the analysis, follow these steps:

1. Clone this repository.
2. Install the necessary Python libraries.
3. Run the scripts or Jupyter notebooks present in the src/ or notebooks/ directory.
