#Program to determine whether a user is tall enough to ride a rolelrcoaster and how much their ticket should cost
print("Hi, Welcome to the Xtreme Rollercoaster!")
# 1 determine if user is tall enough to ride the rollercoaster using if statement
height = int(input("What is your height in cm? "))
cost = 0
if height >= 120:
    print("You can ride the rollercoaster")
#2 nested if statement to determine how much user should pay for ticket based on their age
    age = int(input("How old are you? "))
    if age < 12:
        cost = 5
    elif age < 18:
        cost = 7
    elif age < 45:
        cost = 12
    elif age > 45:
        cost = 0
#3 multiple if statements - does user want a photo or not - this adds to their total receipt cost
    photo = input("Do you want a photo: Y or N").upper()
    if photo == 'Y':
        cost += 3
#4 total receipt cost
    print(f'Your total receipt is ${cost}')
else:
    print("Sorry you're not tall enough to ride the rollercoaster")
