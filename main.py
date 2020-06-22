#Week 67: Functions

#defining a function
def function_greeting(name):
  print(f'Hello! Welcome to Python class, {name}')

function_greeting('Josephine')
function_greeting('Jack')  
#don't orget the colon

def calculate(a , b):
  sum = a + b
  sub = a - b
  mul = a * b

  return sum , sub, mul
#returns as tuple

s , s1 , s2 = calculate(10,5)
print(f' Addition is {s}')
print(f'Subtraction is {s1}')
print(f'Multiplication is {s2}')
#you can return multiple values by separating them by commas as shown in s , s1, and s2


def multiplication(l1):
  multiplication = 1
  for i in l1:
    multiplication *= i
  return multiplication

l1 = [0, 23, 26, 2, 12, 4, 0, 0]
for x in l1:
  if x == 0:
    l1.remove(x)
print(multiplication(l1))



l1=[1,231,5,4,5,345,35,345,462,4,5,23]
print(multiplication(l1))
def count_even_numbers(mylist):
  numberofeven=0
  for x in list1:
    if x%2==0:
      numberofeven+=1
  return x


list1 = [1,3,5,15,9,10,21,25,30,45]

def count_mul3_mul5(list1):
  mul3 = 0
  mul5 = 0
  for i in list1:
    if == 0:
      continue
    if i % 3 == 0:
      mul3 += 1
    elif i % 5 == 0:
      mul5 += 1    
  return mul3,mul5

  mul3, mul5 = count_mul3_mul5(list1)
  print(list1)
  print(f'Mul 3 count: {mul3}, mul 5 count: {mul5}')




#HW
#Have list of numbers and return the range of the list
#add all numbers in an array . . . but if there is number 9, ignore that and following number
#Give a list. . .add all numbers. . .but if there is 10, ignore that and rest of the 5 numbers