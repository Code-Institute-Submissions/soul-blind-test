import os
import random
from data.songs import songs_array as songs_array
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#config the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)


# Set up the Database with on table for the player, one that link the player to a game and one that links a game to songs and scores. 
class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    def __init__(self, username):
        self.username = username
    
    
class Game_with_Players(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    player = db.Column(db.Integer, db.ForeignKey(Player.id), nullable=False)
    rounds_played = db.Column(db.Integer, nullable=False)
    
    def __init__(self, player, rounds_played):
        self.player = player
        self.rounds_played = rounds_played
    
class Game_with_Songs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    game = db.Column(db.Integer, db.ForeignKey(Game_with_Players.id), nullable=False)
    song = db.Column(db.Integer, nullable = False)
    round_numb = db.Column(db.Integer, nullable = False)
    points = db.Column(db.Integer, nullable = True)
    
    def __init__(self, game, song, round_numb, points):
        self.game = game
        self.song = song
        self.round_numb = round_numb
        self.points = points



# HELPER FUNCTIONS 
def select_songs():
    '''
    This functions selects the 10 random songs that the player will have to guess
    by creating an array of 10 random indexes. 
    '''
    return [random.randint(0, len(songs_array)) for i in range(10)]

def answer_is_correct(user_input, song_number, to_check):
    '''
    This function takes a song number and verifies if the user input corresponds to the song's title
    '''
    return user_input.lower() == songs_array[song_number][to_check].lower()
    

def calculate_points(song_number, title_input, artist_input):
    #Handle the case when the user doesn't answer one or two fields
    if not title_input:
        title_input = 'wrong'
    
    if not artist_input:
        artist_input = 'wrong'
    
    if answer_is_correct(title_input, song_number, 'title') and answer_is_correct(artist_input, song_number, 'artist'):
        return 3
    elif answer_is_correct(title_input, song_number, 'title') or answer_is_correct(artist_input, song_number, 'artist'):
        return 1
    else:
        return 0


#Functions to interact with the database
def create_a_player(username):
    '''
    This function adds a new user to the database
    '''
    db.session.add(Player(username))
    db.session.commit()
    
    
def add_game(player_id):
    '''
    This function adds a new game associated with a player_id
    '''
    db.session.add(Game_with_Players(player_id, 0))
    db.session.commit()
    

def get_player_id(player):
    '''
    This function returns the player's id in the database
    '''
    return Player.query.filter_by(username = player).first().id
    

def get_game_id(player_id):
    '''
    This function gets the id of the current game, which is the last game in the db associated by the user
    '''
    return Game_with_Players.query.filter_by(player=player_id).all()[-1].id
    

def add_songs_to_the_game(game_id, songs):
    '''
    Add randomly selected songs to the current game 
    '''
    for index,song in enumerate(songs):
        db.session.add(Game_with_Songs(game = game_id, song = song, round_numb= index, points = 0))
    db.session.commit()
    

def get_playlist(game_id):
    return Game_with_Songs.query.filter_by(game = game_id).all()


def increase_round_counter(player_id):
    '''
    This function will help us increase the rounds counter in the Game_with_Players table, 
    so we know which song to present next to the player
    '''
    game_id = get_game_id(player_id)
    game = Game_with_Players.query.filter_by(id = game_id).first()
    game.rounds_played += 1
    db.session.commit()
    return game.rounds_played


def set_points_for_round(player_id, current_round, points):
    game_id = get_game_id(player_id)
    song_entry = Game_with_Songs.query.filter_by(game=game_id).filter_by(round_numb=current_round).first()
    song_entry.points = points


def start_playing(player_id):
    '''
    This function starts a new game by creating a new game associated with the user, 
    selects all the songs for this game and sets the number of rounds to 0.
    '''
    
    #Create a new game associated with the user
    add_game(player_id)
    
    #Gets the id of the game
    game_id = get_game_id(player_id)
    
    #Add the songs to the database
    songs = select_songs()
    add_songs_to_the_game(game_id,songs)    
        

# ROUTES

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form['username']
        
        #verify if the user entered a name
        if username:
            if not Player.query.filter_by(username = username).first():
                create_a_player(username)
            
            #if they did, we start the game and redirect to the first song of the game 
            player_id = get_player_id(username)  
            start_playing(player_id)
            game_id = get_game_id(player_id)
            playlist = get_playlist(game_id)
            return redirect(url_for('play_song', player_id=int(player_id), song_number=int(playlist[0].song)))

    return render_template('index.html')


@app.route("/<player_id>/<int:song_number>/", methods=["GET", "POST"])
def play_song(player_id, song_number):
    #Increment the counter of rounds 
    current_round = increase_round_counter(player_id)

    if request.method == "POST":
 
        title_guess = request.form['title']
        artist_guess = request.form['artist']
        
        points = calculate_points(song_number=song_number, title_input=title_guess, artist_input=artist_guess)
        set_points_for_round(player_id=player_id, current_round=current_round, points=points)
        
        #If the number of rounds = 10, we redirect to the result page
        if current_round != 10:
            game_id = get_game_id(player_id)
            playlist = get_playlist(game_id)
            return redirect(url_for('play_song', player_id=int(player_id), song_number=int(playlist[current_round].song)))
        # TO DO : ADD FLASH MESSAGE FOR NEXT PAGE 
        
        #If the number of rounds !=0 we redirect to the next guess 
    
    
    return render_template('playing.html', song = songs_array[song_number]["preview_url"])


if __name__ == "__main__":
    db.create_all()
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)