birth_year=input('Birth year:')#input allows user to print
print(type(birth_year))
age=2021- int(birth_year)
print(age)
Course='Python for absolute beginners'
print (Course.upper())#capitalizes the letters
print(Course.startswith('B'))#returns a boolean
course=''''Hi Iman ,
Here is your first python assignment 

Thankyou,
Python@lisalab.com

'''''
print(course)
sentence='Python is a programming language'
print(len(sentence))# shows length of an item in a list

for fruits in("Apple","Mango","Banana","Avocado"):#goes through every item in a list and prints in a new line
    print (fruits)
matrix=[
    [1,2,3],
    [10,20,30],
    [100,200,1000]
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

riddle='what has legs but does not have a body ?'
concealed_riddle="trouser"
riddle_record=0
riddle_end=3
while riddle_record < riddle_end: #executes a set of statement if the condition is true
    riddle=str(input('take a shot at: '))
    riddle_record+=1
    if riddle==concealed_riddle: #used for decision making  #used for comparison
         print('Yeeey fantastic')
    else: #executes if a condition is met
        print('pass it to another person')










