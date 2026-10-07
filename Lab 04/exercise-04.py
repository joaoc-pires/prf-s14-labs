tickets = [
    [80, 75, 90],
    [60, 70, 65],
    [100, 95, 90],
    [50, 55, 60]
]

for row in tickets:
    row_values = ""
    for session in row:
        row_values = row_values + " " + str(session)
    row_values = row_values[1:]
    print(row_values)