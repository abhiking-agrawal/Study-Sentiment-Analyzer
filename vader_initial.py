from nltk.sentiment import vader
sia = vader.SentimentIntensityAnalyzer()
sia.polarity_scores("What a terrible restaurent")