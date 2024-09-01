# app/utils.py
import pandas as pd
import joblib
import os

def load_data():
    preprocessed_data_path = os.path.join("data", "processed_data")
    
    # Load job postings data
    postings_df = pd.read_csv(os.path.join(preprocessed_data_path, "processed_postings.csv"))
    
    # Debugging: Print the first few rows of the DataFrame
    print("Loaded postings data:")
    print(postings_df.head())
    print("DataFrame columns:", postings_df.columns)
    
    # Load TF-IDF matrix and vectorizer
    tfidf_matrix = joblib.load(os.path.join(preprocessed_data_path, "tfidf_matrix.pkl"))
    tfidf_vectorizer = joblib.load(os.path.join(preprocessed_data_path, "tfidf_vectorizer.pkl"))
    
    # Debugging: Print the shapes of the loaded objects
    print("TF-IDF matrix shape:", tfidf_matrix.shape)
    print("TF-IDF vectorizer:", tfidf_vectorizer)
    
    return postings_df, tfidf_matrix, tfidf_vectorizer
