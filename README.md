<div align="center">

# 🎬 Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.1-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**An interactive Streamlit web app that delivers personalized movie recommendations using two machine learning approaches — Content-Based Filtering and Item-Based Collaborative Filtering — trained on the MovieLens 100K dataset.**

[🚀 Live Demo](#-live-demo) · [📖 How It Works](#-how-it-works) · [⚙️ Getting Started](#️-getting-started) · [🗂️ Project Structure](#️-project-structure)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [How It Works](#-how-it-works)
  - [Content-Based Filtering](#1-content-based-filtering)
  - [Item-Based Collaborative Filtering](#2-item-based-collaborative-filtering)
- [Model Performance](#-model-performance)
- [Project Structure](#️-project-structure)
- [Getting Started](#️-getting-started)
- [Usage](#-usage)
- [Tech Stack](#-tech-stack)
- [Next Steps](#-next-steps)

---

## 🌟 Overview

This project is the **deployed interactive front-end** for a movie recommendation engine built on the [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) dataset. It brings together two complementary recommendation strategies into a single Streamlit app, letting users explore personalized suggestions in real time.

> 💡 The underlying models were pre-trained, evaluated, and serialized as `.pkl` files — the app simply loads them at runtime for fast, seamless inference.

---

## 🚀 Live Demo

>  — deployed to [Streamlit Community Cloud](https://streamlit.io/cloud) for a public link._

To run the app locally, see [Getting Started](#️-getting-started) below.

---

## ✨ Features

- 🎯 **Dual recommendation modes** — switch between Content-Based and Item-Based filtering
- 🎛️ **Adjustable output** — control how many recommendations to display (1–20)
- ⚡ **Fast inference** — pre-computed similarity matrices loaded once at startup
- 🧠 **Genre-aware suggestions** — content model uses 19 genre features per movie
- 👥 **Behavior-driven suggestions** — collaborative model leverages real user rating patterns
- 📋 **Similarity & confidence scores** displayed alongside each recommendation

---

## 🤖 How It Works

### 1. Content-Based Filtering

Recommends movies that share similar **genre profiles** to a movie you already like.

**Pipeline:**
1. Each movie is represented as a **binary genre vector** across 19 genre categories
2. **Cosine similarity** is computed between all movie-genre vectors
3. Given a seed movie, the top-N most similar movies by cosine score are returned

```python
def get_content_recommendations(movie_title, n=10):
    sim_scores = cosine_sim_df.loc[movie_title].sort_values(ascending=False).iloc[1:n+1]
    return sim_scores
```

> **Best for:** New users or cold-start scenarios — no rating history required.

---

### 2. Item-Based Collaborative Filtering

Recommends movies that **users with similar tastes** have rated highly — even if the genres differ.

**Pipeline:**
1. A **User-Item rating matrix** is built (users × movies)
2. **Item-Item cosine similarity** is computed across all movie pairs based on co-rating patterns
3. For a given user, unseen movies are scored using a **similarity-weighted sum** of their existing ratings

```python
def get_item_based_recommendations(user_id, user_item_matrix, item_similarity_df, n=10):
    user_ratings = user_item_matrix.loc[user_id]
    user_ratings = user_ratings[user_ratings > 0]
    weighted_scores = item_similarity_df[user_ratings.index].dot(user_ratings)
    similarity_sums = item_similarity_df[user_ratings.index].sum(axis=1)
    predicted_scores = (weighted_scores / similarity_sums).drop(user_ratings.index, errors='ignore')
    return predicted_scores.sort_values(ascending=False).head(n)
```

> **Best for:** Users with a rating history — captures nuanced, behavior-driven preferences.

---

## 📈 Model Performance

Both models were evaluated offline on a held-out test set using **Root Mean Squared Error (RMSE)**:

| Model | RMSE | Notes |
|---|---|---|
| Content-Based Filtering | 1.0288 | Genre features only; limited expressiveness |
| **Item-Based CF** | **0.9546** ✅ | Captures real user behaviour; ~7.2% better |

> Item-Based CF outperforms Content-Based Filtering by **~7.2% RMSE reduction**.

Both models complement each other — content-based handles cold-start items; collaborative filtering excels with rich interaction data.

---

## 🗂️ Project Structure

```
Movie recommender app/
│
├── 🐍 recommender_app.py        # Streamlit app — UI + recommendation logic
├── 🧠 cosine_sim_df.pkl         # Pre-computed content-based similarity matrix
├── 🧠 item_similarity_df.pkl    # Pre-computed item-item similarity matrix
├── 🧠 user_item_matrix.pkl      # User-item interaction matrix
├── 📄 requirements.txt          # Python dependencies  
└── 📄 .gitignore.txt            # Git ignore rules
```

> **Note:** The `.pkl` files contain pre-trained artefacts serialized from the [MovieLens 100K analysis notebook](https://github.com/njorogepaul-moghul/movie-recommender). They must be present in the project root for the app to run.

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/njorogepaul-moghul/movie-recommender-app.git
cd movie-recommender-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run recommender_app.py
```

The app will open automatically at **http://localhost:8501**

---

## 🎮 Usage

| Step | Action |
|---|---|
| 1 | Choose a model: **Content-based** or **Item-based** |
| 2 | **Content-based** → Select a movie title you enjoy |
| 2 | **Item-based** → Select your User ID from the dropdown |
| 3 | Adjust the slider for how many recommendations you want |
| 4 | Click **"Get Recommendations"** and explore your results |

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Interactive web app framework |
| [pandas](https://pandas.pydata.org/) | Data manipulation & matrix operations |
| [NumPy](https://numpy.org/) | Numerical computation |
| [scikit-learn](https://scikit-learn.org/) | Cosine similarity computation |
| [pickle](https://docs.python.org/3/library/pickle.html) | Model serialization & loading |
| [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) | Training dataset |

---

## 🚀 Next Steps

- [ ] **Deploy to Streamlit Cloud** — public live demo link
- [ ] **Hybrid recommender** — blend content-based + collaborative scores
- [ ] **Matrix Factorization** — explore SVD/NMF for improved latent factor modelling
- [ ] **User-Based CF** — add user-user similarity as an alternative mode
- [ ] **Richer content features** — incorporate cast, director, and release year
- [ ] **Search & filter UI** — genre filters and search bar for movies

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ using Python · Streamlit · scikit-learn · MovieLens 100K**

</div>
