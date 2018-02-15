import unittest
from flask.ext.testing import TestCase
from run import *

class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        db = SQLAlchemy(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_a_player(self):
        create_a_player('mathilde')
        
        self.assertEqual(Player.query.first().username, 'mathilde')
        self.assertEqual(Player.query.first().id, 1)
        
    def test_get_player_id(self):
        create_a_player('aretha')
        
        self.assertEqual(get_player_id('aretha'), 1)
    
    def test_add_game(self):
        create_a_player('sam')
        add_game(get_player_id('sam'))
        
        self.assertEqual(Game_with_Players.query.first().id, 1)
        self.assertEqual(Game_with_Players.query.first().rounds_played, 0) 
        
    def test_get_game_id(self):
        create_a_player('al')
        add_game(get_player_id('al'))
        player_id = get_player_id('al')
        
        self.assertEqual(get_game_id(player_id), 1)
 
    def test_add_songs_to_the_game(self):
        create_a_player('gloria')
        add_game(get_player_id('gloria'))
        player_id = get_player_id('gloria')
        game_id = get_game_id(player_id)
        songs = [1,2,3]
        add_songs_to_the_game(game_id, songs)
        
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[0].song, 1)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[1].song, 2)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[2].song, 3)
        
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[0].round_numb, 0)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[1].round_numb, 1)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[2].round_numb, 2)
        
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[0].points, 0)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[1].points, 0)
        self.assertEqual(Game_with_Songs.query.filter_by(game = game_id).all()[2].points, 0)
        
        
    def test_get_playlist(self):
        create_a_player('roberta')
        add_game(get_player_id('roberta'))
        player_id = get_player_id('roberta')
        game_id = get_game_id(player_id)
        songs = [1,2,3]
        add_songs_to_the_game(game_id, songs)
        
        self.assertEqual(get_playlist(game_id)[0].song, 1) 
        self.assertEqual(get_playlist(game_id)[1].song, 2)
        self.assertEqual(get_playlist(game_id)[2].song, 3) 
    
    def test_increase_round_counter(self):
        create_a_player('otis')
        add_game(get_player_id('otis'))
        player_id = get_player_id('otis')
        game_id = get_game_id(player_id)
        songs = [1]
        add_songs_to_the_game(game_id, songs)
        
        self.assertEqual(Game_with_Players.query.filter_by(id = game_id).first().rounds_played, 0)
        self.assertEqual(increase_round_counter(player_id), 1)
        self.assertEqual(increase_round_counter(player_id), 2)
        self.assertEqual(increase_round_counter(player_id), 3)

    def test_set_points_for_round(self):
        create_a_player('otis')
        add_game(get_player_id('otis'))
        player_id = get_player_id('otis')
        game_id = get_game_id(player_id)
        songs = [1,2]
        add_songs_to_the_game(game_id, songs)
        
        set_points_for_round(game_id, 0, 1)
        set_points_for_round(game_id, 1, 3)
        
        self.assertEqual(Game_with_Songs.query.filter_by(game=game_id).filter_by(round_numb=0).first().points, 1)
        self.assertEqual(Game_with_Songs.query.filter_by(game=game_id).filter_by(round_numb=1).first().points, 3)



if __name__ == '__main__':
    unittest.main()