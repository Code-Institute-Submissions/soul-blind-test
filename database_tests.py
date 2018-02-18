import unittest
from flask.ext.testing import TestCase
from data.songs import songs_array as songs_array
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
        increase_round_counter(player_id)
        self.assertEqual(Game_with_Players.query.filter_by(id = game_id).first().rounds_played, 1)
        increase_round_counter(player_id)
        self.assertEqual(Game_with_Players.query.filter_by(id = game_id).first().rounds_played, 2)
        increase_round_counter(player_id)
        self.assertEqual(Game_with_Players.query.filter_by(id = game_id).first().rounds_played, 3)
    
    def test_get_current_round(self):
        create_a_player('michael')
        add_game(get_player_id('michael'))
        player_id = get_player_id('michael')
        game_id = get_game_id(player_id)
        songs = [1]
        add_songs_to_the_game(game_id, songs)
        
        self.assertEqual(get_current_round(player_id), 0)
        increase_round_counter(player_id)
        self.assertEqual(get_current_round(player_id), 1)
        increase_round_counter(player_id)
        self.assertEqual(get_current_round(player_id), 2)


    def test_set_points_for_round(self):
        create_a_player('otis')
        add_game(get_player_id('otis'))
        player_id = get_player_id('otis')
        game_id = get_game_id(player_id)
        songs = [1,2]
        add_songs_to_the_game(game_id, songs)
        
        set_points_for_round(player_id, 0, 1)
        set_points_for_round(player_id, 1, 3)
        
        self.assertEqual(Game_with_Songs.query.filter_by(game=game_id).filter_by(round_numb=0).first().points, 1)
        self.assertEqual(Game_with_Songs.query.filter_by(game=game_id).filter_by(round_numb=1).first().points, 3)
        
    def test_get_total_points(self):
        create_a_player('sam')
        add_game(get_player_id('sam'))
        player_id = get_player_id('sam')
        game_id = get_game_id(player_id)
        songs = [1,2]
        add_songs_to_the_game(game_id, songs)
        
        set_points_for_round(player_id, 0, 1)
        self.assertEqual(get_total_points(game_id), 1)
         
        set_points_for_round(player_id, 1, 3)
        self.assertEqual(get_total_points(game_id), 4)
        
        
    def test_get_result_data(self):
        create_a_player('sam')
        add_game(get_player_id('sam'))
        player_id = get_player_id('sam')
        game_id = get_game_id(player_id)
        songs = [1,2,3,4]
        add_songs_to_the_game(game_id, songs)
        
        
        set_points_for_round(player_id, 0, 1)
        set_points_for_round(player_id, 1, 3)
        
        final_playlist = get_result_data(game_id)
        
        self.assertEqual(len(final_playlist), 4)
        self.assertEqual(final_playlist[0]['points'], 1)
        self.assertEqual(final_playlist[3]['points'], 0)
        self.assertEqual(final_playlist[1]['title'], songs_array[2]['title'])
        self.assertEqual(final_playlist[1]['artist'], songs_array[2]['artist'])
        self.assertEqual(final_playlist[2]['album_img'], songs_array[3]['album_img']['url'])
        
    def test_get_all_user_games_id(self):
        create_a_player('etta')
        player_id = get_player_id('etta')
        add_game(player_id)
        self.assertEqual(get_all_user_games_id(player_id), [1])
        add_game(player_id)
        self.assertEqual(get_all_user_games_id(player_id), [1,2])
        add_game(player_id)
        self.assertEqual(get_all_user_games_id(player_id), [1,2,3])
        
        
    def test_get_summary_points(self):
        create_a_player('sam')
        player_id = get_player_id('sam')
        
        add_game(player_id)
        game_id = get_game_id(player_id)
        songs = [1,2]
        add_songs_to_the_game(game_id, songs)
        set_points_for_round(player_id, 0, 1)
        set_points_for_round(player_id, 1, 3)
        
        self.assertEqual(get_summary_points(1),4)
        
        add_game(player_id)
        game_id = get_game_id(player_id)
        songs = [1,2]
        add_songs_to_the_game(game_id, songs)
        set_points_for_round(player_id, 0, 3)
        set_points_for_round(player_id, 1, 0)
        
        self.assertEqual(get_summary_points(1), 7)
        
    def test_get_all_users(self):
        create_a_player('curtis')
        self.assertEqual(get_all_users(), [1])
        
        create_a_player('percy')
        self.assertEqual(get_all_users(), [1,2])
        
        create_a_player('jackie')
        self.assertEqual(get_all_users(), [1,2,3])
        
        
if __name__ == '__main__':
    unittest.main()