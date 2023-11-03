# A Movie recommendation system - Cinemate

#### Description:
The Movie Recommendation System is a Python-based application designed to provide personalized movie recommendations to users. The system utilizes user data and movie information to suggest movies that align with the user's preferences and interests. This document serves as a guide to understanding the different functionalities and usage of the system.

* Requirements:*
    To run the Movie Recommendation System, ensure you have the following software installed on your system:
    1. Python 
    2. Pandas library 

*** Functions:**
    1. get_movie_recommendations(user, n)
    This function takes a user object and the number of movie recommendations n as input and returns a list of n movie recommendations for the given user. The recommendations are generated based on the user's past interactions and movie attributes.

    2. get_users(df)
    This function reads the user data from the provided DataFrame df and returns a list of user objects. Each user object contains information such as name, age, gender, and movie preferences.

    3. add_movie(df)
    The add_movie function allows users to add new movies to the movie database. It takes the DataFrame df as input and prompts the user to enter details of the new movie, such as title, genre, and release year. The updated DataFrame is returned with the newly added movie.

    4. find_movie(df)
    This function enables users to search for movies in the database based on either the movie title or genre. It takes the DataFrame df and the search query as inputs and returns a list of movies that match the query.

    5. update_movie(df)
    Users can update the details of existing movies using the update_movie function. It takes the DataFrame df and the movie title as inputs and prompts the user to enter the updated information for the movie.

    6. delete_movie(df)
    The delete_movie function allows users to remove a movie from the database. It takes the DataFrame df and the movie title as inputs and deletes the corresponding movie entry from the DataFrame.

    7. menu()
    The menu function displays a user-friendly menu interface with different options, allowing users to interact with the Movie Recommendation System. Users can register, log in, manage the movie database, and receive personalized movie recommendations.

*** Usage:**
    1. Run the application 

    2. Upon running, the menu will be displayed, prompting the user to choose from various options.

    3. Users can manage the movie database by adding, finding, updating, or deleting movies.

    4. To receive movie recommendations, users can select the appropriate option from the menu and specify the number of recommendations they want.

    5. The system will generate personalized movie recommendations.

*** Conclusion:**
    The Movie Recommendation System provides an interactive and personalized movie recommendation experience for users. By leveraging collaborative filtering and content-based filtering techniques, the system suggests movies that cater to individual tastes and interests. Users can easily manage the movie database and explore new movies based on their preferences. Enjoy discovering exciting movies with the Movie Recommendation System!
