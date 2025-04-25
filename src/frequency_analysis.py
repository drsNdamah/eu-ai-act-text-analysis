# src/frequency_analysis.py
from collections import Counter
import pandas as pd

def get_word_frequencies(words, stopwords=None):
    word_freq = Counter(words)
    if stopwords:
        word_freq = {word: count for word, count in word_freq.items() if word not in stopwords}
    return word_freq

def save_frequency_table(freq_dict, output_path="output/word_frequency_output.csv"):
    df = pd.DataFrame(freq_dict.items(), columns=["Word", "Frequency"])
    df = df.sort_values(by="Frequency", ascending=False)
    df.to_csv(output_path, index=False)
    print(f"Word frequency output saved to {output_path}")
