# ============================================================
# Final Company & Location Extractor using NLTK + Regex Context
# ============================================================

import re
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

# Download necessary NLTK data files (run once)
nltk.download('punkt_tab')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')

# Sample job description
text = "We are seeking a Machine Learning Engineer to join IBM Research Labs in San Francisco, California. The role involves collaborating with teams at OpenAI and Microsoft Azure on next-generation AI systems. Candidates should have experience with Python, TensorFlow, and cloud computing. Applicants may also be considered for roles in Toronto and New York offices. Preference will be given to those with prior experience at Google or Meta Platforms Inc."

# Step 1: Tokenize and POS tag
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

# Step 2: Named Entity Recognition (Chunking)
named_entities = ne_chunk(pos_tags, binary=False)

companies = set()
locations = set()

# --- Pass 1: Extract using NLTK Named Entities ---
for subtree in named_entities:
    if isinstance(subtree, Tree):
        label = subtree.label()
        entity = " ".join([token for token, pos in subtree.leaves()])

        if label == "ORGANIZATION":
            companies.add(entity)
        elif label == "GPE":
            locations.add(entity)

# --- Pass 2: Regex + Context Heuristics (to catch missed companies) ---
# Common patterns like "at Amazon", "join Google", "for Microsoft", etc.
context_pattern = re.compile(
    r'\b(?:at|join|joining|with|for|from|hiring|in)\s+([A-Z][A-Za-z0-9&.\-]*(?:\s[A-Z][A-Za-z0-9&.\-]*)*)'
)

matches = context_pattern.findall(text)
for match in matches:
    # Filter out false positives (skills, titles)
    if match.lower() in ["sql", "python", "developer", "engineer", "intern"]:
        continue
    companies.add(match.strip())

# --- Optional: Company suffix detection (Pvt Ltd, Inc, Corp etc.) ---
suffix_pattern = re.compile(r'\b([A-Z][A-Za-z0-9&.\-]*(?:\s[A-Z][A-Za-z0-9&.\-]*)*\s(?:Inc\.?|Ltd\.?|LLC|Corp\.?|Pvt\.?|PLC))\b')
suffix_matches = suffix_pattern.findall(text)
for match in suffix_matches:
    companies.add(match.strip())

# Convert sets to sorted lists
companies = sorted(companies)
locations = sorted(locations)

# Step 4: Display Results
print("🧩 Extracted Company Names:")
print(companies)
print("\n📍 Extracted Locations:")
print(locations)
