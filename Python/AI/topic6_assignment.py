"""
Natural Language Processing (NLP) Assignment

This assignment is centered around the fundamentals of NLP, familiarization with NLP libraries and tools in Python,
and the construction of simple NLP applications.

Make sure to install the following Python libraries:
- nltk
- spacy

You can install them using pip:
pip install nltk spacy

Don't forget to download the necessary data packages for nltk and spacy before starting.
"""

import nltk
import spacy

# Download necessary data for nltk
try:
    # Attempt to load the model
    nlp = spacy.load("en_core_web_sm")
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')
except OSError:
    # If loading fails, download the model and then load it
    print("Downloading the 'en_core_web_sm' model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load the English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    """
    Tokenize the input text into sentences and words.

    Parameters:
    text (str): The text to be tokenized.

    Returns:
    tokens (dict): A dictionary with two keys 'sentences' and 'words', where
                   'sentences' is a list of sentence strings and 'words' is a list of word strings.
    """
    # Your code here
    try:
        sentences = nltk.sent_tokenize(text)
        
        # Divide text into a list of words
        words = nltk.word_tokenize(text)

        return {'sentences': sentences, 'words': words}
    except LookupError:
        # Download 'punkt' if it's missing
        nltk.download('punkt')
        return "Missing resources have been downloaded. Please try again."
    
    except Exception as e:
        return f"An error occurred during tokenization: {str(e)}"

def pos_tagging(text):
    """
    Perform part-of-speech (POS) tagging on the input text.

    Parameters:
    text (str): The text to be POS-tagged.

    Returns:
    tags (list): A list of tuples where the first element is the word and the second is its POS tag.
    """
    # Your code here
    try:
        return nltk.pos_tag(nltk.word_tokenize(text))
    except LookupError:
        # Download 'punkt' and 'averaged_perceptron_tagger' if they're missing
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        return "Missing resources have been downloaded. Please try again."
    
    except Exception as e:
        return f"An error occurred during POS tagging: {str(e)}"


def named_entity_recognition(text):
    """
    Identify named entities in the input text.

    Parameters:
    text (str): The text to be analyzed for named entity recognition.

    Returns:
    entities (list): A list of tuples where each tuple contains the entity and its type.
    """
    # Your code here
    try:
        if nlp is None:
            return "Spacy language model is not loaded. Please ensure 'en_core_web_sm' is installed."
        
        doc = nlp(text)
        entities = []

        for entity in doc.ents:
            # Append a tuple of text and label 
            entities.append((entity.text, entity.label_))  

        return entities
    
    except Exception as e:
        return f"An error occurred during named entity recognition: {str(e)}"   
