# Mini Project Week 13 Spotify Song Recommender
Scenario: I have been hired as a Data Analyst for Gnoosic. The goal is to redefine how users discover music, not just based on their listening history but by allowing them to explore songs based on sound, mood, and energy. The outcome is to design a new music recommendation system that gives users two powerful ways to find songs: 1. By selecting a type of music they want to listen to (e.g. Rock, High Energy, Calm). 2. By asking for a currently trending song, no matter the genre. This interactive music recommender will be tested live and assessed.

# 1. Scrape the Most Popular Songs Right Now on [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)
To create the billboard_hot_100_df = pd.DataFrame({"song_title": song_title, "artist": artist_name})
* Use the Spotify API (spotipy) for the function: def recommend_song():  
    song_choice = input("Do you want a trending song? Please enter yes or no")
    if song_choice.lower() == "yes":
        recommendation = random.choice(billboard_hot_100_df.index)
        song = billboard_hot_100_df.loc[recommendation, 'song_title']
        artist = billboard_hot_100_df.loc[recommendation, 'artist']
        results=sp.search(q=song,type ="track",limit=5,market="GB")
        track_id = results["tracks"]["items"][0]["id"] 
        print("your trending song is: " ,song)
        print("your trending artist is: " ,artist)
            
    else:
        return print("we're still working on it")


# 2. Feature Selection and Feature Engineering of Spotify Audio Features:
   [Audio Features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)
   using audio_features_dataset_curated.csv/

# 3. Find the Best Number of Clusters through Elbow Method and Silhouette Score (I tried 6 and 7).

# 4. Listen to each Cluster's Songs and Label, using a random sample and the def recommend_cluster_song(whole_df, cluster_no) function.

# 5. Continue Working on the Program:
def recommend_song():  
    song_choice = input("Do you want a trending song? Please enter yes or no")
    if song_choice.lower() == "yes":
        recommendation = random.choice(billboard_hot_100_df.index)
        song = billboard_hot_100_df.loc[recommendation, 'song_title']
        artist = billboard_hot_100_df.loc[recommendation, 'artist']
        results=sp.search(q=song,type ="track",limit=5,market="GB")
        track_id = results["tracks"]["items"][0]["id"] 
        print("your trending song is: " ,song)
        print("your trending artist is: " ,artist)
        return(play_song(track_id))

# for the next else part, do a loop where it goes through each cluster/label and plays a sample from that song    
    
    else:
        # Ask the user which cluster label they want to listen to
        cluster_labels = {
        0: "Chill Acoustic / Indie",
        1: "Mainstream Dance Pop",
        2: "High-Energy EDM / Pop Rock",
        3: "Singer-Songwriter Ballads",
        4: "Instrumental Beats / Lo-Fi",
        5: "Chill Jazz / Downtempo",
        6: "Ambient / Relaxed Classical"
    }

        print("Available music types:")
        for lbl in cluster_labels.values():
            print("-", lbl)

        user_choice = input("What type of music do you want to listen to")
        # Find which cluster number matches that label
        cluster_no= None
        for no, lbl in cluster_labels.items():
            if user_choice.lower() in lbl.lower():
                cluster_no = no
                break

        if cluster_no is None:
            print("Sorry, that choice is not available.")
            return None

        # Filter songs from chosen cluster
        cluster_songs = whole_df[whole_df["cluster"] == cluster_no]

        # Play 3 random songs
        sample = cluster_songs.sample(3) 
        print(f"songs from cluster {lbl}:") 
        for id in sample["track_id"]: 
            display(play_song(id)) 

          <img width="740" height="748" alt="image" src="https://github.com/user-attachments/assets/72e6b3d2-ed61-4a59-b4cf-e909d7f1543c" />


# 6. Streamlit! 

<img width="1280" height="832" alt="image" src="https://github.com/user-attachments/assets/273e6285-869d-440d-bb96-bc44b14ecdcd" />
<img width="1280" height="832" alt="image" src="https://github.com/user-attachments/assets/5af01d53-b19a-43a7-a892-6420125632d4" />



