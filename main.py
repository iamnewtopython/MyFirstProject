#Week 5
#List,Set, and Tuple

#List
list1 = [1,2,3,4,5]
countries = ['Canada','U.S.A','Australia',' Eygpt', 'India']
data = [1,'abc', 98.3, True]

for i in countries:
  print(i)




print (len(countries)) #prints length of countries
print(countries) #prints countries
countries.append('China') #adds China
countries.insert(0,'China') #puts China first
print(countries) #prints new countries
print(len(countries)) # prints new lengths of countries
#the code above works but looks messy

print (len(countries)) #prints length of countries
print(countries) #prints countries
#countries.append('China') #adds China
countries.insert(0,'China') #puts China first
if 'Eygpt' in countries:
  countries.remove('Eygpt')
else:
  print('The country you named is not there.')  
print(countries) #prints new countries
print(len(countries)) # prints new lengths of countries


print (len(countries)) #prints length of countries
print(countries) #prints countries
#countries.append('China') #adds China
countries.insert(0,'China') #puts China first
if 'Eygpt' in countries:
  countries.clear()
else:
  print('The country you named is not there.')  
print(countries) #prints new countries
print(len(countries)) # prints new lengths of countries


#print the first country alhabetically
print(min(countries))

#prints the last country alphabetically
print(max(countries))



#write a program to show something in a list that has the minimum amount of letters

mycountries = ['U.S.A','Australia','Sudan', 'India']
smallest_country = ''
min_length = 100
for i in mycountries:
  if len(i) < min_length:
    min_length = len(i)
    smallest_country = i
print(f'The country with the smallest length is {smallest_country} and its length is {min_length}.') 
#the computer goes through the countries lengths. It checks every one and in the end prints the one with the lowest under a minimum length of hundred(this is for the project above)   


#write a program to show the hottest country and its temperature out of a list and the coldest country and its temperature out of the list
countries = ['India', 'USA', 'Canada', 'Australia', 'South Africa']
temperatures = [100.2,96.8,85.3,73.8,102.3]

hot_temp = 0
hot_country = ''
cold_temp = 1000
cold_country = ''

for index, temp in enumerate(temperatures):
  if temp > hot_temp:
    hot_temp = temp
    hot_country = countries[index]
  if temp < cold_temp:
    cold_temp = temp
    cold_country = countries[index]

print(f'The hottest country is {hot_country} and its temperature today is {hot_temp}')
print(f'The coldest country is {cold_country} and its temperature today is {cold_temp}')
#The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later. The temperatures were enumerated to the countries.



#Set
hello_in_other_languages = {'hi','hello','bonjour','bienvenido','hola','hi' , 'bonjour'}
print(len(data))
for i in data:
  print(i)
#there is a different outcome and different order every time 

countries = ['India', 'USA', 'Canada', 'Australia', 'South Africa', 'India','Australia','USA']
countries_set = set(countries) #the set removes duplicate
countries_list = list(countries_set) #the set is converted to a list but is not in order
countries_list.sort() #countries sorted
print(countries_list) #printed countries 


# Key differences between set and list 

#1. Lists can have duplicates
#2. List data is in order
#3. Set data is not order
#4. Set removes duplicates
#5. Lists can be sorted
#6. Set cannot be sorted

#The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on. The sorted() function will create a new list containing a sorted version of the list it is given.


#Homework
#5 names = ['a','b','c']
#maths =[10,20,30]
#physics = [80, 80, 56.3]
#chemistry =[60,20,30]

#The top scorer in Math , physics and chemistry
#The lowest scorer in Math , physics and chemistry
#The top scorer by taking the average
#The lowert scorer by taking the average
#Hint: use only list because set can't hold duplicates


names = ['Michelle','Dante','Eric','John', 'Tris']
score_physics = [100,87.5,98.6,73.5,76.5]
score_math = [65.4,97.7,84.5,87.4,89.6]
score_chemistry = [83.6,76.5,98.3,86.8,99.5]


high_score_math = 0
high_scorer_math = ''
low_score_math = 101
low_scorer_math = ''

for index, score in enumerate(score_math):
  if score > high_score_math:
    high_score_math = score
    high_scorer_math = names[index]
  if score < low_score_math:
    low_score_math = score
    low_scorer_math = names[index]
print (f'The top scorer in math is {high_scorer_math} with a score of {high_score_math}.')    
print (f'The lowest scorer in math is {low_scorer_math} with a score of {low_score_math}.')

high_score_physics = 0
high_scorer_physics = ''
low_score_physics = 101
low_scorer_physics = ''


for index, score in enumerate(score_physics):
  if score > high_score_physics:
    high_score_physics = score
    high_scorer_physics = names[index]
  if score < low_score_physics:
    low_score_physics = score
    low_scorer_physics = names[index]


print (f'The top scorer in physics is {high_scorer_physics} with a score of {high_score_physics}.')    
print (f'The lowest scorer in physics is {low_scorer_physics} with a score of {low_score_physics}.')


high_score_chemistry = 0
high_scorer_chemistry = ''
low_score_chemistry = 101
low_scorer_chemistry = ''


for index, score in enumerate(score_chemistry):
  if score > high_score_chemistry:
    high_score_chemistry = score
    high_scorer_chemistry= names[index]
  if score < low_score_chemistry:
    low_score_chemistry = score
    low_scorer_chemistry = names[index]


print (f'The top scorer in chemistry is {high_scorer_chemistry} with a score of {high_score_chemistry}.')    
print (f'The lowest scorer in chemistry is {low_scorer_physics} with a score of {low_score_chemistry}.')


#Tuple
#A tuple is a collection which is ordered and unchangeable

list1 = [1, 3, 2, 4, 5]  #in random order
tuple1 = tuple(list1)
print(list1)
#*tuple cannot be used with "sort" but it can with 'sorted'
x = sorted(tuple1)
print(x)

#Dictionary
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

student = {'name': 'Tris', 'age': 16, 'languages': 'English'}
print(student)
#this prints the whole thing with brackets
print(student.get('name'))
print(student.get('phone'))

student["phone"] = '728-249-1938'

if (student.get('phone')):
    print(f'Phone number of {student.get("name")} is {student.get("phone")}')
else:
    print(f'{student.get("name")} does not have a phone.')

print(student)
age = student.pop('age')
print(x)
print(student)

t1 = ('a', 'b', 'c', 'r')
l1 = list(t1)
s1 = set(l1)

print(l1.pop())
print(s1.pop())
#pop removes and returns the value

number = input('Enter a number: ')

if number.isdigit():
    output = ''
    length = len(number) - 1
    count = length
    for i in number:
        if i != '0':
            output += str(int(i) * 10**count) + ' + '
            count = count - 1
    print(f'{number} = {output[:-3]}')
else:
    print(f'{number} is not an integer')



    #palindrome
    str = input('Enter a string: ')
if len(str) == 1:
    print('Input needs to be more than 1 character')
else:
    reverse_str = str[::-1]
    if str == reverse_str:
        print(f'{str} is a palindrome')
    else:
        print(f'{str} is NOT a palindrome')


#HW
#-find out what update is in dictionary
#-print Roman Numerals
#https://www.math-only-math.com/rules-for-formation-of-roman-numerals.html
