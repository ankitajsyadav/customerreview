import streamlit as st
import pandas as pd
from textblob import TextBlob  # Simple library for sentiment analysis

# Title and Introduction
st.title("E-commerce Customer Review Analysis Tool")
st.write("Upload a CSV file containing customer reviews to analyze sentiment.")

# Sidebar for User Input
st.sidebar.header("User Input")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Function to perform sentiment analysis
def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        analysis = TextBlob(review)
        sentiments.append(analysis.sentiment.polarity)  # Get sentiment score
    return sentiments

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    if 'review' not in data.columns:
        st.error("CSV must contain a column named 'review'.")
    else:
        st.write(data.head())  # Display uploaded data

        # Perform sentiment analysis
        data['sentiment'] = analyze_sentiment(data['review'])

        # Display sentiment distribution
        sentiment_counts = pd.cut(data['sentiment'], bins=[-1, 0, 0.5, 1], labels=["Negative", "Neutral", "Positive"]).value_counts()
        
        # Bar Chart of Sentiment Distribution
        st.subheader("Sentiment Distribution")
        st.bar_chart(sentiment_counts)

        # Top improvement areas
        st.subheader("Top Improvement Areas (Sample Reviews)")
        st.write(data[['review', 'sentiment']].nlargest(5, 'sentiment'))

# Run the app
# Use the command below to run the app in the terminal
# streamlit run customer_review_analysis.py
