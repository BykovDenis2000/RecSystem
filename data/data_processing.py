import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def get_data(data_path):
    df = pd.read_csv(data_path)
    return df
def get_rating_matrix(rating):
    rating_matrix = rating.pivot_table(index='Food_ID', columns='User_ID', values='Rating').fillna(0)
    return rating_matrix
def get_adjacency_matrix(rating):
    rating_matrix = rating.pivot_table(index='Food_ID', columns='User_ID', values='Rating').fillna(0)
    csr_rating_matrix = csr_matrix(rating_matrix.values)
    return csr_rating_matrix
def get_recommender(csr_rating_matrix):
    recommender = NearestNeighbors(metric='cosine')
    recommender.fit(csr_rating_matrix)
    return recommender
