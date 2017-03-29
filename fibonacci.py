'''Python Programe to print fibonacci numbers from 1 to n
	 "Buzz" when F(n) is divisible by 3.
	 "Fizz" when F(n) is divisible by 5.
	 "FizzBuzz" when F(n) is divisible by 15.
	 "BuzzFizz" when F(n) is prime.
	 the value F(n) otherwise.
	Author: Nisarg Pandya (nisargypandya@gmail.com)
'''
#Get two numbers from the user for the range. Two numbers are used for custom range example: 20 - 20000000
def fibo():
	print "Program to print fibonacci numbers"
	print '"Buzz" when F(n) is divisible by 3'
	print '"Fizz" when F(n) is divisible by 5'
	print '"FizzBuzz" when F(n) is divisible by 15'
	print '"BuzzFizz" when F(n) is prime'
	print 'The value F(n) otherwise'
	#Get input from user, if input is not a positive integer, ask again for input from the user.
	while True:
		endNumber = raw_input("Enter the end number here: ")
		if endNumber >= 0 and endNumber.isdigit() == True: 
			break
		else:
			print "Please provide positive integers only!!"
			endNumber = raw_input("Enter the end number here: ")

	#Function to check if the number is prime
	def isPrime(n):
		if n is 0: return False
		if n < 2: return False
		for i in range(2,int(n**0.5)+1):
			if n%i==0:
				return False
		return True

	#Local variables for generating the fibonacci sequence operation
	a,b=0,1
	#Loop to generate fibonacci sequence along with requested prints
	while(a <= int(endNumber)):
		if a > 0 and a%15 is 0:
			print "FizzBuzz",
		elif a > 0 and a%3 is 0:
			print "Buzz",
		elif a > 0 and a%5 is 0:
			print "Fizz",
		elif a > 0 and isPrime(a):
			print "BuzzFizz",
		else:
			print a,
		a,b=b,a+b

if __name__ == '__main__': 
	fibo()