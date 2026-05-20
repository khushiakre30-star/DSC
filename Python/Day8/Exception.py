#====================================================================================
#Exception in Python

# try:
#     a = int(input("Enter a value : "))
#     b = int(input("Enter a value : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't devided by Zero")
# except ValueError:
#     print("Enter only integer value : ")
# except:
#     print("invalid value : ")

#====================================================================================

# try:
#     a = int(input("Enter a value : "))
#     b = int(input("Enter a value : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

#====================================================================================

import logging
logging.basicConfig(filename="newfile.txt" , level=logging.DEBUG)
try:
    a = int(input("Enter a value : "))
    b = int(input("Enter a value : "))
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is set up. Check 'newfile.txt' for log details.")
