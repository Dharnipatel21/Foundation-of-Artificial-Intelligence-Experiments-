#7th linear kernal
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear')
model.fit(X_train, y_train)
for i in [0, 50, 100, 75, 75]:
    pred = model.predict([X[i]])[0]
    print(f"Sample {i:>3} → Predicted: {iris.target_names[pred]:12} ")
