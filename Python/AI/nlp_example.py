from textblob import TextBlob
import nltk
nltk.download('brown')

text = "This is my example of NLP using Python. I wanted a bit of a long sentence so I am just kind of making up stuff."

blob = TextBlob(text)

# Display the words
print("Words:", blob.words)

# Display the tags
print("POS Tags:", blob.tags)

# Sentiment Analysis
sentiment = blob.sentiment
print("Sentiment Polarity:", sentiment.polarity)
print("Sentiment Subjectivity:", sentiment.subjectivity)

# Show only nouns
print("Noun Phrases:", blob.noun_phrases)

