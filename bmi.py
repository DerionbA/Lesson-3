height = float(input("enter your height "))
weight= float(input("enter your weight "))

bmi = weight / (height/100)**2
print("Your BMI is" , bmi)
if bmi <= 18.4:
    print("You are underweight ")
elif bmi <=24.9:
    print("You are healthy")
elif bmi <=29.9:
	print("You are Over weiht")
elif bmi <=34.9:
	print("You are severely over weight")
elif bmi <=39.9:
	print("You are Obese")
else:
	print("you are severely obese")





