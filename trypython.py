# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# total = num1 + num2
# result = "{0} plus {1} = {2}".format(num1, num2, total)
# print(result)


# text2 = input("Write something here again: ")
# print(text2.upper())


# text1 = input("Write something here: ")
# print(text1[::-1])


# num1 = int(input("Type a number here: "))
# if num1 <= 10:
#     print("too small")
# else:
#     print("too big")


# num1 = int(input("Type a number here: "))
# num2 = int(input("Type a second number here: "))


# if num1 == num2: 
#     print("same")
# else:
#     print("Different")


# num1 = int(input("type a number: "))
# if num1 == 1:
#     name = input("enter your name: ")
#     print("your name is: " + name)
# if num1 == 2:
#     age = input("enter your age: ")
#     print("your age is: " + age)


# NumberList = []

# for i in range(0, 3):
#     number = int(input("type your number: "))
#     NumberList.append(number)


# for i in NumberList:   
#     print(i)


# NumberList = []

# for i in range(0, 10):
#     number = int(input("type your number: "))
#     NumberList.append(number)
   
# print(sum(NumberList))


# i = 0

# while i < 100:
#     print(i)
#     i += 2


# people = {
#     "Joe": {"age": 23, "eyes": "blue", "height": 134, "nationality": "Irish"}, 
#     "Ann": {"age": 13, "eyes": "green", "height": 172, "nationality": "Irish"}, 
#     "Bob": {"age": 23, "eyes": "red", "height": 234, "nationality": "Turkmenistan"}, 
#     "Sam": {"age": 45, "eyes": "grey", "height": 134, "nationality": "French"}, 
#     "Tina": {"age": 46, "eyes": "blue", "height": 154, "nationality": "American"}, 
# }

# name = input("Enter name: ")
# person = people[name]

# what = input("What do you want to know? ")
# print (person[what])


# def add(a, b):
#     print(a + b)
    
# a = int(input("type a number: "))
# b = int(input("type a second number: "))
    
# add(a, b)


# 55. Write a function that accepts one argument n. You can assume that n is an integer. The function should return True if n is even, False if it's odd.
# def one(n):
#     return n % 2 == 0:
        
# one(3)

# 56. Write a function called message that accepts no arguments, it returns "This is the message". Try the following two print
# statements to test the function, compare the results. print(message())  print(message)

# def message():
#     print("This is the message: ")

# print(message())
    
# print(message)

# 57. Create a List containing all of the numbers from 1 to 6. Use the sum function to calculate the sum of the contents of the list.
# numbers = [1, 2, 3, 4, 5 ,6]
    
# print(sum(numbers))   


# 58. Use the range function to create a range from 0 to 99, use the list function to convert the range into a list. Print the list.
# list1 = []

# for i in range(0, 99):
#     i += 1
#     list1.append(i)
# print(list1)


#59. Use the range and list functions to create a list of all of the even numbers from 10 to 50 (including 50). Print out the length of that list.

# l = list(range(10, 51))
# print(l)
# print(len(l))


# 60. Create the following list of lists. print the 3rd item of the fifth list.

# l = [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]

# print(l[4][2])


# 61. Create an empty list called evens. Write a for loop that loops through all the numbers from 0 to 10. Append the even numbers to the evens list. Print out the evens list.

# evens = []

# for i in range(0, 11, 2):
#     evens.append(i)
# print(evens)

# 62. Create any list with at least 10 items. Use python's list slicing syntax to print: The first item, The last item, All but the first item, All but the last item.

# l = []
# for i in range (0,10):
#     l.append("item " + str(i))
# print(l)

# print(l[0])
# print(l[-1])
# print(l[1:])
# print(l[:-1])

# 63. Create a dictionary that represents a student. Each student has a name, an age, a nationality, and a list of subjects.

# student = {
#     a: {"name": "Miguel", "age": 35, "nationality": "spanish", "subjects":["english", "maths"] }
#     b: {"name": "Luca", "age": 26, "nationality": "Italian", "subjects":["geography", "science"] }
#     c: {"name": "Ewa", "age": 25, "nationality": "Irish", "subjects":["business", "accounting"] }
#     d: {"name": "Michael", "age": 36, "nationality": "Irish", "subjects":["art", "irish"] }
# }

# 64. Create a list containing at least 4 of the students described in challenge 63, Convert the list into a dictionary, use the the students names as the key for the dictionary.

# studentList = [a, b, c, d]

# studentDic = {
#     Miguel: {"age": 35, "nationality": "spanish"}
#     Luca: {"age": 26, "nationality": "Italian"}
#     Ewa: {"age": 25, "nationality": "Irish"}
#     Michael: {"age": 36, "nationality": "Irish"}
# }

# 65. Create a dictionary where the keys are words in the english language, and the values are the lengths of the words.
# words = {
#     "hello": 4,
#     "how": 3,
#     "when": 4,
#     "also": 4
# }

# 66. Data Structures Challenge
# A Musician has a name, nationality, and gender. A Musician can play in any number of bands. A Musician can play multiple instruments. For each instrument they have a competency level between 1 and 100.
# Create a data structure that stores the details of each musician along with the bands and instruments.
# It should be possible to get the details of any musician by name, so use a dictionary to store the musician details.