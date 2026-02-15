# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
dist = input("Enter distance: ")
dist_in_int = int(dist)
if (dist_in_int < 3):
        print("Walk")
elif (dist_in_int >= 3 and dist_in_int < 15):
        print("Bike")
else : print("Car")
