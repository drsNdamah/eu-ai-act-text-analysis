# eu-ai-act-text-analysis
Text mining and NLP analysis of the EU AI Act


```markdown
# 🧠 EU AI Act Text Analysis

This project explores the **language of the EU Artificial Intelligence Act** using Natural Language Processing (NLP). By processing the official text, we extract the most frequent and meaningful terms to highlight the Act’s regulatory priorities — such as risk, compliance, and transparency.

This analysis helps policymakers, researchers, and legal tech professionals better understand how the legislation is framed and what themes are emphasized.

---

## 📁 Project Structure

```
eu-ai-act-text-analysis/
│
├── README.md             # Project overview (this file)
├── requirements.txt      # Python dependencies
├── data/                 
│   └── eu_ai_act.pdf     # Source text (or sample placeholder)
├── notebooks/            
│   ├── 01_text_extraction_cleaning.ipynb
│   └── 02_frequency_analysis.ipynb
├── src/                  
│   ├── extract_text.py
│   ├── clean_text.py
│   └── frequency_analysis.py
├── output/               
│   ├── frequency_table.csv
│   └── wordcloud.png
├── images/               
│   └── table_visual.png  # Visual summary for LinkedIn or presentation
└── LICENSE
```

---

## 🔧 Features

- 📄 Extracts text from PDF using `PyMuPDF`
- 🧹 Cleans and lemmatizes using `spaCy`
- 🛑 Removes both generic and domain-specific stopwords
- 📊 Counts word frequencies and exports them as CSV
- 🌥️ Generates a word cloud
- 📷 Includes a table-style image for sharing insights

---

## 📝 Sample Output: Top Words

**Top 10 Words in the EU AI Act:**

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

> View the table image: [`images/table_visual.png`](images/table_visual.png)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/eu-ai-act-text-analysis.git
cd eu-ai-act-text-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Or, if using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🧪 Run the Code

- Run the Jupyter Notebooks in the `notebooks/` folder for step-by-step execution
- Or execute Python scripts in `src/` for modular use:
  ```bash
  python src/extract_text.py
  python src/clean_text.py
  python src/frequency_analysis.py
  ```

Make sure `data/eu_ai_act.pdf` exists before running.

---

## 🛠 Requirements

Your `requirements.txt` includes:

```
spacy
pymupdf
pandas
matplotlib
wordcloud
```

Run:
```bash
pip install -r requirements.txt
```

And download the spaCy model if not already installed:

```bash
python -m spacy download en_core_web_sm
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests and feedback are welcome! Whether you want to extend the analysis, improve visuals, or explore other legislation — let's collaborate.

---

## 📬 Contact

Built with ❤️ by [drsNdamah]  
🔗 [LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/kweku-ndamah-arthur-34b9811aa/))

---

```

Would you like me to generate the `requirements.txt` content based on your project as well?
