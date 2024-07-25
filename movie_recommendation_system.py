# -*- coding: utf-8 -*-
"""Movie_recommendation_system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bCxa4Qr7PJ3yQDLU-gn8TzeT-ARQPek7

importin the dependencies
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""Data Collection and Preprocessing"""

# loading data from csv file to a pandas dataframe
movies_data= pd.read_csv(r'projects/movies.csv')

# printing first five rows
movies_data.head()

# number of rows and columns in data frame
movies_data.shape

#selecting relevant features for recommendation

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# replacing null values with null string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# combining all the 5 selected features
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

# converting text data to featyre vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

"""Cosine Similarity"""

# getting similarity score using cosine similarity
similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# getting movie name from user
movie_name = input('Enter your favorite movie name:')

# creating list with all movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# finding the close match for the movie name given by user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match =find_close_match[0]
print(close_match)

# indec of movie with title

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# getting a list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

sorted_similar_movies = sorted(similarity_score , key = lambda x:x[1] , reverse = True)
print(sorted_similar_movies)

print("Movies suggested")
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if (i<30):
        print(i,',',title_from_index)
        i+=1

"""# Movie Recommendation System"""

movie_name = input('Enter movie name:')
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match =find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
len(similarity_score)
sorted_similar_movies = sorted(similarity_score , key = lambda x:x[1] , reverse = True)
print("Movies suggested")
i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if (i<30):
        print(i,'.',title_from_index)
        i+=1

