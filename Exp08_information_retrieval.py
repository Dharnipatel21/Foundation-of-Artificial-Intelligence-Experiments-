#8 information retrival
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
# Better training dataset
documents = [
    "Artificial intelligence improves healthcare",
    "Machine learning algorithms in finance",
    "AI used in robotics and automation",
    "Deep learning for image recognition",
    "Neural networks in data science",
    "Football match results and sports news",
    "Cooking recipes and kitchen tips",
    "Travel guide for Europe",
    "Latest movie reviews",
    "Music album release updates"
]
labels = [1,1,1,1,1, 0,0,0,0,0]
