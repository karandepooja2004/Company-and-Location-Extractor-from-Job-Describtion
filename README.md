# Company & Location Extractor from Job Describtion

## 📌 Overview

This project demonstrates a **basic Named Entity Recognition (NER)** system using **NLTK** to extract **company names** and **locations** from a job description.

The solution relies purely on **NLTK’s built-in NER (`ne_chunk`)** without any regex or external NLP libraries, making it simple, lightweight, and suitable for **academic assignments and exam-oriented projects**.

---

## ✨ Features

* Extracts **Company / Organization names** (e.g., IBM Research Labs, OpenAI, Google)
* Extracts **Geographical locations (GPE)** such as cities and regions
* Uses **sentence tokenization, word tokenization, POS tagging, and NER chunking**
* Removes duplicate entities automatically
* Easy to understand and modify

---

## 🛠️ Technologies Used

* **Python 3.x**
* **NLTK (Natural Language Toolkit)**

---

## ⚙️ Installation & Setup

### 1️⃣ Install NLTK

```bash
pip install nltk
```

### 2️⃣ Download Required NLTK Data

The following datasets are required and downloaded in the script:

```python
nltk.download('punkt_tab')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')
```

---

## 🚀 Working of the Code

### Step 1: Sentence & Word Tokenization

The input job description is split into sentences and words using `sent_tokenize()` and `word_tokenize()`.

### Step 2: Part-of-Speech (POS) Tagging

Each token is assigned a grammatical tag using `pos_tag()`.

### Step 3: Named Entity Recognition (NER)

NLTK’s `ne_chunk()` function identifies named entities such as:

* **ORGANIZATION** → Company names
* **GPE (Geo-Political Entity)** → Locations

### Step 4: Entity Extraction

* Company names are stored when label = `ORGANIZATION`
* Locations are stored when label = `GPE`

### Step 5: Duplicate Removal

Duplicate entities are removed using Python sets.

---

## ▶️ Sample Input

```text
We are seeking a Machine Learning Engineer to join IBM Research Labs in San Francisco, California.
Applicants may also be considered for roles in Toronto and New York offices.
```

## ✅ Sample Output

```
Extracted Company Names:
['IBM Research Labs', 'OpenAI', 'Google', 'Meta Platforms Inc', 'Microsoft Azure']

Extracted Locations:
['San Francisco', 'California', 'Toronto', 'New York']
```

---

## 📊 Applications

* Job description analysis
* Resume parsing
* Recruitment & HR analytics
* Information extraction in NLP
* Academic NLP mini-projects
