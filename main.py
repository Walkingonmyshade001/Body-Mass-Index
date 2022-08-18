#basic calculation 

print(8/3)
print(round(8/3, 2))
print(round(8/3, 3))
print(round(8/3))
print(8//3)

print()

height = float(input("Enter your height in m \n"))
weight = float(input("Enter your weight in kg \n"))
bmi = weight / (height**3)
BMI = round(bmi)
print(BMI)
