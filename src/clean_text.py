# src/clean_text.py
import spacy

# Load spaCy model globally
nlp = spacy.load("en_core_web_sm")

def clean_and_lemmatize(text):
    spacy_doc = nlp(text)
    lemmatized_words = [
        token.lemma_.lower()
        for token in spacy_doc
        if token.is_alpha and not token.is_stop
    ]
    return lemmatized_words


