# Chose a mode of transportation based on the distance (e.g., <3 km : walk, 3-15 km: Bike, >15 km : car).

distance = int(input("Enter the distance : "))

if distance < 3:
    print("Go to Walk")
elif distance >= 3 and distance < 15:
    print("Go with Bike")
else:
    print("Go with car")
