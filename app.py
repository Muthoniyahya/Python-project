birth_year=input('Birth year:')
print(type(birth_year))
age=2021- int(birth_year)
print(age)
Course='Python for absolute beginners'
print (Course.upper())#capitalizes the letters
print(Course.startswith('B'))#returns a boolean
course='''Hi Iman ,
Here is your first python assignment 

Thankyou,
Python@lisalab.com

'''
print(course)
sentence='Python is a programming language'
print(len(sentence))# shows length of an item in a list

for fruits in("Apple","Mango","Banana","Avocado"):#used for iterating over a sequence
    print (fruits)
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)
names=["Kauthar","Aimal","Zahir"]
names.append("Eshan")#adds an item in a list
print(names)
names.sort()#sorts a list in ascending manner
print(names)
names.pop()#removes the last list in an item
print(names)