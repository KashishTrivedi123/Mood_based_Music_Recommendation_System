#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import random

# Load the dataset for Bollywood songs
hindi_songs_df = pd.read_excel(r"C:\Users\kashish trivedi\Desktop\Project\final_Bollywood_songs.xlsx")

# Load the dataset for English songs
english_songs_df = pd.read_excel(r"C:\Users\kashish trivedi\Desktop\Project\data_moods (1).xlsx")

# Define a function to recommend 10 songs based on the user's mood and language preference
def recommend_songs(mood, language):
    songs = []
    if mood == "Mysterious":
        # Combine all moods for the mysterious mood
        mood_songs_df = pd.concat([hindi_songs_df, english_songs_df])
    elif language == "Hindi":
        # Filter the Bollywood songs dataset by the user's mood
        mood_songs_df = hindi_songs_df[hindi_songs_df["Genre"] == mood]
    elif language == "English":
        # Filter the English songs dataset by the user's mood
        mood_songs_df = english_songs_df[english_songs_df["mood"] == mood]
    # Select 10 random songs from the filtered dataset
    selected_songs_df = mood_songs_df.sample(10)
    for index, row in selected_songs_df.iterrows():
        song = row["name"]
        artist = row["artist"]
        lastfm_url = row["Lastfm_url"]
        if lastfm_url:
            songs.append(f"[{song} by {artist}]({lastfm_url})")
        else:
            songs.append(f"{song} by {artist}")
    return songs

# Create the Streamlit app
st.title("SOUNDSCAPE")
mood_options = ["Happy", "Sad", "Romantic", "Energetic", "Calm", "Neutral", "Motivational", "Angry", "Mysterious"]
mood = st.selectbox("Select your mood:", mood_options)
language_options = ["Hindi", "English"]
language = st.selectbox("Select a language:", language_options)

# Call the recommend_songs function to recommend 10 songs
recommended_songs = recommend_songs(mood, language)
st.write(f"Here are 10 {mood} {language} songs:")
for song in recommended_songs:
    st.write(song)

# Add a "Next" button to show the next 10 songs
if len(recommended_songs) >= 10:
    if st.button("Next"):
        recommended_songs = recommend_songs(mood, language)
        st.write(f"Here are the next 10 {mood} {language} songs:")
        for song in recommended_songs:
            st.write(song)


# In[ ]:




