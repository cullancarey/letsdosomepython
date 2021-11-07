##This will go over for loops. Basic concept that I use a lot

##for loop
##we'll start with a list of numbers from 1-10 and then loop over them.
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
	print(number)

##In the above, num represents the an interator which goes on by one through the list. 
##Basically, "for each number in numbers (the list), print the number"


##while loop
##we'll use the same list from 1-10"

numbers = [1,2,3,4,5,6,7,8,9,10]

number = 0
while number < len(numbers):
	number+=1
	print(number)

##A while loop does not iterate over the list like the for loop does.
##A while loop does something until a condition is met. 
##In this while loop, it prints the variable number until 
##the number is not less than the length of the list. 
##So it prints 1-10 just like the for loop above. 