import pandas as pd
import re
import os

print("Memulai preprocessing data...")

# Load dataset
df = pd.read_csv("data/brimo_raw_reviews.csv")

# Menghapus review yang kosong
df = df.dropna(subset=['review'])

# Case Folding
df['clean_review'] = df['review'].str.lower()

# Menghapus angka dan simbol
df['clean_review'] = df['clean_review'].apply(
    lambda x: re.sub(r'[^a-zA-Z\s]', '', x)
)

# Tokenisasi
df['tokens'] = df['clean_review'].apply(lambda x: x.split())

# Menyimpan hasil preprocessing ke folder data
df.to_csv("data/brimo_tokenized_reviews.csv", index=False)

print("Preprocessing selesai sampai tokenisasi!")
print("\nContoh hasil tokenisasi:\n")
print(df[['review', 'clean_review', 'tokens']].head())