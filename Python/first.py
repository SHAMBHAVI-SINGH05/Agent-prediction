
"""print("Hello World");
print(90+50)
name = "Shambhavi Singh"
print(name)
print(type(name))
age = 23 
old = False
a = None
print(type(old))
A,B = 2,3
txt = "@"
print(2*txt*3)
#floor basically roundoff 
A,B = 12,5
C=A//B
print(C)
#denominator negative answer negative
A,B = 5,-2
C=A%B
print(C)

#input() statement is used to accept values form user
name = input("name : ")
print(name)
age = int(input("age :"))
print(age)
#conditional statement
light = input("light :")
if(light == "red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light == "green"):
     print("go")
else:
    print("light is broken")
#Single Line if/ ternary Operator

#<var> = <var1> if <condition> else <var2>
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

#<str1> if <condition> else <str2>
food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#Clever if/ Ternary Operator
#<var> = (false_val,true_val)[<condition]
 age = int(input("age:"))
vote =("yes","no") [age <= 18]

#type conversion
a,b = 1,"2"
c = int(b)
sum = a+c
print(sum)

a = int(input("num1 :"))
b = int(input("num2 :"))
sum = (a+b)
print(sum)
str1 = "This is a string.\n we are creating it in python"
print(str1)
#negative index
str = "Apple"
str1 = str[-3:-1]
print(str1)

#Lists and tuples in python
#A built-in data type that stores set of values
#It cam store elements of different types together(integer,float,string etc)
marks =[76,98,99,81]
print(marks)
#List Slicing
a = marks[1:4]
print(a)
#example
movies =[]
mov1 = input("enter 1st movie:")
mov2 = input("enter 2ns movie:")
mov3 = input("enter 3rd movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#Tuples in python
#A built- in data type that leads us creata immutable sequence of values
tup = (2,1,3,4)
print(tup)

list1 = [1,2,3]
list2 = [1,2,3]

copy_list  = list1.copy()
copy_list.reverse()

if(copy_list == list1);
    print("palindrome list")


#Dictionary in python
#dictionaries are used to store data values in key:value pairs
#They are unordered,mutable(changeable) & dont allow duplicate keys
dict = {
    "name" : "Shambhavi Singh",
    "age" : 20,
    "marks" : [99,98,98],
}
print(dict)
#nested dictonary
student = {
    "name" : kiki,
    "subjects" : {
        "phy" : 97,
        "chem" :
    }
}

#Set in python
#set is th collection of the unordered items
#each element in the set must be unique & immutable

#Loops in python
#while loop

i = 1;
while(i<=100):
    print(i);
    i+=1

 #function in python
 def calc_sum(a,b):
 sum = a+b 
print(sum)
return sum"""