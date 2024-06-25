import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

with open("data/features.pkl", "rb") as f:
    features = pickle.load(f)


def search_similar_images(query_feature, top_k=5):
    image_names = list(features.keys())
    image_features = np.array(list(features.values()))
    similarities = cosine_similarity([query_feature], image_features)[0]
    similar_indices = similarities.argsort()[-top_k:][::-1]
    similar_images = [
        {"image_name": image_names[idx], "similarity": float(similarities[idx])}
        for idx in similar_indices
    ]
    return similar_images
