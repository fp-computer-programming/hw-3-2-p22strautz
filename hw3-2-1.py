# Author: SCT (ADMG) 9/29/21

grade = int(input("What is your grade number?\n"))

if grade >= 93:
    print("You have an A.")
elif grade >= 90:
    print("You have an A-")
elif grade >= 87:
    print("You have a B+")
elif grade >= 83:
    print("You have a B")
elif grade >= 80:
    print("You have a B-")
elif grade >= 77:
    print("You have a C+")
elif grade >= 73:
    print("You have a C")
elif grade >= 70:
    print("You have a C-")
elif grade >= 65:
    print("You have a D+")
elif grade >= 60:
    print("You have a D")
else:
    print("You have an F")
