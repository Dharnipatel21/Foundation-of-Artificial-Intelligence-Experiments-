# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)
# Logistic Regression with balancing
model = LogisticRegression(class_weight='balanced')
model.fit(X, labels)
# Test Query
query = input("Enter your query: ")
query_vector = vectorizer.transform([query])
prob = model.predict_proba(query_vector)[0]
prediction = model.predict(query_vector)[0]
print("Probability (Not Relevant, Relevant):", prob)
print("Final Prediction:", prediction)
Enter your query: i like pizza
Probability (Not Relevant, Relevant): [0.5036412 0.4963588]
Final Prediction: 0
