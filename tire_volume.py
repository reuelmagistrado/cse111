# Gets the current date from the computer's operating system.
# import math module
from datetime import datetime
import math

# Gets the current date from the computer's operating system.
current_date = datetime.now()

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = round(math.pi*tire_width**2*aspect_ratio*(tire_width*aspect_ratio+2540*wheel_diameter)/10_000_000_000, 2)


if tire_width <= 155 and aspect_ratio <= 50 and wheel_diameter <= 15:
    price = 150
    print(f"\nPrice: ${price}")
elif tire_width <= 215 and aspect_ratio <= 80 and wheel_diameter <= 20:
    price = 250
    print(f"\nPrice: ${price}")
elif tire_width <= 285 and aspect_ratio <= 95 and wheel_diameter <= 24:
    price = 350
    print(f"\nPrice: ${price}")
else:
    price = 450
    print(f"\nPrice: ${price}")

print(f"The approximate volume is {tire_volume} liters")
answer = input((f"\nDo you want to buy the tire {tire_width}/{aspect_ratio} R{wheel_diameter} (yes/no)? "))

if answer.lower() == "yes":
    phone_number = input("Please enter your phone number: ")

    # Opens a text file named volumes.txt for appending.
    # Appends to the end of the volumes.txt file one line of text that contains the following five values:
    # current date, width of the tire, aspect ratio of the tire, diameter of the wheel, volume of the tire, phone number

    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date:%Y-%m-%d}, {tire_width}, {aspect_ratio}, {wheel_diameter}, {tire_volume}, {phone_number}", file=volumes_file)

    print("\nThank you for choosing our product!")

elif answer.lower() == "no":
    print("\nThank you for visiting us!")

else:
    print("\nInvalid Answer!")
