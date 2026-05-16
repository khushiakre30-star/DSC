#Data jyda rahe tho best rhega -linkedlist
#=====================================================================================
#Class--->Object---->Constructor
#class-->binding of data members and member function 
#Object-->

#=====================================================================================

# class Student:
#     def __init__(self, name, age):
#         self.name="Khushi"
#         self.age = 20

#         def display(self):
#             print("Name:", self.name)
#             print("Age:", self.age)

#======================================================================================
#    
# class Message:
#     def __init__(self):
#         self.text = "I am constructor"
#     def shows(self):
#         print(self.text)
# obj = Message()
# obj.shows()
# obj2 = Message()

#====================================================================================

#Parameterize Constructor

# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no

#     def displayStudentInfo(self):
#         print("Name = ",self.Name)
#         print("Age = ",self.Age)
#         print("Roll No = ",self.RollNo)
    

# studentObj= StudentInfo("Khushi",20,33)
# studentObj.displayStudentInfo

# #======================================================================================

# #Stack implementation with size limit
# # Stack implementation 
# # 1. list/array
# # 2.linkedlist

# import sys
# class Stack:
#     def __init__(self,size):
#         self.myStack = []  #creating stack
#         self.stackSize = size # Stack size defined

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFull():
#             print("Stack is Full ")
#         else:
#             self.myStack.append(value)
#             print("Element Push")

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty !!!!!")
#         else:
#             print(self.myStack.pop())

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty ")
#         else:
#             print(self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = None

#     def display(self):
#         print(self.myStack)

# size=int(input("Enter the Size of Stack : "))
# obj = Stack(size) 
# print("Stack has Created : ")
# while True:
#     print("1. PUSH Operation : ")
#     print("2. Display Stack : ")
#     print("3. POP Operation : ")
#     print("4. PEEK Operation : ")
#     print("5. Delete Operation : ")
#     print("7. Exit")
#     choice =int(input("Enter Your Choice : "))
#     if choice == 1:
#         value = int(input("Enter value to push in Stack : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     else:
#         sys.exit()

#=======================================================================================

#Input:572378233 3
#Output:3

mylist = [5,7,2,3,7,8,2,3,3]
newdict ={}
for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j< len(mylist):
        if key == mylist[j]:
            count+=1
        j = j+1
    if count>1:
        newdict[key] = count
    max = newdict
    print(max)

#=======================================================================================

# #Student Managment System
# 1 Add student
# 2 show student
# 3 update student
# 4 delete student
# 5 exit
# select any choice:
