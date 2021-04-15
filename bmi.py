
weight = float(input("Enter Weight: "))
height = float(input("Enter Height: "))

BMI = weight / (height * height)

if BMI < 18.5:
    print("Underweight")

elif 18.5 <= BMI <= 24.9:
    print("Normal")

elif 25 <= BMI <=29.9:
    print("Overweight")

elif 30 <= BMI <=34.9:
    print("Obese")

elif 35 >= BMI:
    print("Extremelyobese")
    