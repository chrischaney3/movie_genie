# The Movie Genie Web Application
## Overview:
Movie Genie is a movie recommendation web app designed to provide personalized movie suggestions based on users' preferences. With a vast database of movies spanning different genres and eras, our app aims to enhance the movie-watching experience by offering relevant and curated recommendations. Leveraging advanced machine learning algorithms, Movie Genie analyzes user preferences, viewing history, and user-generated ratings to generate accurate and tailored movie suggestions.
## Instructions:
Create a machine learning algorithm for recommending personalized movie suggestions based on movie preferences.
- ***Clean the data:*** Ensure the data used for training the model is clean and well-structured.
- ***Process the data:*** Transform and preprocess the data to prepare it for training the machine learning model.
- ***Create the Vector Algorithm:*** Develop an algorithm that can represent user preferences and movie features as vectors for efficient computation.
- ***Train the model:*** Utilize the processed data to train the machine learning model that will generate movie recommendations.
- ***Finalizing the topic:*** Refine the topic and scope of the project, ensuring it aligns with the objectives of Movie Genie.
- ***Coming up with the possible data source:*** Identify potential data sources such as Kaggle or IMDb for gathering movie-related information.

style.css
This style sheet determines the font, the text size, and colorscheme.
<img width="362" alt="Screenshot 2023-06-04 at 10 00 08 PM" src="https://github.com/chrischaney3/movie_genie/assets/112666732/a66c1112-2718-4e91-a923-629e3abcbfaa">
data.html
The html file references the style sheet for the flask app in the header section, then has the input section for the user to input their favorite movie title after the prompt. First it outputs the model's guess for what the user inputted with an "if" statement for whether the inputted movie is the first in the similar_movie_indices list. The user can misscapitalize, misspell, or leave out punctuation in their input, and the model will return it's assumption under "Did you mean:". It displays the text "I think you will like: " and displays the the top 3 movie suggestions in the similar_movie_indices. The href creates a hyperlink to the imdb page for each movie suggested. 
- insert the screenshot from slide 9
movie_app.py
Imports the necessary libraries for the model and for Flask
Contains a route to render the data.html template and calls the make_suggestion function
Defines the make_suggestion function with the code for the model which returns a list comprehension of the movie title and year of the movie in a link to the imdb.
-insert screenshot from slide 8

### Created by: 
Chris Chaney, Farrukh Sultani, Kyra Achee, Katherine Winder and Terry Goins















## Resources:
