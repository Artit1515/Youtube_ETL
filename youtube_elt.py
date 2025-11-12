from dotenv import load_dotenv
import os
import requests
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='requests')

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
channel_id = "GoWentGo" 
part = "contentDetails"
max_results = 50


channel_url = f"https://youtube.googleapis.com/youtube/v3/channels?part={part}&forHandle=%40{channel_id}&key={YOUTUBE_API_KEY}"


def get_playlist_id(url):
    try:
        response = requests.get(channel_url)
        data = response.json()

        items_data = data["items"][0]
        chanels_playlists_id = items_data["contentDetails"]["relatedPlaylists"]["uploads"]
        print((chanels_playlists_id))
        return chanels_playlists_id
    except Exception as e:
        raise e



def get_videos_id():
    base_playlist_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_results}&playlistId={get_playlist_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(base_playlist_url)
    data = response.json()
    video_id = []
    while True:
  
        for i in data["items"]:
            video = i["contentDetails"]["videoId"]
            video_id.append(video)

        next_page_token = data.get("nextPageToken")
        
        
        if next_page_token:
            next_page = f"{base_playlist_url}&pageToken={next_page_token}"
            response = requests.get(next_page)
            data = response.json()
            print("Fetching next page...")
            print("Total videos so far:", len(video_id))
            print(data)

        if not next_page_token: 
            print(video_id)
            print("Total videos:", len(video_id))
            return video_id
            break




    





if __name__ == "__main__":
    get_playlist_id = get_playlist_id(channel_url)
    get_videos_id() 
