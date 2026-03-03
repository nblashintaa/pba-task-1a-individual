PBA-TASK-1A-INDIVIDUAL
│
├── data/
│   ├── brimo_raw_reviews.csv
│   └── brimo_tokenized_reviews.csv
│
├── src/
│   └── week1_tokenization.py
│
├── requirements.txt
├── README.md
└── .gitignore
## Deskripsi Aplikasi

BRImo (BRI Mobile) adalah aplikasi mobile banking resmi dari Bank Rakyat Indonesia (BRI).  
Aplikasi ini memungkinkan pengguna untuk melakukan berbagai transaksi keuangan secara digital, seperti:

- Transfer antar bank
- Pembayaran tagihan
- Top up e-wallet
- Pembelian pulsa
- Cek saldo & mutasi rekening
- Pembukaan rekening online

Sebagai salah satu aplikasi perbankan terbesar di Indonesia, BRImo memiliki jutaan pengguna aktif dan ribuan ulasan di Google Play Store.  
Review pengguna ini dapat dianalisis menggunakan Natural Language Processing (NLP) untuk memahami opini dan pengalaman pengguna terhadap aplikasi.


## Dataset

Dataset yang digunakan adalah review pengguna aplikasi BRImo yang diambil langsung dari Google Play Store menggunakan library:

- `google-play-scraper`

Jumlah data yang diambil: **500 review terbaru**


## Tahapan Pengerjaan

### Data Collection (Scraping)

Mengambil 500 review terbaru dari aplikasi BRImo menggunakan `google_play_scraper`.

Data yang diambil meliputi:
- Username
- Rating
- Review
- Tanggal review

---

### Text Preprocessing

Tahapan preprocessing yang dilakukan:

- Case folding (mengubah teks menjadi huruf kecil)
- Menghapus angka
- Menghapus tanda baca dan simbol
- Menghapus spasi berlebih

Tujuan preprocessing adalah membersihkan teks agar siap dianalisis dalam tahap NLP berikutnya.


### Tokenization

Tokenisasi dilakukan menggunakan:

```python
nltk.tokenize.word_tokenize()