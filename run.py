import os
import random
from data.songs import songs_array as songs_array
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

current_game = {
    'score' : {},
    'songs' : []
}

def select_songs():
    '''
    This functions selects the 10 random songs that the player will have to guess
    by creating an array of 10 random indexes. 
    '''
    return [random.randint(0, len(songs_array)) for i in range(10)]
    
    
def start_game():
    """
    Sets the current user and current song and sets the score to an empty list
    """
    current_game['score'].clear()
    songs = select_songs()
    for song in songs:
        current_game['songs'].append(song)

# Functions to create:
# Verifies if the user found the correct title
# Verifies if the user found the correct artiste
# Counts the points (1 artist, 1 title, 3 both)
# Goes to the next song
# Ends the game -> gets the final score, stores the score in the DB, redirect to the last page



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_game()
        return redirect(current_game['songs'][0])
    return render_template('index.html')


@app.route("/<int:song_number>/")
def play_song(song_number):
    print(current_game)
    return render_template('playing.html', song = songs_array[song_number]["preview_url"])


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)