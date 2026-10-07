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

class Movie3D(Movie):
    def __init__(self, title, year, duration, glasses_required):
        super().__init__(title, year, duration)
        self.glasses_required = glasses_required
    
    def describe(self):
        if self.glasses_required: 
            return f"{self.title} ({self.year}) - 3D (Glasses needed) - {self.duration} minutes"
        else:
            return f"{self.title} ({self.year}) - 3D (Glasses NOT needed) - {self.duration} minutes"


class MovieIMAX(Movie):
    def __init__(self, title, year, duration, screen_width):
        super().__init__(title, year, duration)
        self.screen_width = screen_width
    
    def describe(self):
        return f"{self.title} ({self.year}) - IMAX {self.screen_width} meters screen - {self.duration} minutes"

movies = [
    Movie("Inception", 2010, 148),
    Movie3D("Avatar", 2022, 192, True),
    Movie3D("Avatar: The Way of Water", 2024, 192, False),
    MovieIMAX("Oppenheimer", 2023, 180, 24),
    MovieIMAX("Oppenheimer", 2023, 180, 32)
]

for movie in movies:
    print(movie.describe())

# Questions
# 1. Which class is the parent class? Movie
# 2. Which classes inherit from Movie? Movie3D & MovieIMAX
# 3. Which attributes are inherited? Title, year, duration
# 4. What does super() do? calls the method in the superclass, in this case Movie
# 5. Why can the same for loop call describe() on all three objects? Because all objects have the same method, also defined in the super class, just overriden in the children
# The Cinema manages a collection of movie objects, while Movie3D and MovieIMAX demonstrate how specialised classes can inherit from a general Movie class.
