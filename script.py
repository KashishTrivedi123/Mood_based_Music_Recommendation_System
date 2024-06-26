# streamlit_script.py

import streamlit as st
import pandas as pd
import json

# Load the dataset for Bollywood songs
hindi_songs_df = pd.read_excel('final_Bollywood_songs.xlsx')

# Load the dataset for English songs
english_songs_df = pd.read_excel('english_music_dataset.xlsx')

# Define a function to recommend 10 songs based on the user's mood and language preference
def recommend_songs(mood, language):
    songs = []
    if mood == "Mysterious":
        # Combine all moods for mysterious mood
        hindi_songs_df_mystery = hindi_songs_df[hindi_songs_df["Genre"] != "Instrumental"]
        english_songs_df_mystery = english_songs_df[english_songs_df["mood"] != "Other"]
        mood_songs_df = pd.concat([hindi_songs_df_mystery, english_songs_df_mystery])
    elif language == "Hindi":
        # Filter the Bollywood songs dataset by the user's mood
        mood_songs_df = hindi_songs_df[hindi_songs_df["Genre"] == mood]
    elif language == "English":
        # Filter the English songs dataset by the user's mood
        mood_songs_df = english_songs_df[english_songs_df["mood"] == mood]
    # Select 10 random songs from the filtered dataset
    song_list = mood_songs_df.sample(10)["name"].tolist()
    artist_list = mood_songs_df.sample(10)["artist"].tolist()
    link_list = mood_songs_df.sample(10)["Lastfm_url"].tolist()
    for i in range(10):
        if link_list[i]:
            songs.append(f"[{song_list[i]} by {artist_list[i]}]({link_list[i]})")
        else:
            songs.append(f"{song_list[i]} by {artist_list[i]}")
    return songs

# Create the Streamlit app
if 'songs' not in st.session_state:
    st.session_state.songs = []

if 'page' in st.experimental_get_query_params():
    page = st.experimental_get_query_params()['page'][0]
    if page == 'mood':
        if 'mood' not in st.session_state:
            st.session_state.mood = None
        if 'language' not in st.session_state:
            st.session_state.language = None

        st.title("SOUNDSCAPE")
        mood_options = ["Happy", "Sad", "Romantic", "Energetic", "Calm", "Neutral", "Motivational", "Angry", "Mysterious"]
        st.session_state.mood = st.selectbox("Select your mood:", mood_options, index=mood_options.index(st.session_state.mood) if st.session_state.mood else None)
        language_options = ["Hindi", "English"]
        st.session_state.language = st.selectbox("Select a language:", language_options, index=language_options.index(st.session_state.language) if st.session_state.language else None)

        if st.button("Recommend Songs"):
            recommended_songs = recommend_songs(st.session_state.mood, st.session_state.language)
            st.session_state.songs = recommended_songs

    elif page == 'face':
        st.write("Face Detection page content")

    elif page == 'location':
        st.write("Location page content")

if st.session_state.songs:
    st.json({"songs": st.session_state.songs})
