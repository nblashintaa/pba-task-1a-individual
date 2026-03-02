import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load data
df = pd.read_csv("data/brimo_cleaned_reviews.csv")

# Hapus data kosong
df = df.dropna(subset=["clean_review"])

# Labeling 2 kelas
def label_sentiment(rating):
    if rating >= 4:
        return "positive"
    else:
        return "negative"

df["sentiment"] = df["rating"].apply(label_sentiment)

# Fitur & target
X = df["clean_review"]
y = df["sentiment"]

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Visualisasi Confusion Matrix
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.xticks([0,1], ["negative", "positive"])
plt.yticks([0,1], ["negative", "positive"])
plt.colorbar()
plt.show()