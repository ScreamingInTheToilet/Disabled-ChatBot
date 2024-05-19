Num_ask = int(input('Choose a number'))
# Input asking user for an int number
Sum1 = 0
File = []


for i in range(Num_ask+1):
    File.append(i)
    Sum1 += i
print(Sum1)
Number_Checker = []
# Adding all the numbers from 1 to the chosen number by using for loops.

for i in File:
    if i % 3 == 0:
# The modulus operator check if theres any remainder when i is divided by 3
        Number_Checker.append(i)
    elif i % 5 == 0:
# The modulus operator check if theres any remainder when i is divided by 5
        Number_Checker.append(i)
# Modified version of the above for loop
Sum2 = 0
for i in Number_Checker:
    Sum2 += i
print(Sum2)
