import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- Load saved models/matrices ---
with open("cosine_sim_df.pkl", "rb") as f:
    cosine_sim_df = pickle.load(f)

with open("item_similarity_df.pkl", "rb") as f:
    item_similarity_df = pickle.load(f)

with open("user_item_matrix.pkl", "rb") as f:
    user_item_matrix = pickle.load(f)


# --- Recommendation functions ---
def get_content_recommendations(movie_title, n=10):
    if movie_title not in cosine_sim_df.index:
        return None
    sim_scores = cosine_sim_df.loc[movie_title].sort_values(ascending=False).iloc[1:n+1]
    return sim_scores


def get_item_based_recommendations(user_id, user_item_matrix, item_similarity_df, n=10):
    if user_id not in user_item_matrix.index:
        return None
    
    user_ratings = user_item_matrix.loc[user_id]
    user_ratings = user_ratings[user_ratings > 0]

    if user_ratings.empty:
        return None

    weighted_scores = item_similarity_df[user_ratings.index].dot(user_ratings)
    similarity_sums = item_similarity_df[user_ratings.index].sum(axis=1)
    predicted_scores = weighted_scores / similarity_sums
    predicted_scores = predicted_scores.drop(user_ratings.index, errors='ignore')

    return predicted_scores.sort_values(ascending=False).head(n)


# --- Streamlit UI ---
st.title("🎬 Movie Recommender System")
st.write("Select a recommendation model to get personalized movie suggestions!")

model_type = st.selectbox("Choose a model:", ["Content-based", "Item-based"])

if model_type == "Content-based":
    movie_title = st.selectbox("Select a movie you like:", sorted(cosine_sim_df.index))
    n = st.slider("Number of recommendations:", 1, 20, 10)

    if st.button("Get Recommendations"):
        recommendations = get_content_recommendations(movie_title, n)
        if recommendations is not None:
            st.write("Top recommendations based on your selection:")
            for i, (title, score) in enumerate(recommendations.items(), 1):
                st.write(f"{i}. {title} (similarity: {score:.2f})")
        else:
            st.warning("Movie not found or insufficient data.")

else:
    user_id = st.selectbox("Select your user ID:", sorted(user_item_matrix.index))
    n = st.slider("Number of recommendations:", 1, 20, 10)

    if st.button("Get Recommendations"):
        recommendations = get_item_based_recommendations(user_id, user_item_matrix, item_similarity_df, n)
        if recommendations is not None:
            st.write("Top recommendations based on your ratings:")
            for i, (title, score) in enumerate(recommendations.items(), 1):
                st.write(f"{i}. {title} (predicted rating: {score:.2f})")
        else:
            st.warning("User not found or insufficient ratings.")
