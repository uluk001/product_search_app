import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os


def load_features(feature_file="data/features.pkl"):
    if not os.path.exists(feature_file):
        raise FileNotFoundError(f"Feature file '{feature_file}' does not exist.")
    with open(feature_file, "rb") as f:
        features = pickle.load(f)
    return features


def search_similar_images(query_feature, top_k=5):
    features = load_features()
    image_names = list(features.keys())
    image_features = np.array(list(features.values()))
    similarities = cosine_similarity([query_feature], image_features)[0]
    similar_indices = similarities.argsort()[-top_k:][::-1]
    similar_images = [
        {"image_name": image_names[idx], "similarity": float(similarities[idx])}
        for idx in similar_indices
    ]
    return similar_images
