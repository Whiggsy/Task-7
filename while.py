# calculate the average of a series of numbers entered by user

# variables
total = 0
counter = 0
number = 0

# while -1 isnt entered this loop runs
while not number == -1:
    number = int(input("Input any number to find the average of a series of numbers '-1' ends\n"))
    total += number
    counter += 1
    
average = (total + 1) / (counter - 1)

print(f"Average of your numbers is {average}")