import os
import random
from data.songs import songs_array as songs_array
from flask import Flask, render_template

app = Flask(__name__)

def select_songs():
    '''
    This functions selects the 10 random songs that the player will have to guess
    by creating an array of 10 random indexes. 
    '''
    return [random.randint(0, len(songs_array)) for i in range(10)]

# def start_game():

# Functions to create:
# Start the game -> gets the name of user, starts a counter for the number of rounds, redirects to the first game page. 
# Verifies if the user found the correct title
# Verifies if the user found the correct artiste
# Counts the points (1 artist, 1 title, 3 both)
# Goes to the next song
# Ends the game -> gets the final score, stores the score in the DB, redirect to the last page


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<int:song_number>/")
def play_song(song_number):
    return render_template('playing.html', song = songs_array[song_number]["preview_url"])


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)