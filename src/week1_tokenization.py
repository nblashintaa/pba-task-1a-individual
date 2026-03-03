# WEEK 1 - INTRODUCTION TO NLP
# TOKENIZATION USING NLTK
# Dataset: Review Aplikasi BRImo

# Import Libraries
from google_play_scraper import reviews, Sort
import pandas as pd
import nltk
import re
import os
from nltk.tokenize import word_tokenize


# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Scrapping data review aplikasi BRImo
print("Mengambil data review BRImo...")

app_id = 'id.co.bri.brimo'

result, continuation_token = reviews(
    app_id,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=500
)

df = pd.DataFrame(result)

# Memilih kolom yang relevan dan mengganti nama kolom
df = df[['userName', 'score', 'content', 'at']]
df.columns = ['user', 'rating', 'review', 'date']

# Menyimpan row data review ke CSV
df.to_csv("data/brimo_raw_reviews.csv", index=False)

print("Scraping selesai!")
print(f"Total data: {len(df)} review")

# Prepocessing data review
print("\nMemulai preprocessing...")

# Mengahapus review yang kosong 
df = df.dropna(subset=['review'])

# Case Folding
df['clean_review'] = df['review'].str.lower()

# Menghapus whitespace berlebih
df['clean_review'] = df['clean_review'].apply(
    lambda x: re.sub(r'\s+', ' ', x).strip()
)

# Mengahapus angka & simbol
df['clean_review'] = df['clean_review'].apply(
    lambda x: re.sub(r'[^a-zA-Z\s]', '', x)
)

# Tokenization
print("\nMelakukan tokenisasi...")

df['tokens'] = df['clean_review'].apply(lambda x: word_tokenize(x))

# Menyimpan hasil tokenisasi
df.to_csv("data/brimo_tokenized_reviews.csv", index=False)

print("Tokenisasi selesai!")

# Output
print("\nContoh 5 data pertama:\n")
print(df[['review', 'clean_review', 'tokens']].head())

# Statistik dasar
all_tokens = [token for tokens in df['tokens'] for token in tokens]

print("\nStatistik Token:")
print("Total tokens:", len(all_tokens))
print("Unique tokens:", len(set(all_tokens)))