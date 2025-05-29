from enum import Flag
class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16

class Movie:
    def __init__(self, name: str, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre: MovieGenres):
        return genre in self.genres
    
    def __str__(self):
        return self.name
