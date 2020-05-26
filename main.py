#Week 3
#Comparison Operators

#> (Greater than)
#< (Less than)
#>= (Greater than equal to)
#<= (Less than equal to)
#= (Assignment Operator)
#== (Equal to)
    #result of operators is always Boolean (True or False)

x = 10
y = 15
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)

#Logical
#and
#or
#not

True and True - True
True and False - False
False and False - False
False and True - False


True or False - True
True or True - True
...

x = 5 
x += 1                
  #same as x = x + 1
print (x)

# is tests to see if 2 variables are equal or not

# if statement
# To write code, say if <whichever Logical Operation>:

x = 100
y = 20
if x > y: 
    print (f' {x} is greater than {y}')
    #Doesn't do anything because computer checked if statement is true or false and it was false so it didn't do anything
else:
    print (f' {x} is greater than {y}')

x = int(input("Enter first number: "))
y = int(input("Enter the second number: "))
if x>y:
  print(f'x - y = {x-y}')
else:
  print(f'y - x = {y-x}')
#elif means else if

#Make code for
  #0-3 : toddler
  #4-12 : child 
  #13-17 : teenager
  #18 and above : adult

age = int(input("What is your child's age? "))
if 0 < age <= 3:
  print("toddler")
elif 3 < age <= 12:
  print("child")
elif 12 < age <= 18:
  print("teenager")
else:
  print("adult")

  #code for weight in kg or lambda
    # formula : <n>  kg * 2.2 pounds

#wt = input('Weight in kg or lb: ')
#weight = int(input(f'Enter weight in {wt}: '))
#if wt.lower() == 'kg' :
 #   print('In kg')
  #  print (f'Weight in pounds is {weight * 2.2}')
#elif wt.lower() == 'lb' :
 # print('In lb')
  #print(f'Weight in pounds is {weight / 2.2}')


my_str = 'Hello World'
print(my_str[0:5:2])
  #Skips every other letter

print(len(my_str))  #len means the length of the string


for x in my_str:
  print(x)
print ('Done')

my_str = 'Hello World!'
i = 1

for x in range(100):
  print(x)
print('Done')
#range(n) -> 0 - n-1
#range (x,n,step) start from x goes up to n-1 skips step

#while loop

#while i < 10:
  #print(i) don't do this otherwise 1 will go on forever

i = 1
while i <= 100:
  print (i)
  i += 23
print ('Done')

#Make a command to print whether a number is even or odd

num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))

#Print whether a number is divisible by 5

number = int(input(" Please Enter any Positive Integer : "))

if((number % 5 == 0)):
 print("Number {0} is Divisible by 5 ".format(number))
else:
    print("Number {0} is Not Divisible by 5 ".format(number))

#print a factorial of n

num = int(input(" Please Enter any Positive Integer : "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#print command to ask if you can turn the fan on or off