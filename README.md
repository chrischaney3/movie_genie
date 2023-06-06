![Screen-Shot-2018-10-10-at-3](https://github.com/chrischaney3/movie_genie/assets/112741203/e1ec48e2-78e9-45ae-95aa-c5cd9e26c51d)
http://kyrabob.pythonanywhere.com/



# The Movie Genie Web Application
## Overview:
Movie Genie is a movie recommendation web app designed to provide personalized movie suggestions based on users' preferences. With a vast database of movies spanning different genres and eras, our app aims to enhance the movie-watching experience by offering relevant and curated recommendations. Leveraging advanced machine learning algorithms, Movie Genie analyzes user preferences, viewing history, and user-generated ratings to generate accurate and tailored movie suggestions.


### Created by: 
Chris Chaney, Farrukh Sultani, Kyra Achee, Katherine Winder and Terry Goins

## Instructions:
Create a machine learning algorithm for recommending personalized movie suggestions based on movie preferences.
- ***Clean the data:*** Ensure the data used for training the model is clean and well-structured.
- ***Process the data:*** Transform and preprocess the data to prepare it for training the machine learning model.
- ***Create the Vector Algorithm:*** Develop an algorithm that can represent user preferences and movie features as vectors for efficient computation.
- ***Train the model:*** Utilize the processed data to train the machine learning model that will generate movie recommendations.
- ***Finalizing the topic:*** Refine the topic and scope of the project, ensuring it aligns with the objectives of Movie Genie.
- ***Coming up with the possible data source:*** Identify potential data sources such as Kaggle or IMDb for gathering movie-related information.

## Clean The Data:
![Screenshot_20230605_124430](https://github.com/chrischaney3/movie_genie/assets/112741203/e4816a12-37b3-4258-843f-75f5c21eb455)

## Turning Qualitative to Quantitative
  - To find movie similarities it was necessary to transform words into a unique descriptor to compare
  - The user input needs to match with the dataset so we use the difflib.get_close_matches against the list of movie titles in title      columns
  - Then we can reference index instead of title further on
![Screenshot_20230605_011813](https://github.com/chrischaney3/movie_genie/assets/112741203/98cb5edc-de99-44c6-bbfc-60ca9542533a)

## Model and List
  - We use the vectorizer to convert the raw text strings into numbers
  - Using the NearestNeighbors algorithm we identify the most similar attributes
  - We use the newly ordered data compared to the input title and pull indices most near to create a list of similar movies
  ![Screenshot_20230605_012828](https://github.com/chrischaney3/movie_genie/assets/112741203/7e3ac995-afb3-454e-9623-d6fdec6abc00)

## style.css
***This style sheet determines the font, the text size, and colorscheme.***

<img width="362" alt="Screenshot 2023-06-04 at 10 00 08 PM" src="https://github.com/chrischaney3/movie_genie/assets/112666732/a66c1112-2718-4e91-a923-629e3abcbfaa">

## data.html
The html file references the style sheet for the flask app in the header section, then has the input section for the user to input their favorite movie title after the prompt. First it outputs the model's guess for what the user inputted with an "if" statement for whether the inputted movie is the first in the similar_movie_indices list. The user can misscapitalize, misspell, or leave out punctuation in their input, and the model will return it's assumption under "Did you mean:". It displays the text "I think you will like: " and displays the the top 3 movie suggestions in the similar_movie_indices. The href creates a hyperlink to the imdb page for each movie suggested. 
![Screenshot_20230605_013346](https://github.com/chrischaney3/movie_genie/assets/112741203/32bbe1ff-e143-4d4e-bf46-51a19983b177)

## The Flask App 
The python file contains one route to render the index.html template and the function for the model
![Screenshot_20230605_013301](https://github.com/chrischaney3/movie_genie/assets/112741203/562b8be2-f6f4-48b8-8f14-8ca8e1ee9b0f)

  - Reference a style sheet
  - Textbox for user to input their favorite movie
  - Guesses what it thinks the user inputs
  - Gives 3 suggestions
  - Links to each listed movie’s Imdb
  

## Deploying Script on pythonanywhere
  - Create directories
  - Upload files
  - Change relevant file paths
  
![Screenshot_20230605_014014](https://github.com/chrischaney3/movie_genie/assets/112741203/0fcd6d40-2f39-4ddc-9256-6baa405b8342)

![Screenshot_20230605_014031](https://github.com/chrischaney3/movie_genie/assets/112741203/a325d5f3-acaf-4302-b987-f7733ab3239a)



## Challenges with Deploying Script
- Different rules for file paths than on local computer
- Unintuitive debugging help

![Screenshot_20230605_013817](https://github.com/chrischaney3/movie_genie/assets/112741203/21ac6cca-d195-42c7-b61a-cfc5237f6fcb)

movie_app.py
Imports the necessary libraries for the model and for Flask
Contains a route to render the data.html template and calls the make_suggestion function
Defines the make_suggestion function with the code for the model which returns a list comprehension of the movie title and year of the movie in a link to the imdb.


## Demonstartion:
![Screenshot 2023-06-05 at 6 20 43 PM](https://github.com/chrischaney3/movie_genie/assets/112741203/b600cc29-d3d1-49b9-a90d-651655647c60)


## Resources:
  - https://youtu.be/v1PfNYOQ4Fk
  - https://pythonanywhere.com 
