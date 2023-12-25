from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from utils.text_cleaner import text_cleaning
from data.data_processing import get_data, get_recommender, get_adjacency_matrix, get_rating_matrix
import numpy as np
import pandas as pd

def get_recommendations(title):
    df = get_data("data/food.csv")
    df['Describe'] = df['Describe'].apply(text_cleaning)
    rating = get_data("data/ratings.csv")
    rating_matrix = get_rating_matrix(rating)
    recommender = get_recommender(get_adjacency_matrix(rating))

    user = df[df['Name'] == title]
    user_index = np.where(rating_matrix.index == int(user['Food_ID']))[0][0]
    user_ratings = rating_matrix.iloc[user_index]

    reshaped = user_ratings.values.reshape(1, -1)
    distances, indices = recommender.kneighbors(reshaped, n_neighbors=16)

    nearest_neighbors_indices = rating_matrix.iloc[indices[0]].index[1:]
    nearest_neighbors = pd.DataFrame({'Food_ID': nearest_neighbors_indices})

    result = pd.merge(nearest_neighbors, df, on='Food_ID', how='left')
    print(result)
    return result