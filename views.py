from django.shortcuts import render
import pandas as pd
import random

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

# Define the Django views
def mood_view(request):
    if request.method == "POST":
        mood = request.POST.get("mood")
        language = request.POST.get("language")

        # Call the recommend_songs function to recommend 10 songs
        recommended_songs = recommend_songs(mood, language)

        context = {
            "mood": mood,
            "language": language,
            "recommended_songs": recommended_songs
        }

        return render(request, "mood.html", context)
    else:
        return render(request, "mood.html")

def face_view(request):
    # Code for your face button
    return render(request, "face.html")

def location_view(request):
    # Code for your location button
    return render(request, "location.html")
