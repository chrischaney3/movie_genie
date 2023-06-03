#Dependencies needed for python file:
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create the variable to read the csv.
filepath = ("Data/movie_genie_df_Final.csv")
movies_data = pd.read_csv(filepath)

movies_data.reset_index(inplace=True)

#Examine the first fiver row to confirm successful read.
movies_data.head()

#Check the data has been cleaned and check shape.
movies_data.info()

#Created a variable to hold the columns that determine the best values
selected_features = ['genres', 'budget', 'overview', 'popularity', 'production_companies', 'release_date', 'cleaned_keywords']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Merge columns together to create a unique ID
# Convert float columns to strings
movies_data['budget'] = movies_data['budget'].astype(str)
movies_data['popularity'] = movies_data['popularity'].astype(str)

# Merge columns together to create a unique ID
movie_database = movies_data['genres']+' '+movies_data['budget']+' '+movies_data['overview']+' '+movies_data['popularity']+' '+movies_data['production_companies']+' '+movies_data['release_date']+' '+movies_data['cleaned_keywords']

#Holding the place for the variable in the html input
movie_title = input("What is your favorite movie: ")

#Create a list of titles to pair to the features down the road
list_of_titles = movies_data['title'].tolist()


import difflib

# Filter out NaN or non-string values from list_of_titles
filtered_titles = [title for title in list_of_titles if isinstance(title, str)]

# Get the closest match to the input movie title
closest_match = difflib.get_close_matches(movie_title, filtered_titles, n=1, cutoff=0.6)

# Check if a close match was found
if closest_match:
    close_match = closest_match[0]
    print(f"Closest match: {close_match}")
    index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]
    print(f"Index of the movie: {index_of_the_movie}")
else:
    print("No close match found.")


from sklearn.neighbors import NearestNeighbors

# Convert movie_database to a TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movie_database.astype(str).values.astype('U'))

# Initialize the NearestNeighbors model
nn_model = NearestNeighbors(metric='cosine')
nn_model.fit(tfidf_matrix)

# Get the index of the input movie title
input_title_index = list_of_titles.index(close_match)

# Find the indices of similar movies (excluding the exact match)
similar_movie_indices = nn_model.kneighbors(tfidf_matrix[input_title_index], n_neighbors=31, return_distance=False)[0][1:]

# Print the similar movies
print('Movies suggested for you:\n')
for index in similar_movie_indices:
    print(list_of_titles[index])





