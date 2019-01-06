num_1 = input('Enter first number:')
num_2 = input('Enter second number:')
num_3 = input('Enter third number:')

def greatest_num(a,b,c):

        if a > b and a > c:
                return a
        elif b > a and b >c :
                return b
        elif c > a and c > b:
                return c
        else:
                return "INVALID"

big_num = greatest_num(num_1,num_2,num_3)

print ("The geratest number is " + big_num)
