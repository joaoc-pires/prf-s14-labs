tickets = [
    [80, 75, 90],
    [60, 70, 65],
    [100, 95, 90],
    [50, 55, 60]
]

for i in range(len(tickets)):
    movie_average = 0
    for session in tickets[i]:
        movie_average += session
    movie_average = movie_average / len(tickets[i])
    print(f"Movie {i + 1}: {round(movie_average, 2)}")
    