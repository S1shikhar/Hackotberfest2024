import math

def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))

test_number = 96696.

print ("The original number is : " + str(test_number))

res = test_number == rev(test_number)
print ("Is the number palindrome ? : " + str(res))
