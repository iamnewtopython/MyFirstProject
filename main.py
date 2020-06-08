#Week 4

#Make code that shows if number is divisible by 3, say Fizz. If number is divisible by 5, say Buzz. If number is divisible by 3 and 5, say Fizz Buzz. If divisibl by neither, say Oops.

'''number = int(input('Enter a number: '))
if number % 3 == 0 and number % 5 == 0:
  print('Fizz Buzz') 
elif((number % 3 == 0)):
 print('Fizz')
elif ((number % 5 == 0)):
  print('Buzz') 
else:
  print('Oops')   


  for x in range(1,11):
    if x % 2 == 0:
      pass
    else:
      print(x) 

    #pass is a statement that will do nothing

for x in range(100):
    if x % 10 == 0:
        continue
    print(x)    
    print ('Done') 

#continue is to continue to the next iteration of a loop 

for x in range(1,100):
    if x % 10 != 0:
        continue
    print(x)    
    print ('Done') 

for x in range(100):
    pass
print ('Done')     

for x in range(100):
    continue
print ('Done')  

#fibonacci sequence with limited numbers

nterms = int(input("How many terms? "))

# first two terms
n1=0
n2=1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence up to",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1'''

#Homework 
  #Write code for Pascal's Triangle
  #ask for max count and show first n prime numbers
  #Ask for input . . .and say if number is prime or not.
  
# taking input from user
number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")    

