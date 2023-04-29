# 1.Create a function named Subtraction which can subtract two numbers.

def Subtraction(a,b):
    sub=a-b
    return sub

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The result of subtraction is: ", Subtraction(num1,num2))

# 2.Create a function named Multiply which can multiply three numbers.

def Multipy(x,y):
    multipy=x*y
    return multipy

num1=int(input("Enter the value: "))
num2=int(input("Enter the value: "))
print("The result of multipy is: ", Multipy(num1,num2))

#3.Create an empty list named test_empty_list.Expected result: test_empty_list = []

test_empty_list = []
len(test_empty_list)

# 4.Create a list which contain five items ("I", "love", "Python", "so", "much!").
# Expected result: list_name = ["I", "love", "Python", "so", "much!"]

list_name = ["I", "Love", "Python", "so", "much!"]
print(list_name)

# 5.Access the third element in the list of exercise 4.
# Expected result: Python

list_name = ["I", "Love", "Python", "so", "much!"]
print(list_name[3])

# 6.Modify the item "love" in the list in the exercise 4 to "hate".
# Expected result: list_name = ["I", "hate", "Python", "so", "much!"]

list_name = ["I", "Love", "Python", "so", "much!"]
list_name[1] = "hate"
print(list_name)