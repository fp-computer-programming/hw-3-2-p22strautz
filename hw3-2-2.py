# Author: SCT (ADMG) 9/29/21

Height = int(input("What is your height?\n"))

Weight = int(input("What is your weight?\n"))

BMInum = Weight / (Height ** 2)

if BMInum < 19:
    print("You are underweight")
elif BMInum < 25:
    print("You are Healthy")
elif BMInum < 30:
    print("You are overweight")
elif BMInum < 40:
    print("You are obese")
elif BMInum >= 40:
    print("You are extremely obese")
