from google_play_scraper import reviews, Sort
import pandas as pd
import os

print("Sedang mengambil data review BRImo...")


app_id = 'id.co.bri.brimo'

result, continuation_token = reviews(
    app_id,
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=500   # Mengambil 500 review terbaru
)

df = pd.DataFrame(result)

# Mengambil kolom yang diperlukan
df = df[['userName', 'score', 'content', 'at']]
df.columns = ['user', 'rating', 'review', 'date']

# Menyimpan ke folder data
df.to_csv('data/brimo_raw_reviews.csv', index=False)

print("Scraping selesai!")
print(f"Total data: {len(df)} review")