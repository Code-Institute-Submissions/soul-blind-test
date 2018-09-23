# The Vintage Blindtest

This is a blind test game that allows you to test your knowledge of vintage soul songs.
 
## UX
 
This website is obviously for people who like old soul songs, otherwise it may be hard to play. 
The typical user would be a music lover who wants to try or prove his knowledge, or someone who likes this kind of music and wants to discover some songs.

The mockups can be found [here](https://github.com/mathilde206/soul-blind-test/blob/master/Mockups%20Soul%20Blind%20Test.pdf)

## Features
 
### Existing Features

- Use the API from spotify to create the songs data ([get_songs.py](https://github.com/mathilde206/soul-blind-test/blob/master/data/get_songs.py))
- Record users and their scores
- The game: show a random song, take guesses, calculate the points, keep track of the result
- The leaderboard: show the top ten players 

### Features Left to Implement
- Accept answers that are 80% correct
- Contact form: send me an email

## Technologies Used

- [Flask](http://flask.pocoo.org/)
    - I use **Flask** to handle page routing and other backend functions
- [SQL Alchemy](https://www.sqlalchemy.org/) and [SQLite](https://www.sqlite.org) 
    - I use **SQL Alchemy** and **SQLite** for the database and db queries
    - Note: the website is deployed on heroku with a SQLite database. SQLite databases are currently not supported by Heroku meaning that the data is deleted after a few hours.
- [Bootstrap 4](http://getbootstrap.com/)
    - I use **Bootstrap** to give the project a simple, responsive layout
- [Spotipy](http://spotipy.readthedocs.io/en/latest/)
    - I use **Spotipy** to get the data from Spotify.


## Testing
- The functions related to the database are tested in database_test.py
- The other python functions are tested in tests.py
- Documentation for the user testing can be found there : [User Tests](https://github.com/mathilde206/soul-blind-test/blob/master/user_testing.pdf)

## Deployment

### Local
1. Firstly you will need to clone this repository by running the ```git clone https://github.com/mathilde206/soul-blind-test``` command
2. Then you need to install all the dependencies from the requirements.txt file:
  ```
  pip install -r requirements.txt

  ```
3. To start the application : ```python3 run.py```

### Production
The website is deployed on heroku at [vintage-blindtest.herokuapp.com](http://vintage-blindtest.herokuapp.com/)
To deploy, I included two environment variables : IP: 0.0.0.0 and PORT: 5000

## Credits

### Media
- The music extracts come from Spotify through spotipy.
- The background image comes from Unsplash from Mr Cup / Fabien Barral on Unsplash (Free of rights)
