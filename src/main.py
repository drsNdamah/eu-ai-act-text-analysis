# src/main.py
from extract_text import extract_text_from_pdf
from clean_text import clean_and_lemmatize
from stopwords import get_custom_stopwords
from frequency_analysis import get_word_frequencies, save_frequency_table
from generate_wordcloud import create_wordcloud

def main():
    file_path = "data/EU_AI_ACT.pdf"
    output_csv = "output/word_frequency_output.csv"
    output_wc = "output/wordcloud.png"

    print("🔍 Extracting text...")
    raw_text = extract_text_from_pdf(file_path)

    print("🧹 Cleaning and lemmatizing text...")
    words = clean_and_lemmatize(raw_text)

    print("🛑 Applying stopwords...")
    stopwords = get_custom_stopwords()

    print("📊 Analyzing word frequencies...")
    freq = get_word_frequencies(words, stopwords)
    save_frequency_table(freq, output_csv)

    print("🌥️ Generating word cloud...")
    create_wordcloud(raw_text, stopwords, output_wc)

if __name__ == "__main__":
    main()
