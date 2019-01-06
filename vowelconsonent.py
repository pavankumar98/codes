input_num = input()
input_num = input_num.lower()

vowels = ['a','e','i','o','u']
consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

if (input_num in vowels):
        print("vowel")

elif (input_num in consonents):
        print("consonent")
else:
	print("invalid")
