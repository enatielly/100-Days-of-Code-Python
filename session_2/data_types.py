# #Data Types

# #Strings

# print("Hello"[4])

# #Integer

# print(123 + 345)

# #Float

# 3.14159

# #Boolean
# True
# False

# #strings x integer
# num_char = len(input("What's your name?"))
# # print(type(num_char))

# new_num_char = str(num_char) #turns int in str

# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))

 
#PEMDAS
# ()
# **
# *
# /
# +
# -

#print(3 * (3 + 3) / 3 - 3)

# print(round(1/3, 2))

# print(4 / 2)
# print(type(4 / 2))

# print(4 // 2)
# print(type(4 // 2))

# result = 4 / 2
# result /= 2
# print(result)


score = 0

# User scores a point
# score = score + 1 #same
score += 1 #same

height = 1.8
isWinning = True

print(score)

print("your score is " + str(score))

#f-String

print(f"your score is {score}")

print(f"your score is {score}, your height is {height}, and you are winning is {isWinning}")