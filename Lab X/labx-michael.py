#Declaring imports
import random

#Exercise 1 - Control Structures
def firstExercise():
    distance = 1000
    speed = 120
    time = distance/speed
    print(f"\nExercise 1\nTime: {time: .2f} hours")
firstExercise()

#1.1 - Speed Limit

def speedLimit():
    distance = 1000
    speed = 150
    time = distance/speed

    if speed > 120:
        speed = 120
    
    print(f"\nExercise 1.1\nTime: {time: .2f} hours")
speedLimit()

#1.2 - Several Speeds
def severalSpeeds():
    print ("\nExercise 1.2")
    speeds = [80, 100, 120, 140]
    distance = 1000
    for speed in speeds:
        time = distance/speed
        print(f"Speed: {speed} km/h - Time: {time: .2f} hours")
severalSpeeds()


#Exercise 2 - Vectors
def vectorsStart():
    print("\nExercise 2 - Vectors")
    names = ["Ferrari", "Porsche", "Testla", "BMW"]
    speeds = [240, 220, 200, 250]

    for i in range(len(names)):
        print(names[i], speeds[i])
vectorsStart()

#2.3 - Car Information
def carInfo():
    print("\nExercise 2.3 - Car Information")
    names = ["Ferrari", "Porsche", "Testla", "BMW"]
    speeds = [240, 220, 200, 250]
    distance = 1000

    for i in range(len(names)):
        time = distance/speeds[i]
        name = names[i]
        speed = speeds[i]
        print(f"{name} - {speed} km/h. Travel time: {time} hours per 1000 km")
carInfo()

#Exercise 3 - Matrices and Nested Loops
speeds = [
        [120, 130, 140],
        [100, 110, 120],
        [90, 100, 110],
        [130, 140, 150]
    ]

def speedMatrix():
    print("\n Exercise 3 - Matrices and Nested Loops")
    for row in speeds:
        for speed in row:
            print(speed)
speedMatrix()

#3.4 - Display the Matrix
def alignedMatrix():
    print("\n Exercise 3.4 - Display the Matrix")
    for row in speeds:
        print(row)
alignedMatrix()

#3.5 - Average Speed
def averageSpeed():
    speeds = [
        [120, 130, 140],
        [100, 110, 120],
        [90, 100, 110],
        [130, 140, 150]
    ]
    print("\nExercise 3.5 - Average Speed")
    counter = 0
    for row in speeds:
        sum = 0
        counter += 1
        for speed in row:
            sum += speed
        print("Car ", counter, ": ", sum/len(row), "km/h \n")
averageSpeed()

#4 - Functions
def calculate_time(distance, speed):
    time = distance/speed
    return time

def testCalcTime():
    print("\nExercise 4 - Functions")
    time = calculate_time(1000, 120)
    print(f"Time: {time: .2f} hours")
testCalcTime()

#4.6 - Energy
def calculate_energy(distance, energy_rate):
    print("\nExercise 4.6 - Energy")
    energy = distance*energy_rate
    print(f"Energy: {energy: .2f} units")
calculate_energy(1000, 0.08)

#Example 5 - From Functions to Objects
#import random is at the top

class Car:
    def __init__(self, name, max_speed, energy_rate):
        self.name = name
        self.max_speed = max_speed
        self.energy_rate = energy_rate
    
    def run(self, distance):
        speed = random.randint(60, self.max_speed)
        time = distance / speed
        energy = distance * self.energy_rate
        return time, energy


def newFerrari():
    car = Car("Ferrari", 240, 0.08)
    time, energy = car.run(1000)
    print("\nExample 5.0")
    print(f"Time: {time: .2f} hours")
    print(f"Energy: {energy:.2f} units")
newFerrari()

# Questions
# 1. Attributes: name, max speed, energy_rate
# 2. Constructor: __init__(attributes)
# 3. Method: run(self, distance)
# 4. Parameters: self
# 5. returned values: Car

#Exercise 6 - Several Objects
ferrari = Car("Ferrari", 240, 0.08)
porsche = Car("Porsche", 220, 0.09)
tesla = Car("Tesla", 200, 0.05)

cars = [
    ferrari,
    porsche,
    tesla
]

def learnMore():
    print("\nEx6 - Learn more about cars!")
    for car in cars:
        time, energy = car.run(1000)
        print(
        f"{car.name}: "
        f"{time:.2f} hours, "
        f"{energy:.2f} units"
        )
    print("List ended :)")
learnMore()

#Exercise 7 - Create another car
bmw = Car("BMW", 230, 0.07)
cars.append(bmw)

learnMore()

#Exercise 7 - create a race
class Race:
        def __init__(self, cars):
             self.cars = cars
        
        def run(self, distance):
            print("\nLet's start a new race!")
             
            results = []

            for car in self.cars:
                  
                  time, energy = car.run(distance)

                  results.append(
                       (car.name, time, energy)
                  )
            print("The results are: ", results)
            return results

race = Race(cars)

results = race.run(1000)

for name, time, energy in results:
     print(
          f"{name}: "
          f"{time:.2f} hours - "
          f"{energy:.2f} units"
     )

#Exercise 8 - a different race
def raceTwo():
    audi = Car("Audi", 225, 0.07)
    bmw = Car("BMW", 230, 0.07)
    myCars = [audi,bmw]
    raceTwo = Race(myCars)
    raceTwo.run(1000)
raceTwo()


#Exercise 9 - Final Exercise

def finalRace():
    ferrari = Car("Ferrari", 240, 0.08)
    porsche = Car("Porsche", 220, 0.09)
    tesla = Car("Tesla", 200, 0.05)
    bmw =Car("BMW", 230, 0.07)

    cars=[ferrari, porsche, tesla, bmw]
    finalRace = Race(cars)
    finalRace.run(1000)
finalRace()