def split_string(string):

	list_string = string.split(' ')
	
	return list_string
def join_string(list_string):

	string = '-'.join(list_string)
	
	return string

if __name__ == '__main__':
	string = 'Rohan for Karanjit'
	
	# Splitting a string
	list_string = split_string(string)
	print(list_string)


	# Join list of strings into one
	new_string = join_string(list_string)
	print(new_string)



