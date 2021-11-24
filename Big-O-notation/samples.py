

from pprint import pprint

def fibonacci(n: int) ->int:
	
	n1 = 1  #O(1)
	n2 = 1  #O(1)
	cumulator = 0  #O(1)

	if n <= 1: #O(1)
		print(n) #O(1)
	else: #O(1)
		for _ in range(n-2): #O(n)

			cumulator = n1 + n2  #O(1)
			n1, n2 = n2, cumulator #O(1)

		print(cumulator)#O(1)
	
        #T(n)=1+1+1+(n*(1+1))+1
	#T(n)=3+2n+1
	#T(n)=4+2n //

'''def is_prime(n: int) -> bool:
        
	if n < 2:
                return False

	for x in range(2, n):
		if n % x == 0:
			return False
	return True'''
        



def main():
	
	limit = 4         #O(1)
	for x in range(limit+1):  #O(n)*(O(1))
		print(" "*(limit - x), "*"*x)

        #T(n)=1+n //

	fibonacci(1)
	fibonacci(7)
	fibonacci(5)


	

	n = 18  #O(1)
	if n == 1:  #O(1)
		print(1) #O(1)

		#O(1)+(O(1)*O(1))

	number = lambda n: (2*n -3) #O(1)
	print(number(8))

	#T(n)=1+(1*1)+1
	#T(n)=3


'''
	print(is_prime(37))'''


# 0 1 1 2 3 5 8 13 21 34 
if __name__ == "__main__":
	main()
