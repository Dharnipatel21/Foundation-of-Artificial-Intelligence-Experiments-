#12 KNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Algorithm: Find K nearest neighbors, classify by majority vote
# Use Case: Student performance prediction (pass/fail)
# Dataset
data = pd.DataFrame({
'study_hours': [2, 4, 1, 3, 5, 6, 1, 4, 3, 7],
'attendance': [60, 75, 50, 80, 90, 95, 55, 85, 70, 88],
'previous_marks': [50, 65, 45, 70, 85, 90, 58, 78, 57, 92],
'result': [0, 1, 0, 1, 1, 1, 0, 1, 0, 1]  # 0=Fail, 1=Pass
})
X = data[['study_hours', 'attendance', 'previous_marks']]
y = data['result']
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Predictions:", y_pred)
print("Actual:", y_test.values)
