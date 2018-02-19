# The Vintage Blindtest
 
## Overview

### What is this app for?
 
This is a blind test game that allows you to test your knowledge of vintage soul songs. 
 
### What does it do?
It selects 10 random songs in a preselected playlist, and presents them to the user who can try to make a guess. 


### How does it work
1. the player enters his username 
2. he is then redirected to the first page where he hears a 30 seconds extract from a randomly chosen song and can make a guess. If the guess is right, he gets some points (1 for correct title or correct artist, 3 points for both). 
3. once the player makes a guess he is redirected to the next song x10 times 
4. After 10 rounds,the player can see his overall result and the songs he got right. 
The user can also view the leaderboard. 

## Features

### Existing Features

-General Features
  - Use the API from spotify to create the songs data 
  - Record users and their scores
  - The game: show a random song, take guesses, calculate the points, keep track of the result
  - The leaderboard: show the top ten players
  - Contact form: send me an email 

### Features to Implement

- Nice to have: 
  - user experience: 
    - accept answers that are 80% correct
  - Contact form: send me an email
 
## Tech Used
### Some the tech used includes:
- [Flask](http://flask.pocoo.org/)
    - I use **Flask** to handle page routing and other backend functions
- [SQL Alchemy](https://www.sqlalchemy.org/) and [SQLite](https://www.sqlite.org) 
    - I use **SQL Alchemy** and **SQLite** for the database and db queries
- [Bootstrap 4](http://getbootstrap.com/)
    - I use **Bootstrap** to give the project a simple, responsive layout
- [Spotipy](http://spotipy.readthedocs.io/en/latest/)
    - I use **Spotipy** to get the data from Spotify.
 

## Testing
- The functions related to the database are tested in database_test.py
- The other python functions are tested in tests.py

## Contributing
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone https://github.com/mathilde206/soul-blind-test``` command
2. Then you need to install all the dependencies from the requirements.txt file:
  ```
  pip install -r requirements.txt

  ```
3. To start the application : ```python3 run.py```
4. Make changes to the code and if you think it belongs in here then just submit a pull request

### Add more songs 
If you feel one artist is missing from the playlist and should be added in this game, feel free to ask me. 