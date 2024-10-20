# Sentiment Analysis on Vaccination Tweets

## Project Overview

This project implements a sentiment analysis system designed to evaluate the sentiment of tweets related to vaccinations. Leveraging machine learning techniques, it preprocesses the textual data, trains classification models, and makes predictions about the sentiment expressed in new tweets.

## Key Features

- **Text Preprocessing**: The project includes a robust preprocessing pipeline that cleans and prepares tweets for analysis, including steps such as converting to lowercase, removing punctuation and numbers, and eliminating extra whitespace.
  
- **Model Training**: The project utilizes popular machine learning algorithms, specifically Logistic Regression and Support Vector Classifier (SVC), to classify the sentiment of the tweets as positive or negative.

- **Model Persistence**: After training, the models are saved using Joblib, allowing for efficient loading and reuse in future analyses without the need for retraining.

- **User Interaction**: The system includes a user-friendly interface where users can input new text to analyze sentiment and receive immediate feedback on whether the sentiment is positive or negative.

## Technologies Used

- **Python**: The core programming language for implementation.
- **Scikit-learn**: For machine learning functionalities.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **NLTK**: For natural language processing tasks.
- **Joblib**: For saving and loading models.

## Conclusion

This sentiment analysis project provides valuable insights into public opinion regarding vaccinations, making it a useful tool for researchers, public health officials, and anyone interested in understanding sentiment trends on social media platforms.
