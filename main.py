print("Welcome to the rollercoaster!!\n")
height = int(input("What is your height in cm??\n"))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster!!\n")
	age = int(input("What is your age?\n"))
	if age <= 12:
		bill = 5
		print("Child tickets are $5.")
		
	elif age <= 18:
		bill = 7
		print("Youth tickets are $7.")
		
	elif age >= 45 and age <=55:
		bill = 0	
		print("Adults beteewn 45 - 55 pay $0")
		
	else:
		bill = 12
		print("Adult tickets are $12.\n")
		
	wants_photo = input("Do you want a photo taken? Y or N. \n")
	if wants_photo == "Y":
		bill += 3 #+= is the same as bill = bill + 3
		
	print(f"Your final bill is ${bill}")
else:
	print("Sorry, you have to grow taller before you can ride.")