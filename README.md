# 🎬 Movie Recommender App

An interactive **Streamlit web app** that allows users to explore and receive personalized movie recommendations.  
The app supports **two recommendation engines** — **Content-Based Filtering** and **Item-Based Collaborative Filtering** — giving users the freedom to choose their preferred model.

---

## 🌐 Live Demo

👉 **Try it here:** [Movie Recommender Streamlit App](https://movie-recommender-app-rnsbnbtaaawhqkjhzldybs.streamlit.app/)



---

## 🚀 Features

- 🎥 **Select a Model:** Choose between *Content-Based* or *Item-Based* recommendation systems.  
- 🔍 **Search & Recommend:** Enter or select a movie title to get top similar recommendations.  
- 📊 **Interactive Results:** Instantly view similar movies ranked by similarity score.  
- ⚡ **Fast & Lightweight:** Powered by pre-computed cosine similarity matrices.  

---

## 🧠 Models Overview

### 🟦 Content-Based Filtering
Recommends movies based on their **genre similarity** — using cosine similarity between genre vectors.

### 🟩 Item-Based Collaborative Filtering
Recommends movies based on **user rating patterns**, finding items similar to what users with similar tastes enjoyed.

---

## 🧰 Tech Stack

- **Python 3.12+**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Pickle** (for saving trained similarity matrices)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommender-app.git
cd movie-recommender-app
2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

3. Install Requirements
pip install -r requirements.txt

4. Run the Streamlit App
streamlit run recommender_app.py

📂 Project Structure
movie-recommender-app/
│
├── recommender_app.py              # Main Streamlit app
├── content_based.pkl               # Saved content-based similarity matrix
├── item_based.pkl                  # Saved item-based similarity matrix
├── requirements.txt
├── .gitignore
└── README.md

📈 Next Steps

🔧 Integrate hybrid recommendations (combining both models)

🌐 Deploy the app on Streamlit Cloud or Render

🎞️ Add movie posters and metadata for richer visuals
