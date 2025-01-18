
# creating of variables ,initilizing the variables.printing the type of the variable
# name="skill city"
# print(type(name))
# name=2025
# print(type(name))

# print("hello Word")-print statement
# var=10 # variable declaration and initalization assinment statement

# operators
# print(5+2)
# print(5*2)
# print(5*2/3*2-5*5+5/2)
# print(2_22_222_000)

# a=bool(0)
# print(a)
# a=int(100)
# print(a)
# a=float(100)
# print(a)
# a=str(100)
# print(a)

# string concatination
# firstName = "stela"
# lastName = "valkova"
# print(firstName.upper() +" "+ lastName.lower())
# print(firstName[-1:-3])
# print(firstName[::-1])

#comparison operator
# num=1
# num1=2
# print(num1 ==num)


#logical AND(all the conditions must be true to proceed) OR(onlyone conditiond need to be true to proceed) NOT(reverse)
# firstname
# AND
# lastName

# mobilephone
# OR
# phonenumber

#conditionals statements
# email = "abv@gmail.com"
# password = "1234566"

# #login     - in different language &&= AND    
# if email == "abv@gmail.com" and password =="1234566":
#     print("welcome")
# else:
#     print("sorry your password and or email are not correct")



# if conditions:
#     statemnents
# elif conditions:
#     statement
#     else:
#         statements

# number = int(input("Enter a number "))
# print(number)
# if number % 2 == 0:
#     print("your number is even")
# else:
#     print("your number is odd")

# salary = int(input("What is your salary "))
# x = salary
# print(x)
# expirience = int(input ("Which year you've started work "))
# y = expirience
# print(y)
# bonus = 0.07*y
# if y > 2022:
#     print("no bonus") 
# else:
#     print(bonus)

# fruit = ["banana","apple","cherry","apple","banana"]
# # print(fruit[2])
# # print(len(fruit))
# fruit.remove("banana")
# print(fruit)

# fruit=("banana","leno","rapes")
# print(type(fruit))

# listOfFruit = list(fruit)


# listOfFruit.append( "orange")
# fruit = tuple(listOfFruit)
# print(fruit)
# fruit={"apple", "banana", "Cherry"}
# fruit.add("kivi") - make a tuple first
# print(fruit)


# users = {
#   "user1":   {
#         "firstName": "Jane",
#         "lastName": "Doe",
#         "phoneNumber": "1234567890",
#         "email": "lorem@gmail.com",
#         "address": "123, Lorem Ipsum",
#     },
#    "user2": {
#         "firstName": "John",
#         "lastName": "Doe",
#         "phoneNumber": "1234567890",
#         "email": "abc@mail.com",
#         "address": "123, Lorem Ipsum"
#     }
# }

# print(users["user1"]["firstName"])
# print(users.get("user1").get("lastName"))



# data_type = input("Enter the data collection type (list, set, or dictionary): ").lower()


# if data_type == "list":
#     print([1, 2, 3])
# elif data_type == "set":
#     print({1, 2, 3})
# elif data_type == "dictionary":
#     print({"key1": 1, "key2": 2, "key3": 3})
# else:
#     print("Invalid data collection type.")

# x = 1
# for i in range(1,5):
    # x *= i
    # print(x) 
      
      
#       myFirstName = "Muhammed"
# for character in myFirstName:
#     print(character)
# myList = [1,2,3,4,5,6,7,8,9,10]
# for number in myList:
#     print(number)
# mySet = {1,2,3,4,5,6,7,8,9,10}
# for number in mySet:
#     print(number)
# myTuple = (1,2,3,4,5,6,7,8,9,10)
# for number in myTuple:
#     print(number)


# for i  in range (1,51):
#      if i == 5 :
#         continue
    
# print(i)
       
       
        
# answer = input("What is your favorite country? Bulgaria,France,Spain or Italy  ?")     
# countries = ["Bulgaria","France","Spain","Italy"]
# for  i in countries:
#          print(i)
# if countries[2]== "Spain":
#             print("Yaay Spain is 3rd in your list of favourite countries")
# else:
#             print("Boo,I can't believe Spain isn't your 3rd favourite country!")
           
           
           
# myName = "STELA"
# for char in myName[:: -1]:
#    print(char)


# myName ="STELA"
# reversedName ="ALETS"
# for char in reversedName:
#     print(char)


# for char in myName:
#     if char == myName[1]:
#         print(char)

# import random



# targetNumber = 6
# guess = random.randint(0,6)
# count =1

# # if guess == targetNumber:
    
# while guess != targetNumber:
#         print("sorry")
#         guess= random.randint(0,6)
#         print("Guess")
#         count += 1

# print("you got",count)


import random

targetNumber = 6
guess = random.randint(0, 750)
counter = 1
# Comparison Operator != means not equal to == means equal to
while guess != targetNumber:
    print("Sorry, that's not it.")
    counter += 1 # Increment the counter
    guess = random.randint(0, 750)
    print("Guess again as your guess was ",guess)
    
    
print("You got it after ",counter," tries!")