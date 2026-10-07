class Movie:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration

    def describe(self):
        return f"{self.title} ({self.year}) - {self.duration} minutes"

# Questions
# Identify in the code:
# 1. the class; Movie
# 2. the constructor; __init__
# 3. the attributes; title; year, duration
# 4. the method; describe
# 5. the parameters of the constructor; title; year, duration
# 6. the value returned by describe(). the title, year, and duration, human readable

movies = [
    Movie("Dune", 2024, 166),
    Movie("Avatar", 2022, 192),
    Movie("Inception", 2010, 148),
    Movie("O Sol a tremer de frio numa noite de tempestade", 2000, 169)
]
for movie in movies:
    print(movie.describe())