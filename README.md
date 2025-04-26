
# 🧠 EU AI Act Text Analysis

A Natural Language Processing (NLP) project that analyzes the text of the European Union Artificial Intelligence Act. The goal is to highlight key themes, regulatory focus areas, and term frequencies through text cleaning, lemmatization, and visualization.

#
## 📊 What This Project Does

- ✅ Extracts raw text from the official EU AI Act PDF
- 🧼 Cleans and lemmatizes the text using `spaCy`
- 🧱 Removes common and domain-specific stopwords
- 📈 Performs word frequency analysis
- 🌥️ Generates a word cloud
- 📸 Produces visualizations for reports or LinkedIn

---

## 🗂️ Project Structure

```
eu-ai-act-text-analysis/
│
├── README.md               # Project overview
├── requirements.txt        # Python dependencies
├── data/                   
│   └── eu_ai_act.pdf       # Source PDF of the AI Act
├── src/                    # Modular Python code
│   ├── extract_text.py     # PDF text extraction
│   ├── clean_text.py       # Lemmatization & stopword removal
│   ├── frequency_analysis.py # Frequency counts
│   ├── generate_wordcloud.py # Word cloud generation
│   └── main.py             # Orchestrates all steps
├── output/                 
│   ├── frequency_table.csv # Word frequencies
│   └── wordcloud.png       # Generated word cloud
├── images/
│   └── table_visual.png    # Visual summary for sharing
└── LICENSE
```

---

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/drsNdamah/eu-ai-act-text-analysis.git
cd eu-ai-act-text-analysis
```

### 2. Set up your environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Add your input
Place the `eu_ai_act.pdf` file inside the `data/` folder.

### 5. Run the project
```bash
python src/main.py
```

---

## 📈 Sample Output: Top Terms

| 🔠 Word      | 🔢 Frequency | 💬 Interpretation                                |
|-------------|--------------|--------------------------------------------------|
| ai          | 1667         | Central focus — clearly the core topic.         |
| system      | 1478         | Regulation targets AI systems.                  |
| risk        | 776          | Emphasis on high-risk categorization.           |
| regulation  | 729          | Legal and compliance-heavy nature.              |
| high        | 527          | Often in "high-risk" context.                   |
| authority   | 521          | Role of regulatory bodies.                      |
| provider    | 516          | Focus on developers and suppliers.              |
| market      | 403          | Attention to the internal EU market.            |
| model       | 366          | Regulation of the underlying model.             |
| person      | 348          | Individual rights and impact.                   |
#



## ⚙️ Requirements

- `spacy`
- `pymupdf`
- `pandas`
- `matplotlib`
- `wordcloud`

Install with:
```bash
pip install -r requirements.txt
```

---

## 📁 Output

- `output/frequency_table.csv`: CSV file with word frequencies
- `output/wordcloud.png`: Word cloud image of filtered terms
- `images/table_visual.png`: Clean visualization for sharing

---

## 📜 License

MIT License. See the [LICENSE](LICENSE) file for full details.

---

## 🤝 Contributing

Pull requests, ideas, and forks are welcome! You can improve visuals, expand the analysis to other legislation, or add interactive dashboards.

---

## 👤 Author

Built with ❤️ by [drsNdamah]  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/kweku-ndamah-arthur-34b9811aa/)

---
```

Would you like this saved as a file or pushed to your GitHub repo in a PR format?
