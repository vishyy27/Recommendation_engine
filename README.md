# User Recommendation System

## Overview

This project implements a user recommendation system that suggests similar users based on shared interests. The system demonstrates how similarity-based algorithms can be used to build personalized recommendations.

---

## Problem Statement

The objective is to recommend users who have similar interests to a given user. Such systems are widely used in platforms to improve user engagement and personalization.

---

## Approach

The system uses a user-based collaborative filtering approach:

1. Represent each user as a feature vector of interests.
2. Compute similarity between users using cosine similarity.
3. Rank users based on similarity scores.
4. Apply additional constraints to refine recommendations.

---

## Features

* **Cosine Similarity**
  Measures similarity between users based on their interest vectors.

* **Feature Weighting**
  Assigns higher importance to selected features (e.g., sports, tech, fitness).

* **Location-Based Filtering**
  Recommends users from the same location.

* **Hybrid Scoring**
  Combines similarity score with the number of common interests.

* **Edge Case Handling**
  Handles invalid user inputs gracefully.

---

## Tech Stack

* Python
* Pandas
* Scikit-learn

---

## Project Structure

```
Recommendation_engine/
│
├── data/
│   └── users.csv
│
├── notebook/
│   └── model.ipynb
│
├── src/
│   └── recommend.py
│
├── README.md
├── .gitignore
```

---

## How It Works

1. Load user data from a CSV file.
2. Preprocess the data by removing non-numeric columns.
3. Apply feature weighting.
4. Compute cosine similarity between users.
5. For a given user:

   * Filter users based on location.
   * Calculate hybrid scores.
   * Return top N recommended users.

---

## Example

Input:

```
recommend(1)
```

Output:

```
[6, 3, 8, 10]
```

---

## Future Improvements

* Integration with real-world datasets
* Conversion into a REST API using FastAPI
* Deployment as a web service
* Incorporation of behavioral data (user activity, interactions)
* Use of advanced techniques such as embeddings

---

## Key Learnings

* Understanding similarity-based recommendation systems
* Implementing cosine similarity from scratch
* Feature engineering and weighting techniques
* Structuring machine learning projects for scalability
