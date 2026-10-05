speeds = [
        [120, 130, 140],
        [100, 110, 120],
        [90, 100, 110],
        [130, 140, 150]
    ]

def speedMatrix():
    for row in speeds:
        for speed in row:
            print(speed)
speedMatrix()

def alignedMatrix():
    for row in speeds:
        print(row)
alignedMatrix()

def averageSpeed():
    print("Äverage speed")
    for i in range(len(speeds)):
        sum = 0
        for j in range(len(speeds[i])):
            sum += speeds[i][j]
        lenSpeed = len(speeds[i])
        print("Car ", i+1,": ", sum/lenSpeed," km/hour. \n")
averageSpeed()