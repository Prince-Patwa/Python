# Convert minutes into hours and minutes (e.g., 135 mins ? 2 hr 15 min).

min = int(input("Enter the value of minutes : "))

hr = min//60
minutes = min%60

print("Conterted value in Houre and minutes, who's given by you.")
print(hr,"Hours",minutes,"Minutes")