input_num = int(input('Enter a number'))

def num_of_digts(num):
	count = 0
	while num > 0:
		num = num // 10
		count = count + 1
	print (count)
	
(num_of_digts(input_num))



