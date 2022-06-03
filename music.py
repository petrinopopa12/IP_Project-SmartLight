import spotify as spotify
#from dotenv import load_dotenv
import os
from flask import Blueprint
import requests

#load_dotenv()
music = Blueprint('music', __name__)
SECRET_KEY = os.getenv("SPOTIFY_TOKEN")

@music.route('/song/<songid>', methods=['GET'])
def get_song(songid):
    song = requests \
        .get(f'https://api.spotify.com/v1/tracks/{songid}',
                headers={'Authorization': f'Bearer {SECRET_KEY}'}) \
        .json()

    return song