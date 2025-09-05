
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Initialize the analyzer
analyzer = SentimentIntensityAnalyzer()

# Your input text
text = "I hate this stupid app. Please fix it! 1 star"

# Get the sentiment scores
scores = analyzer.polarity_scores(text)

# Print the results
print("Sentiment scores:", scores)

# Optional: interpret result
compound = scores['compound']
if compound >= 0.05:
    sentiment = "Positive"
elif compound <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Overall sentiment:", sentiment)