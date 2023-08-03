import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os
import cowsay

cwd = os.getcwd()
file_path = os.path.join(cwd, "movies.csv")

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def get_similar_users(user, n, cosine_sim_df):
    similarity_values = cosine_sim_df[user]
    similarity_values = similarity_values.sort_values(ascending=False)
    return similarity_values.iloc[1:n+1]

def get_movie_recommendations(user, n, pivot_table, cosine_sim_df, df):
    similar_users = get_similar_users(user, 5, cosine_sim_df)
    similar_users_ratings = pivot_table.loc[similar_users.index]
    mean_ratings = similar_users_ratings.mean(axis=0)
    mean_ratings = mean_ratings.sort_values(ascending=False)
    rated_movies = pivot_table.loc[user]
    rated_movies = rated_movies[rated_movies > 0]
    mean_ratings = mean_ratings.drop(rated_movies.index)
    movie_titles = pd.DataFrame({'movieId': mean_ratings.index})
    movie_titles = pd.merge(movie_titles, df[['movieId', 'title']], on='movieId')
    
    already_rated_movies = list(rated_movies.index)
    movie_titles = movie_titles[~movie_titles['title'].isin(already_rated_movies)]
    
    return list(movie_titles['title'][:n])

def get_users(df):
    user_ratings = df.groupby('userId').count()['rating']
    user_ratings = user_ratings.sort_values(ascending=False)
    user_ratings = pd.DataFrame({'userId': user_ratings.index, 'count': user_ratings.values})
    user_ratings = user_ratings.head(10)
    print(user_ratings)
    choice = input("Do you want to see the next 10 users? (y/n): ").capitalize()
    if choice == "Y" or choice == "Yes":
        df.drop(df[df["userId"].isin(user_ratings["userId"])].index, inplace=True)
        get_users(df)

def add_movie(df):
    movie_name = input("Enter the movie name: ").strip()
    movie_name_lower = movie_name.lower()
    if movie_name_lower in df["title"].str.lower().unique():
        print("The movie is already in the list.")
    else:
        movie_id = df["movieId"].max() + 1
        movie_rating = float(input("Enter the movie rating: "))
        new_row = {"movieId": movie_id, "title": movie_name, "rating": movie_rating}
        df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
        print("The movie was added to the list.")
    return df

def find_movie(df):
    movie_name = input("Enter the movie name: ").strip()
    movie_name_lower = movie_name.lower()
    
    found_movies = df[df["title"].str.lower().fillna("").str.contains(movie_name_lower)]
    
    if not found_movies.empty:
        print("\nFound movies:")
        for index, row in found_movies.iterrows():
            print(f"Movie: {row['title']} | Rating: {row['rating']}")
    else:
        print("No movies found with the given name.")


def update_movie(df):
    movie_name = input("Enter the movie name: ").strip()
    movie_name_lower = movie_name.lower()
    found_movies = df[df["title"].str.lower() == movie_name_lower]
    if not found_movies.empty:
        movie_rating = float(input("Enter the movie rating: "))
        df.loc[found_movies.index, "rating"] = movie_rating
        print("The movie rating was updated.")
    else:
        print("The movie is not in the list.")
        add_movie(df)

def delete_movie(df):
    movie_name = input("Enter the movie name: ").strip()
    movie_name_lower = movie_name.lower()
    found_movies = df[df["title"].str.lower() == movie_name_lower]
    if not found_movies.empty:
        df.drop(found_movies.index, inplace=True)
        print("The movie was deleted from the list.")
    else:
        print("The movie is not in the list.")

def continue_choice():
    continue_choice = input("Do you want to continue? (y/n): ").capitalize()
    return continue_choice == "Y" or continue_choice == "Yes"

def menu(pivot_table, cosine_sim_df, df):
    while True:
        print("\n1. Get movie recommendations")
        print("2. Get users")
        print("3. Add movie")
        print("4. Update movie rating")
        print("5. Delete movie")
        print("6. Find movie by name")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Try again.")
            continue
        
        if choice == 1:
            user = int(input("Enter the user id: "))
            n = int(input("Enter the number of movie recommendations: "))
            recommendations = get_movie_recommendations(user, n, pivot_table, cosine_sim_df, df)
            print("\nMovie Recommendations:")
            for i, movie in enumerate(recommendations, start=1):
                print(f"{i}. {movie}")
            if not continue_choice():
                break
        
        elif choice == 2:
            get_users(df)
        
        elif choice == 3:
            df = add_movie(df)
        
        elif choice == 4:
            update_movie(df)
        
        elif choice == 5:
            delete_movie(df)
        
        elif choice == 6:
            find_movie(df)
        
        elif choice == 7:
            print("Goodbye!")
            break


def welcome_message():
    print("\nWelcome to Cinemate!")
    print()
    cowsay.tux("Hello! I'm here to help you discover awesome movies!")
    print()


def main():
    welcome_message()
    df = load_data(file_path)
    pivot_table = df.pivot_table(index='userId', columns='movieId', values='rating')
    pivot_table = pivot_table.fillna(0)
    cosine_sim = cosine_similarity(pivot_table)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_table.index, columns=pivot_table.index)
    menu(pivot_table, cosine_sim_df, df)

if __name__ == "__main__":
    main()