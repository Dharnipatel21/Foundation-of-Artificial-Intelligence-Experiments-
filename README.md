# Foundation-of-Artificial-Intelligence-Experiments-
FAI lab observations: AI algorithms &amp; ML models in Python - search, optimization, game AI, classification, and clustering


# 🤖 Foundations of Artificial Intelligence (FAI) — Lab Observations

A collection of Python programs implementing core AI algorithms and machine learning techniques, developed as part of the FAI lab course.

---

## 📋 Table of Contents

| # | Experiment | Technique |
|---|-----------|-----------|
| 1 | [Knapsack Problem](#1-knapsack-problem) | Greedy Algorithm |
| 2 | [Travelling Salesman (SA)](#2-travelling-salesman---simulated-annealing) | Local Search / Simulated Annealing |
| 3 | [Peak Element Finder](#3-peak-element-finder) | Binary Search |
| 4 | [Alpha-Beta Pruning](#4-alpha-beta-pruning) | Game Tree Search |
| 5 | [Shortest Path in Grid](#5-shortest-path-in-a-matrix) | BFS |
| 6 | [Tic-Tac-Toe AI](#6-tic-tac-toe-ai) | Minimax Algorithm |
| 7 | [SVM Classifier](#7-svm-with-linear-kernel) | Support Vector Machine |
| 8 | [Information Retrieval](#8-information-retrieval) | TF-IDF + Logistic Regression |
| 9 | [News Sentiment Classification](#9-news-sentiment-classification) | TF-IDF + Logistic Regression |
| 10 | [Educational Speech Recognition](#10-educational-speech-recognition) | NLP + gTTS |
| 11 | [Customer Segmentation](#11-k-means-clustering) | K-Means Clustering |
| 12 | [Student Performance Prediction](#12-k-nearest-neighbors-knn) | KNN Classifier |
| 13 | [TSP - Nearest Neighbor](#13-travelling-salesman---nearest-neighbor) | Greedy Heuristic |
| 14 | [Graph Traversal](#14-bfs--dfs) | BFS & DFS |
| 15 | [Price Optimization](#15-hill-climbing) | Hill Climbing |

---

## 🧪 Experiments

### 1. Knapsack Problem
Implements a **greedy approach** to the 0/1 knapsack problem. Given item weights and values with a capacity constraint, it selects items to maximize total value.

**Sample Output:**
```
7
```

---

### 2. Travelling Salesman - Simulated Annealing
Uses **Simulated Annealing** (a local search technique) to find a near-optimal route across a set of world cities using the Haversine distance formula.

**Cities supported:** New York, London, Dubai, Tokyo, Sydney, Paris, Singapore, Mumbai, Chennai, Berlin, Toronto, Beijing

**Sample Output:**
```
Initial Distance : X,XXX.XX km
Optimized Distance: X,XXX.XX km
Saved : XXX.XX km
```

---

### 3. Peak Element Finder
Finds a **peak element** in an array using binary search (O(log n)). Also computes its complex square root using Python's `cmath`.

**Sample Output:**
```
16 (4+0j)
```

---

### 4. Alpha-Beta Pruning
Implements the **Alpha-Beta Pruning** optimization for minimax game tree search, reducing the number of nodes evaluated.

**Sample Output:**
```
Optimal Value: 15
```

---

### 5. Shortest Path in a Matrix
Finds the **shortest path** between two points in a grid (with obstacles) using **Breadth-First Search (BFS)**.

**Sample Output:**
```
(4, [(0,0), (0,1), (0,2), (1,2), (2,2)])
```

---

### 6. Tic-Tac-Toe AI
An AI agent that plays Tic-Tac-Toe optimally using the **Minimax algorithm**. Returns the best possible move for the current board state.

**Sample Output:**
```
(1, 1)
```

---

### 7. SVM with Linear Kernel
Trains a **Support Vector Machine** with a linear kernel on the Iris dataset to classify flower species.

**Sample Output:**
```
Sample   0 → Predicted: setosa
Sample  50 → Predicted: versicolor
Sample 100 → Predicted: virginica
```

---

### 8. Information Retrieval
Uses **TF-IDF vectorization** and **Logistic Regression** to classify whether a query is relevant to AI/tech documents.

**Sample Output:**
```
Enter your query: i like pizza
Final Prediction: 0  (Not Relevant)
```

---

### 9. News Sentiment Classification
Classifies news headlines as **Positive** or **Negative** using TF-IDF features and Logistic Regression.

**Sample Output:**
```
Researchers develop new vaccine against deadly virus
 → Positive News

Hurricane causes widespread destruction across the region
 → Negative News
```

---

### 10. Educational Speech Recognition
Simulates a speech-to-text pipeline for an educational context. Extracts structured data (student name, study hours, subject) from a sentence using **regex**, and optionally generates an audio confirmation using **gTTS**.

**Sample Output:**
```
Structured Record: {'Student': 'dharni', 'Study_Hours': '1', 'Subject': 'english'}
Confirmation: Great work! 1 hours of english study logged for dharni.
```

---

### 11. K-Means Clustering
Segments customers into **5 clusters** based on Age, Annual Income, and Spending Score using **K-Means**, with a scatter plot visualization.

**Sample Output:**

| Age | Annual_Income | Spending_Score | Cluster |
|-----|--------------|----------------|---------|
| 25  | 40000        | 60             | 4       |
| 34  | 60000        | 65             | 2       |

---

### 12. K-Nearest Neighbors (KNN)
Predicts student **pass/fail** based on study hours, attendance, and previous marks using a **KNN classifier** (k=3).

**Sample Output:**
```
Accuracy: 1.0
Predictions: [0 1 1]
Actual:      [0 1 1]
```

---

### 13. Travelling Salesman - Nearest Neighbor
Solves a small TSP instance using the **Nearest Neighbor greedy heuristic** on a 4-city distance matrix.

**Sample Output:**
```
Optimized Route: [0, 1, 2, 3, 0]
Total Distance: 20
```

---

### 14. BFS & DFS
Implements both **Breadth-First Search** and **Depth-First Search** for pathfinding in a social network graph.

**Sample Output:**
```
BFS: ['A', 'C', 'F']
DFS: ['A', 'B', 'E', 'F']
```

---

### 15. Hill Climbing
Uses the **Hill Climbing** optimization technique to find the price point that maximizes profit, modeled as a parabolic function.

**Sample Output:**
```
Start: $36 → Optimal: $50, Profit: $2500
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Environment:** Google Colab
- **Libraries:** `scikit-learn`, `numpy`, `pandas`, `matplotlib`, `gTTS`, `collections`, `math`, `cmath`, `re`, `random`

---

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/FAI-observations.git
   ```

2. Open any `.ipynb` notebook in [Google Colab](https://colab.research.google.com/) or run locally with Jupyter.

3. Install dependencies if running locally:
   ```bash
   pip install scikit-learn numpy pandas matplotlib gtts
   ```
> *All experiments were implemented and tested on Google Colab as part of the FAI lab course.*
