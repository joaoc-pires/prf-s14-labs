speeds = [80, 100, 120, 140]
distance = 1000 #kms

for speed in speeds:
    average = distance / speed
    print(f"Speed: {speed} km/h - Time: {average} hours")


# Speed: 80 km/h - Time: 12.50 hours
# Speed: 100 km/h - Time: 10.00 hours
# Speed: 120 km/h - Time: 8.33 hours
# Speed: 140 km/h - Time: 7.14 hours