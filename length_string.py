# Returns length of string
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "rohan"
print(findLen(str))

# Returns length of string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
 
str = "rohan"
print(findLen(str))

# Python code to demonstrate string length 
# using for loop

# Returns length of string
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter


str = "rohan"
print(findLen(str))

