import pandas as pd
import streamlit as st

# Load the dataset
movies_df = pd.read_excel("/workspaces/blank-app/movie.xlsx")

# Title of the app
st.title("Movie Recommendation App")

# User inputs
carrier = st.multiselect("Select Carrier", ["amazon", "netflix"])
price = st.selectbox("Select Price", ["free", "paid"])
list_of_gerns = movies_df["genre"].str.split(", ").explode().unique()
genre = st.multiselect("Select Genre", list_of_gerns)


# Filter movies based on user input
recommended_movies = movies_df[
    (movies_df["carrier"].apply(lambda x : any(gene in x for gene in carrier))) &
    (movies_df["price"] == price) &
    (movies_df["genre"].apply(lambda x : any(gene in x for gene in genre)))
]

# Display recommended movies
st.write("Recommended Movies:")
st.dataframe(recommended_movies)

