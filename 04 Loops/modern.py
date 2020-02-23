#this is basic application to demonstrate banking transaction using list, tuples, dictionary
import sys

bank_name = "Modern College of Vashi"
students = {}
id_no = 1
while 1:
    print("[+] {} [+]".format(bank_name))
    print("  1) Add Student \n  2) Delete Student \n  3) Show Students \n  4) Student Info \n  5) Exit")
    choice = int(input("Enter Your choice: "))
    if choice == 1:
        name = input("Enter your Name : ")
        age = input("Enter your age : ")
        course = input("Enter Your Course : ")
        admission_year = input("Enter your admission year : ")
        students[id_no] = [name,age,course,admission_year]
        id_no = id_no + 1
    if choice == 2:
        id_no = int(input("Enter account ID : "))
        del students[account_no]
    if choice == 3:
        for i in students:
            print("\n")
            print("[+] Student ID : {}".format(i))
            print("    Student name : {}".format(students[i][0]))
            print("    Student age : {}".format(students[i][1]))
            print("    Student course : {}".format(students[i][2]))
            print("    Student admission year : {}".format(students[i][3]))
    if choice == 4:
        id = int(input("Enter ID no : "))
        print("\n")
        print("[+] Student ID : {}".format(id))
        print("    Student name : {}".format(students[id][0]))
        print("    Student age : {}".format(students[id][1]))
        print("    Student course : {}".format(students[id][2]))
        print("    Student admission year : {}".format(students[id][3]))
    if choice == 5:
        break
    
print("Thanks for using our application")
sys.exit()
        


        
    

