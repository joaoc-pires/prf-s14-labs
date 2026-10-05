import random

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

class Race:
    def __init__(self, cars):
        self.cars = cars
        
    def run(self, distance):
        results = []
        for car in self.cars:
            time, energy = car.run(distance)
            results.append(
                (car.name, time, energy)
            )
        return results

cars = [
    Car("Ferrari", 240, 0.08),
    Car("Porsche", 220, 0.09),
    Car("Tesla", 200, 0.05),
    Car("BMW", 230, 0.07)
]

race = Race(cars)
results = race.run(1000)
for name, time, energy in results:
    print(
        f"{name}: "
        f"{time:.2f} hours - "
        f"{energy:.2f} units"
    )
# 1. the attributes of a car; name, max_speed, energy_rate
# 2. the constructor; init
# 3. the method; run
# 4. the parameters; name, max_speed, energy_rate, distance
# 5. the returned values. time, energy

