weight = int(input("Your body weight: "))
unit = input("L for lbs OR K for kg: ")


if unit.upper() == "K":
    print(f"Your weight is {weight} kg")
elif unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} lbs")
else:
    print(f"Your weight is {weight}")
