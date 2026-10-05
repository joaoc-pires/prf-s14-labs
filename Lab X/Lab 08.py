
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

ferrari = Car("Ferrari", 240, 0.08)
porsche = Car("Porsche", 220, 0.09)
tesla = Car("Tesla", 200, 0.05)
new_car = Car("BMW",230,0.07)

cars = [
    ferrari,
    porsche,
    tesla,
    new_car
]

for car in cars:
    time, energy = car.run(1000)
    print(
        f"{car.name}: "
        f"{time:.2f} hours, "
        f"{energy:.2f} units"
    
    )

