print("Age and Driving")
age = int(input("Enter your age: "))

if age >= 18:
    print("You passed")

    if age >= 70:
        print("You may need a medical check")
    elif age >=18:
        print("You can apply for a driver,s license")

else:
    print("your are too young to drive")

