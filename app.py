import streamlit as st
import pandas as pd
import random
import spotipy
import numpy as np
import config
import json
from spotipy.oauth2 import SpotifyClientCredentials


#Initialize SpotiPy with user credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.client_id,
                                                           client_secret= config.client_secret))


# Load  data
billboard_hot_100_df = pd.read_csv("billboard_hot_100.csv")
whole_df = pd.read_csv("whole_df.csv")


# Your cluster labels
cluster_labels = {
    0: "Energetic Dance-Pop",
    1: "Chilled Acoustic Ballads",
    2: "Upbeat Pop/Rock",
    3: "Funky Danceable Pop",
    4: "Happy Party Pop",
    5: "Relaxed Instrumental / Lo-fi"
}

st.title("🎵 Spotify Song Recommender")

# Ask user if they want a trending song or cluster
song_type = st.selectbox("What type of song do you want?", ["Trending", "By Cluster"])

if song_type == "Trending":
    if st.button("Get Trending Song"):
        recommendation = random.choice(billboard_hot_100_df.index)
        song = billboard_hot_100_df.loc[recommendation, 'song_title']
        artist = billboard_hot_100_df.loc[recommendation, 'artist']
        results = sp.search(q=song, type="track", limit=5, market="GB")
        track_id = results["tracks"]["items"][0]["id"]

        st.write(f"**Your trending song is:** {song}")
        st.write(f"**Artist:** {artist}")
        st.components.v1.iframe(f"https://open.spotify.com/embed/track/{track_id}", width=320, height=80)

else:
    cluster_choice = st.selectbox("Choose a music type:", list(cluster_labels.values()))

    if st.button("Get Cluster Songs"):
        # Find cluster number by label
        cluster_no = [k for k, v in cluster_labels.items() if v == cluster_choice][0]
        cluster_songs = whole_df[whole_df["cluster"] == cluster_no]

        sample = cluster_songs.sample(3)
        for _, row in sample.iterrows():
            track_id = row["track_id"]
            track_name = row["track_name"]
            artist = row["artists"]

            st.write(f"🎶 {track_name} — {artist}")
            st.components.v1.iframe(f"https://open.spotify.com/embed/track/{track_id}", width=320, height=80)





