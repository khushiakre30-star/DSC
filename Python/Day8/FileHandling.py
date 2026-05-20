#====================================================================================
#File Handling
import csv
f = open('employee.csv','a')
a = csv.writer(f)
#a.writerow(["EmpID" , "Emp Name", "Emp Age"])
empid = int(input("Enter your Emp id : "))
empName = input("Enter Employee Name : ")
age = int(input("Enter employee age : "))
a.writerow([empid,empName,age])
print("File has created")