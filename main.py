import joblib
import re

logreg = joblib.load('logreg_model.joblib')
vect = joblib.load('count_vectorizer.joblib')

def data_processing(text):
    text = text.lower()
    
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def analyze_sentiment(text):
    text_cleaned = data_processing(text)  
    text_vector = vect.transform([text_cleaned])  
    prediction = logreg.predict(text_vector)  

    return prediction[0]

if __name__ == "__main__":
    input_text = input("Enter a sentence to analyze sentiment: ")
    result = analyze_sentiment(input_text)
    print(f"The sentiment is: {result}")
