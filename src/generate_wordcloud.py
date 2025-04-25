# src/generate_wordcloud.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordcloud(text, stopwords=None, output_path="output/wordcloud.png"):
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=200,
        stopwords=stopwords,
        colormap='viridis'
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud from PDF Document")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
