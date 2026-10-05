name = "Ferrari"
max_speed = 240
energy_rate = 0.08

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

car = Car("Ferrari", 240, 0.08)
time, energy = car.run(1000)
print(f"Time: {time:.2f} hours")
print(f"Energy: {energy:.2f} units")


# 1. the attributes of a car; name, max_speed, energy_rate
# 2. the constructor; init
# 3. the method; run
# 4. the parameters; name, max_speed, energy_rate, distance
# 5. the returned values. time, energy

