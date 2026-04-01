"""def print_your_name(name, age, height, marks):
    print(f"The datatype of age is {type(age)}")
    print(f"The datatype of height is {type(height)}")
    print(f"The datatype of name is {type(name)}")
    print(f"The datatype of marks is {type(marks)}")

    return f"My name is {name}, age is {age} and height is {height} cm and marks are {marks}"

# Now we call the function **outside the definition**
function_result = print_your_name("Shambhavi Singh", 20, 165, 99)

print(function_result)

def even_number_printer(n):
    for i in range(n):
        if (i+1)%2 == 0:
            print(i+1)



even_number_printer(50)

a = [1,2,3]
b = [4,5,6]

sum = 0

for i in range(len(a)):
   sum = sum + a[i]*b[i]

print("The sum is",sum)

import numpy as np

a = np.array([1, 2, 3])   # 1D array

b = np.array([[1, 2], [3, 4]])  # 2D array

c = [1, 2, 3]  # Python list

c = c * 3  # Repeat the list 3 times
a = a * 2  # Multiply array elements by 2

d = np.array([[1,2,3],[4,5,10]])
print(a)  # Prints: [2 4 6]
print(c)  # Prints: [1, 2, 3, 1, 2, 3, 1, 2, 3]

np.sqrt(c)
print(type(b[0,1]))
print(np.sum(d,axis=0))

import numpy as np
import time
N  = 1_000_000

list1 = list(range(N))
list2 = list(range(N))
list3 = list(range(N))

time_start = time.time()

for i in range(len(list1)):
    list3[i] = list1[i]*list2[i]

time_end = time.time()

print("The total time taken with lists= ", time_end-time_start)
print("The length of list3 = ", len(list3))

list1 = np.arange(N)
list2 = np.arange(N)

time_start_np  = time.time()

list3 = list1*list2

time_end_np = time.time()

print("The total time taken with numpy = ", time_end_np-time_start_np)
print("The shape of list3 = ", np.shape)

import numpy as np
import time
import random

N = 100
A = []
B = []
C = []

for i in range(N):
    A.append([0]*N)
    B.append([0]*N)
    C.append([0]*N)


for i in range(N):
    for j in range(N):
        A[i][j] = random.random()

for i in range(N):
    for j in range(N):
        B[i][j] = random.random()  

for i in range(N):
    for j in range(N):
        C[i][j] = 0

time_start = time.time()

for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j] += A[i][k]*B[k][j]

time_end = time.time()

print("The total time taken with python list = ", time_end-time_start)
print(len(C),len(C[0]))

A1 = np.random.rand(N,N)
B1 = np.random.rand(N,N)

time_start_np = time.time()

C1 = A1@B1

time_end_np = time.time()

print("The total time taken with numpy = ", time_end_np-time_start_np)
print(C1.shape)


import numpy as np
import time
import random

A = np.array([[60,70,95],[83,68,79],[91,39,45],[90,90,3],[80,81,82]])

mean_scores = np.mean(A,axis=1)
print(mean_scores)

subject_top_score = np.max(A,axis = 0)
print(subject_top_score)
print("Subject toppers = ",np.argmax(A,axis=0))
print("Overall topper is student number",np.argmax(np.sum(A,axis =1)))
print(np.where(mean_scores == max(mean_scores))[0][0])

import numpy as np
import time
import random

A = np.array([[2,4,5],[6,7,9],[3,5,6],[7,6,7]])
total= np.sum(A,axis=1)
print("Total marks for each student:",total)
topper = np.argmax(total)
print("Topper is student number:",topper)

import numpy as np
import time
import random

A = np.array([[60,79,82,91],
             [45,67,88,34],
             [45,67,22,76],
             [67,89,90,78],
             [64,67,43,66]])
min_per_subject = np.min(A,axis=0)
print("Min score in each subject:",min_per_subject)
"""

import numpy as np
A = np.array([[55,34],
              [56,78],
              [77,23],
              [67,87],
              [52,14]])
topper_first_mark = np.argmax(A[:,0])
print(topper_first_mark)