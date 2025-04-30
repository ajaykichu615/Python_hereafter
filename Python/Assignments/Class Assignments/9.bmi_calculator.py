"""Write a program that calculates the BMI of a person based on their height and weight.
Based on the bmi value, classify the person into one of the following categories:
below 18.5-- under weight
18.5-24.9--normal weight
25-29.9--overweight
30-34.9--obesity class I
35-39.9--obesity class II
40 and above--obesity class III"""

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f'Your BMI is {bmi}')
if bmi < 18.5:
    print("under weight")
elif 18.5 <= bmi <= 24.9:
    print("normal weight")
elif 25 <= bmi <= 29.9:
    print("overweight")
elif 30 <= bmi <= 34.9:
    print("obesity class I")
elif 35 <= bmi <= 39.9:
    print("obesity class II")
else:
    print("obesity class III")

