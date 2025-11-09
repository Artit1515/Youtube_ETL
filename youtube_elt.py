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

url = f"https://youtube.googleapis.com/youtube/v3/channels?part={part}&forHandle=%40{channel_id}&key={YOUTUBE_API_KEY}"

def get_plist_id(url):
    response = requests.get(url)
    data = response.json()

    items_data = data["items"][0]
    chanels_playlists_id = items_data["contentDetails"]["relatedPlaylists"]["uploads"]
    print((chanels_playlists_id))
    return chanels_playlists_id

if __name__ == "__main__":
    get_plist_id(url)