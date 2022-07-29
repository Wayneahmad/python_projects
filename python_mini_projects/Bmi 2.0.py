
print("Welcome to the BMI Generator 2.0\n")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

print("\nYour results")
if bmi < 18.5:
    print(
        f"Your BMI is {bmi}. which means you are underweight, you need some food ASAP!!")
elif bmi <= 25:
    print(f"Your BMI is {bmi}. You have a normal weight, Well done :)")
elif bmi <= 30:
    print(
        f"Your BMI is {bmi}. You are above average.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}. You are really overweight.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")
