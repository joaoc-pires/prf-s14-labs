class Movie:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration

    def describe(self):
        return f"{self.title} ({self.year}) - {self.duration} minutes"

class Cinema:
    def __init__(self, name, movies):
        self.name = name
        self.movies = movies

    def show_movies(self):
        for movie in self.movies:
            print(movie.describe())
    
    def number_of_movies(self):
        return len(self.movies)

movies = [
    Movie("Dune", 2024, 166),
    Movie("Avatar", 2022, 192),
    Movie("Inception", 2010, 148)
]
cinema = Cinema("Central Cinema", movies)
cinema.show_movies()

movies2 = [
    Movie("Oppenheimer", 2024, 300),
    Movie("Interstellar", 2016, 3002)
]
cinema2 = Cinema("Old Town Cinema", movies2)
cinema.show_movies()