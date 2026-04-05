# User Recommendation System

## Overview

This project implements a user recommendation system that suggests similar users based on shared interests. The system is inspired by real-world applications such as social platforms where users are matched based on preferences and behavior.

---

## Problem Statement

The objective is to recommend users who have similar interests to a given user. This helps in building connections, improving engagement, and enhancing user experience on platforms like MeetMux.

---

## Approach

The system follows a user-based collaborative filtering approach:

1. Represent each user as a feature vector of interests.
2. Compute similarity between users using cosine similarity.
3. Rank users based on similarity scores.
4. Apply additional constraints and enhancements to improve recommendations.

---

## Features

* **Cosine Similarity**
  Measures similarity between users based on their interest vectors.

* **Feature Weighting**
  Assigns higher importance to certain features (e.g., sports, tech, fitness) to reflect real-world preferences.

* **Location-Based Filtering**
  Recommends users from the same location to simulate practical constraints.

* **Hybrid Scoring**
  Combines similarity score with the number of common interests to improve recommendation quality.

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
4. Compute cosine similarity between all users.
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
* Incorporation of user behavior data (clicks, interactions)
* Use of advanced models such as embeddings or neural networks

---

## Key Learnings

* Understanding similarity metrics in machine learning
* Building recommendation systems from scratch
* Feature engineering and weighting
* Structuring a machine learning project for production readiness
