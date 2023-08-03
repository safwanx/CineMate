from project import load_data, get_similar_users, get_movie_recommendations, get_users, add_movie
import pandas as pd
import pytest
from unittest.mock import patch
from sklearn.metrics.pairwise import cosine_similarity


def test_add_movie():
    df = pd.read_csv("movies.csv")
    movie_name = df["title"].iloc[-1]
    movie_id = df["movieId"].iloc[-1]
    with patch('builtins.input', side_effect=["New Movie Name", "10"]):
        df = add_movie(df)
    assert df["title"].iloc[-1] == "New Movie Name"
    assert df["rating"].iloc[-1] == 10.0
    df.drop(df[df["title"] == "New Movie Name"].index, inplace=True)
    df.to_csv("movies.csv", index=False)


def test_get_similar_users():
    df = pd.read_csv("movies.csv")
    user = 1
    n = 5
    pivot_table = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    cosine_sim = cosine_similarity(pivot_table)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_table.index, columns=pivot_table.index)
    similar_users = get_similar_users(user, n, cosine_sim_df)  # Pass cosine_sim_df as an argument
    assert len(similar_users) == n
    assert similar_users.index[0] != user


def test_get_movie_recommendations():
    df = pd.read_csv("movies.csv")
    user = 1
    n = 5
    pivot_table = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    cosine_sim = cosine_similarity(pivot_table)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=pivot_table.index, columns=pivot_table.index)
    movie_recommendations = get_movie_recommendations(user, n, pivot_table, cosine_sim_df, df)  # Pass required arguments
    assert len(movie_recommendations) == n
    assert movie_recommendations[0] != "Toy Story (1995)"


def test_get_users():
    df = pd.read_csv("movies.csv")
    with patch('builtins.input', return_value='1'): 
        get_users(df)
    assert True


def test_load_data():
    df = load_data("movies.csv")
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 6
    assert df.columns[0] == "movieId"
    assert df.columns[1] == "title"
    assert df.columns[2] == "genres"
    

def main():
    pytest.main(["-v", __file__])
    print("All tests passed")


if __name__ == "__main__":
    main()