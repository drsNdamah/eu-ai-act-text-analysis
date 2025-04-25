import fitz  # PyMuPDF
import spacy
from wordcloud import STOPWORDS, WordCloud
from collections import Counter
import pandas as pd
import os
import matplotlib.pyplot as plt

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Set your PDF file path (inside input folder)
file_path = "data/EU_AI_ACT.pdf"

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# Read text from PDF
doc = fitz.open(file_path)
document = ""
for page in doc:
    document += page.get_text()

# Apply spaCy processing to the text (tokenization, lemmatization)
spacy_doc = nlp(document)

# Lemmatize the words and filter out stopwords and non-alphabetic tokens
lemmatized_words = [token.lemma_.lower() for token in spacy_doc if token.is_alpha and not token.is_stop]

# Create a Counter to count word frequencies
word_freq = Counter(lemmatized_words)

# === Custom Stop Words ===
custom_stopwords = set(STOPWORDS)  # Load default stop words from WordCloud
additional_stopwords = {
    "abovementione", "include", "refer", "overview", "verifie", "signature", "alternatively", "taxonomy", "perspective",
    "established", "server", "theft", "leakage", "accidental", "unknown", "unsuitability", "tcn", "ecris",
    "conviction", "reform", "series", "en", "candidate", "duplicate", "incoming", "chatbot",
    "railway", "metro", "bus", "stadium", "gym", "swimming", "hospitality", "cafés", "restaurant", "shop",
    "sequence", "token", "criteria", "brief", "flag", "fourth", "smart", "layer", "neutral",
    "normally", "encouraged", "contemplate", "certifier", "directives", "eea", "scanned", "optional",
    "rape", "organised", "armed", "robbery", "sabotage", "biometrics", "steer",
    "tissue", "organ", "injury", "bodily", "head", "arm", "smile", "frown", "apparent", "issuing", "outlier",
    "clean", "supervised", "datasheet", "layout", "show", "illustration", "photograph", "package", "firmware",
    "radioactive", "grievous", "murder", "munition", "strong", "adjust", "continuously", "difficult", "valuable",
    "compute", "upfront", "planning", "commonly", "barriers", "mind", "evolution", "quick",
    "observance", "mitigating", "window", "teaming", "red", "interpreting", "irregular", "ship", "seizure",
    "hostage", "restraint", "kidnapping", "psychotropic", "drug", "pornography", "terrorism", "proceed",
    "required", "archive", "holder", "underpin", "want", "misinformation", "hard", "preference", "maximise",
    "correspond", "keyword", "guardrail", "combined", "false", "discourage",
    "audits", "asse", "upgrade", "marked", "cancel", "preliminary", "negligently", "intentionally",
    "complainant", "character", "delegated", "message", "mere", "driver", "pilot", "watermark", "trace",
    "manipulation", "pain", "amusement", "satisfaction", "contempt", "shame", "excitement", "embarrassment",
    "disgust", "surprise", "anger", "unmanned", "propeller", "negligent", "aggravating",
    "percentage", "reply", "viability", "revocation", "whispering", "sadness", "happiness",
    "television", "domain", "city", "circulation", "divergence", "import", "cryptographic", "metadata",
    "diverge", "circulate", "obstacle", "watercraft", "michel", "metsola", "brussels", "twentieth", "inclusion",
    "exclusive", "handle", "formal", "prescribed", "misclassifie", "disagreement", "forward", "undisclosed",
    "multilateral", "bilateral", "clearance", "close", "insight", "doctor", "chemical", "predictor",
    "primarily", "generating", "regions", "conclusions", "mix", "terminal", "storing", "participative",
    "oppose", "tacitly", "encouraging", "similarity"

}
custom_stopwords.update(additional_stopwords)  # Add custom stop words to the set

# Remove stopwords from the word frequencies
filtered_words = {word: count for word, count in word_freq.items() if word not in custom_stopwords}

# Convert the filtered word frequencies into a pandas DataFrame
word_freq_table = pd.DataFrame(filtered_words.items(), columns=['Word', 'Frequency'])

# Sort the table by frequency in descending order
word_freq_table = word_freq_table.sort_values(by='Frequency', ascending=False)

#print(word_freq_table.head(30))


# Save the word frequency table as a CSV file
output_file_path = "word_frequency_output.csv"
word_freq_table.to_csv(output_file_path, index=False)

print(f"Word frequency output saved to {output_file_path}")



# === Create Word Cloud ===
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    max_words=200,
    stopwords=custom_stopwords,  # Exclude stopwords
    colormap='viridis'
).generate(document)

# Display Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Hide axes
plt.title("Word Cloud from PDF Document")
plt.show()