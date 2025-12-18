#import required libraries
import nltk
from nltk import sent_tokenize, word_tokenize, ne_chunk, pos_tag
from nltk.tree import Tree

# download necessary NLTK data files
nltk.download('punkt_tab')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')

# Sample job description
text = """We are seeking a Machine Learning Engineer to join IBM Research Labs in San Francisco, California.
The role involves collaborating with teams at OpenAI and Microsoft Azure on next-generation AI systems.
Candidates should have experience with Python, TensorFlow, and cloud computing.
Applicants may also be considered for roles in Toronto and New York offices.
Preference will be given to those with prior experience at Google or Meta Platforms Inc."""

#Tokenize and POS tag
sentences = sent_tokenize(text)
tokens = [word for sentence in sentences for word in word_tokenize(sentence)]
pos_tags = pos_tag(tokens)

# Apply NER
named_entities = ne_chunk(pos_tags, binary=False)

# Extract companies and locations
companies = []
locations = []

for subtree in named_entities:
    if isinstance(subtree, Tree):
        label = subtree.label()
        entity = " ".join([token for token, pos in subtree.leaves()])

        if label == "ORGANIZATION":
            companies.append(entity)
        elif label == "GPE":
            locations.append(entity)

# Remove duplicates
companies = list(set(companies))
locations = list(set(locations))

# Step 4: Display Results
print("Extracted Company Names:")
print(companies)
print("\nExtracted Locations:")
print(locations)
