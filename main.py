#Variables
x=10
y=20

print(('10+20='), x+y)

print(x+y)
print(y-x)
print(y/x)
print(x*y)
print(x//y)
print(10**20)
print(10%20)


first_name=input('Enter your first name:')
last_name=input('Enter your last name:')
print('Your first name is' + first_name + '.' 'Your last name is' + last_name+ '.')
print('Your full name is...' + first_name + ' '+ last_name)

#fstring
x=78
y=16
print (f'The value of {x} + {y} = {x+y}')

#Data_types
  #string
    #x='ad'
  #Integer/int
    #a=10
  #Decimal Float
    #b=7.2
  #Boolean
    #light_bulb_on = True

x='10'
y="20"

print (int(x)+int(y)) #doesn't work
print (int(x)+float(y)) #does work

#you can convert and integer to a float, but not a float to an integer. 

a=(input("Enter a number:"))
b=(input("Enter another number:"))
a = int(a)
b=int(b)
print (f"the sum of {a} + {b} = {a + b}")

firstname=input('Enter your first name')
lastname=input('Enter your last name')
address=input('Enter your address')
zipcode=input('Enter your zipcode')
birthyear=int(input('Enter your year of birth'))
age = 2020 - birthyear
print(f'''Name: {firstname} {lastname}
Address: {address}
Zip: {zipcode}
Age: {age}''')

number1 = int(input("Enter number1"))
number2 = int(input("Enter number2"))

'''
Operators"

+
-
*
/
% (Modulus)
**(Exponent)
//(Integer Division)

'''

number1 = int(input("Enter number1 "))
number2 = int(input("Enter number2 "))

print(f'Result of {number1} + {number2} = {number1 + number2}')
print(f'Result of {number1} - {number2} = {number1 - number2}')
print(f'Result of {number1} * {number2} = {number1 * number2}')
print(f'Result of {number1} / {number2} = {number1 / number2}')

# % means modulus (Reminder)
print(f'Result of {number1} % {number2} = {number1 % number2}')

# ** means Exponent
print(f'Result of {number1} ** {number2} = {number1 ** number2}')

# // means integer division
print(f'Result of {number1} // {number2} = {number1 // number2}')

#https://www.w3schools.com/python/python_ref_string.asp


#Practice 
x=23
y=18

number1 = int(input("Enter number 1 "))
number2 = int(input("Enter number 2 "))

print(f'Result of {number1} ** {number2} = {number1 ** number2}')
