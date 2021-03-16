height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = weight / (height**2)
if BMI < 18.5:
    print("Your BMI is "+str(BMI)+", You are underweight")
elif BMI > 18.5 and BMI < 25:
    print("Your BMI is "+str(BMI)+", You have normal weight")
elif BMI > 25 and BMI < 30:
    print("Your BMI is "+str(BMI)+", You are overweight")
elif BMI > 30 and BMI < 34.9:
    print("Your BMI is "+str(BMI)+", You are Obese (Class 1)")
elif BMI > 35 and BMI < 39.9:
    print("Your BMI is "+str(BMI)+", You are Severely Obese (Class 2)")
elif BMI > 40 and BMI < 49.9:
    print("Your BMI is "+str(BMI)+", You are Morbidly Obese (Class 3)")
elif BMI > 50:
    print("Your BMI is "+str(BMI)+", You are Super Obese (Class 4)")
