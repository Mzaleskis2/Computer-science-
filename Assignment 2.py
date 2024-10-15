#12
num = input("Input a number")
num = int(num)
num2 = input("Input a number")
num2 = int(num2)
if num > num2 :
    print(num," is greater than ",num2)
elif num2 > num :
    print(num2," is greater than ",num)
#13
num = 9
num = input("Input a number under 20")
num = int(num)
if num < 20 :
    print("Thank You")
if num == 20 :
    print("Too high")
if num > 20 :
    print("Too high")
#14
num= int(input("Enter a number between 10 and 20: "))
if num >=10 and num <=20:
    print("Thank you")
else:
    print("Incorrect answer")
#15
colour= input("enter your favourite colour: ")
if colour == "red" or colour == "Red" or colour == "RED":
    print("I like red too")
else:
     print("I dont like", colour, "I prefer red")
#16
raining= input("Is it raining?")
text = raining.lower()
if text == "yes":
    windy= input("Is it windy?")
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
#17
age= input("What is your age?")
age= int(age)
if age == 18 or age > 18:
    print("You can vote")
if age == 17:
    print("You can learn to drive")
if age == 16 or age < 16:
    print("You can go trick or-Treating")
#18
num = 1
num = input("Enter a number")
num = int(num)
if num < 10 :
    print("Too low")
if num > 20 :
    print("too high")
if num > 10 and num < 20 :
     print("Thank You")
#19
num = 1
num = input("Enter 1, 2 or 3")
num = int(num)
if num == 1 :
    print("Thank you")
if num == 2 :
    print("Well done")
if num == 3 :
    print("Correct")
if num > 3 :
    print("Error message")

    
    
          