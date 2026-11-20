import math
num1 = float(input("enter the value needed to be converted? "))


print("What do you wnat to convert in? ")
print("1. Degrees → Radians ")
print("2. Radians → Degrees")
print("3. m/s → km/h")
print("4. km/h → m/s")
print("5. Wheel RPM → linear speed (m/s)")

query = int(input("Enter the operation numnber? "))

if query== 1:
    conversion1 = num1 * (math.pi/180)
    print(f"{conversion1:.3f} radians")
elif query == 2:
    conversion2 = num1 *(180/math.pi)
    print(f"{conversion2:.3f} degrees")
elif query == 3:
    convo3 = num1 * 3.6
    print(f"{convo3:.3f} km/hr")
elif query == 4:
    convo4= num1 / 3.6
    print(f"{convo4:.3f} m/s")
elif query == 5:
    radius = float(input("whats the radius? "))
    convo5 = num1 * (2 * math.pi) * radius / 60
    print(f"{convo5:.3f} m/s")
else:
    print("invalid choice")