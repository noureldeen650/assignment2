'''Q1:'''
string ="hello"
print(len(string))

i=0
for x in string:
 i=i+1
print(i)

'''Q2:'''
print("enter your name")
name=input()
print("enter your age")
age=input()
print("enter your favorite food")
favorite_food= input()

print(f"Hi! my name is "+name+". I am "+age+ " year old,and my favorite food is "+favorite_food)

'''Q3:'''
print("enter the name of the first city")
city1= input()

print("enter the name of the second city")
city2=input()
print("enter the name of the third city")
city3=input()
print("enter the name of the fourth city")
city4=input()
print(f"I would like to visit these cities: {city1}, {city2}, {city3}, {city4}")

'''Q4:'''
string="python developer!"
print(string[2:5])
print(string[2:])
print(string[-5:])
print(string.strip())
print(string.replace("p", "P"))

i=0
for x in string:
    if x=='p':
     i=i+1
print(i)