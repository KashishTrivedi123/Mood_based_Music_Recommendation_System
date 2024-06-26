#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd

# Load the Bollywood songs dataset
bollywood_songs_df = pd.read_excel(r"C:\Users\kashish trivedi\Desktop\Project\final_Bollywood_songs.xlsx")

# Load the English songs dataset
english_songs_df = pd.read_excel(r"C:\Users\kashish trivedi\Desktop\english_music_dataset.xlsx")

# Define the mappings of locations and moods to specific song genres
location_mood_mapping = {
    "Gym": ["Angry", "Energetic", "Motivational"],
    "Travelling": ["Happy", "Sad", "Calm"],
    "Beach": ["Happy", "Sad", "Calm"],
    "Party": ["Energetic", "Romantic"],
    "Running": ["Energetic"],
    "Studying": ["Calm"]
}

# Define a function to recommend songs based on the user's location, mood, and language preference
def recommend_songs(location, language):
    songs = []
    if language == "Hindi":
        songs_df = bollywood_songs_df
    elif language == "English":
        songs_df = english_songs_df
    
    # Get the mood based on the selected location
    mood_genres = location_mood_mapping.get(location, [])
    mood = ", ".join(mood_genres)
    
    # Filter the songs based on location and mood
    mood_songs_df = songs_df[songs_df["Genre"].isin(mood_genres)]
    
    # Select 20 random songs from the filtered dataset
    sampled_songs_df = mood_songs_df.sample(20)
    
    for _, song in sampled_songs_df.iterrows():
        song_name = song["name"]
        artist_name = song["artist"]
        lastfm_url = song["Lastfm_url"]
        if lastfm_url:
            songs.append(f"[{song_name} by {artist_name}]({lastfm_url})")
        else:
            songs.append(f"{song_name} by {artist_name}")
    return songs

# Create the Streamlit app
st.title("SOUNDSCAPE")

# User selection for location
location_options = ["Gym", "Travelling", "Beach", "Party", "Running", "Studying"]
location = st.selectbox("Select your location:", location_options)

# User selection for language
language_options = ["Hindi", "English"]
language = st.selectbox("Select a language:", language_options)

# Call the recommend_songs function to recommend songs based on user selection
recommended_songs = recommend_songs(location, language)
num_songs_to_display = 10

start_index = st.session_state.get("start_index", 0)

if len(recommended_songs) > num_songs_to_display:
    if st.button("Next"):
        start_index += num_songs_to_display
        if start_index >= len(recommended_songs):
            start_index = 0
        st.session_state["start_index"] = start_index

end_index = start_index + num_songs_to_display
next_songs = recommended_songs[start_index:end_index]
st.write(f"Here are {len(next_songs)} {location} songs in {language}:")
for song in next_songs:
    st.write(song)


# In[ ]:





# In[ ]:




