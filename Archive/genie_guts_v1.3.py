#Dependencies needed for python file:
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

def make_suggestion(movie_title):
    # Create the variable to read the csv.
    filepath = ("Data/movies_cleaned.csv")
    movies_data = pd.read_csv(filepath)

    movies_data.reset_index(inplace=True)

    #Created a variable to hold the columns that determine the best values
    selected_features = ['genres', 'budget', 'original_language', 'runtime', 'vote_average', 'vote_count', 'cast_names', 'director_name', 'executive_producers', 'production_companies', 'release_date', 'keywords']

    # Fill in any "NA" with a blank
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    # Convert float columns to strings
    movies_data['budget'] = movies_data['budget'].astype(str)
    movies_data['runtime'] = movies_data['runtime'].astype(str)
    movies_data['vote_average'] = movies_data['vote_average'].astype(str)
    movies_data['vote_count'] = movies_data['vote_count'].astype(str)

    # Merge columns together to create a unique ID
    movie_database = movies_data['genres']+' '+movies_data['budget']+' '+movies_data['original_language']+' '+movies_data['runtime']+' '+movies_data['vote_average']+' '+movies_data['vote_count']+' '+movies_data['cast_names']+' '+movies_data['director_name']+' '+movies_data['executive_producers']+' '+movies_data['production_companies']+' '+movies_data['release_date']+' '+movies_data['keywords']

    #Create a list of titles to pair to the features down the road
    list_of_titles = movies_data['title'].tolist()
    list_of_poster_paths = movies_data['poster_path'].tolist()

    # Filter out NaN or non-string values from list_of_titles
    filtered_titles = [title for title in list_of_titles if isinstance(title, str)]

    # Get the closest match to the input movie title
    closest_match = difflib.get_close_matches(movie_title, filtered_titles, n=1, cutoff=0.6)

    # Check if a close match was found
    if closest_match:
        close_match = closest_match[0]
        index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]
        print(f"Index of the movie: {index_of_the_movie}")
    else:
        no_match = "No Match Found"

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

    return closest_match[0], list_of_titles[similar_movie_indices[0]], list_of_poster_paths[similar_movie_indices[0]], no_match
