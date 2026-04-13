# Exp 9 - Feature Extraction from News Text using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
FAI observation - Colab
news = [
"Government announces new economic policy to boost growth",
"Stock market crashes amid global financial crisis",
"Scientists discover breakthrough in cancer treatment",
"Earthquake devastates coastal city thousands displaced",
"Tech giant launches revolutionary AI powered smartphone",
"Flood warnings issued as heavy rainfall continues",
"Prime Minister signs historic peace agreement with neighbors",
"Unemployment rate drops to lowest level in decade"
]
labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Positive News, 0 = Negative News
tfidf = TfidfVectorizer(max_features=1000)
X = tfidf.fit_transform(news)
model = LogisticRegression()
model.fit(X, labels)
# 
✅
 Multiple News Inputs
new_articles = [
"President unveils major infrastructure development plan",
"Hurricane causes widespread destruction across the region",
"Researchers develop new vaccine against deadly virus",
"Violent protests erupt in capital city over elections",
"modi just announce the war"
]
print("=" * 55)
print("      
�
�
NEWS SENTIMENT CLASSIFICATION RESULT")
print("=" * 55)
for article in new_articles:
X_new = tfidf.transform([article])
pred = model.predict(X_new)[0]
label = " Positive News" if pred == 1 else " Negative News"
print(f"\n {article}\n   → {label}")
print("=" * 55)
