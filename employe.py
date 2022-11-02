import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'employedb')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add employee')
    print('2 view all employee')
    print('3 search a employee')
    print('4 update a employee')
    print('5 delete a employee')
    print('6 exit')
    choice = int(input('Enter the option:'))
    if(choice==1):
        print('employee enter selected')
    elif(choice==2):
        print('view employees')
    elif(choice==3):
        print('search a employees')
    elif(choice==4):
        print('update the employees')
    elif(choice==5):
        print('delete the employees')
    elif(choice==6):
        break
    