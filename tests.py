import unittest
from data.songs import songs_array as songs_array
from run import select_songs

class Test_blind_test(unittest.TestCase):
    
    def test_select_random_songs(self):
        '''
        This test verifies that 10 songs' indexes are selected 
        and that they are in the songs_array.
        '''
        self.assertEqual(len(select_songs()),10)
        for track in select_songs():
            self.assertLessEqual(track,len(songs_array))
