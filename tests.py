import unittest
from data.songs import songs_array as songs_array
from run import select_songs, answer_is_correct, calculate_points

class Test_blind_test(unittest.TestCase):
    
    def test_select_random_songs(self):
        '''
        This test verifies that 10 songs' indexes are selected 
        and that they are in the songs_array.
        '''
        self.assertEqual(len(select_songs()),10)
        for track in select_songs():
            self.assertLessEqual(track,len(songs_array))
    
    def test_is_correct(self):
        song_number = 0
        user_input = songs_array[0]['title']
        title = 'title'
        self.assertTrue(answer_is_correct(user_input, song_number, title))
        
        #also works with different capital letters
        self.assertTrue(answer_is_correct(user_input.upper(), song_number, title))
        
        #also works with the artist
        user_input = songs_array[0]['artist']
        artist = 'artist'
        self.assertTrue(answer_is_correct(user_input.upper(), song_number, artist))
        
        #is false when the title is different
        user_input = songs_array[1]['title']
        self.assertFalse(answer_is_correct(user_input, song_number, title))
    
    def test_calculate_points(self):
        song_number = 0
        correct_title = songs_array[0]['title']
        wrong_title = 'Au Clair de La Lune'
        correct_artist = songs_array[0]['artist']
        wrong_artist = 'Britney Spears'
        
        # 1 point if the artist is correct but the title is false 
        self.assertEqual(calculate_points(song_number, wrong_title, correct_artist), 1)
        
        # 1 point if the title is correct but the artist is false 
        self.assertEqual(calculate_points(song_number, correct_title, wrong_artist), 1)
        
        # 1 point if the artist is correct but the title is none  
        self.assertEqual(calculate_points(song_number, None, correct_artist), 1)
        
        # 1 point if the title is correct but the artist is none  
        self.assertEqual(calculate_points(song_number, correct_title, None), 1)
        
        # 3 points if both the title and the artist are correct 
        self.assertEqual(calculate_points(song_number, correct_title, correct_artist), 3)
        
        # 0 points if both the title and the artist are wrong 
        self.assertEqual(calculate_points(song_number, wrong_title, wrong_artist), 0)
        
        # 0 points if both the title and the artist are wrong 
        self.assertEqual(calculate_points(song_number, None, None), 0)