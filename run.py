import os
from data.songs import songs_array as songs_array

from flask import Flask, render_template,redirect 

app = Flask(__name__)

# Functions to create:
# Start the game -> gets the name of user, starts a counter for the number of rounds, redirects to the first game page. 
# Select a random song
# Verifies if the user found the correct title
# Verifies if the user found the correct artiste
# Counts the points (1 artist, 1 title, 3 both)
# Goes to the next song
# Ends the game -> gets the final score, stores the score in the DB, redirect to the last page


@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/<index>")
def play_song(index):
    return "<audio controls='controls' autoplay><source src={} /></audio>".format(songs_array[int(index)]["preview_url"])


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)