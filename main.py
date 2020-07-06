#Week 7: Functions
'''
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
  for x in l1:
    if x%2==0:
      numberofeven+=1
  return x


#HW
#Have list of numbers and return the range of the list
def highlow(list1):
  
  diff=0
  sortlist=sorted(list1)
  diff=sortlist[-1]-sortlist[0]
  
  return diff

l1=[1,2,3,4,5,6,7,0,0]
print(highlow(l1))
l1=[0,-1,0,0,0]
print(highlow(l1))

#create a code that adds the sum of everything except the first and last number
def ignore_first_last(my_list):
  sum = 0
  for i in my_list:
    sum += i 
  return sum - my_list[0] - my_list[-1]

l1 = [1,2,5,2,7,3]
print(ignore_first_last(l1))    

'''
NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]
if Even_Sum > Odd_Sum:
  print("Even Wins!")
elif Odd_Sum > Even_Sum:
  print("Odd Wins!")
else:
  print("There was a tie.")    

#Homework
#Check if number is an armstrong number or not
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")

#print first 10 armstrong numbers
 