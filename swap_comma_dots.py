def Replace(str1):
	maketrans = str1.maketrans
	final = str1.translate(maketrans(',.', '.,', ' '))
	return final.replace(',', ", ")


string = "14, 625, 498.002"
print(Replace(string))

