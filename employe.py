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
    choice = int(input('Enter an option: '))
    if(choice==1):
        print('employee enter selected')
        import mysql.connector
    choice = int(input('Enter the option:'))
    if(choice==1):
        print('employee enter selected')
        empcode = input('enter the code: ')
        empname = input('enter the name: ')
        designation = input('enter the designation: ')
        salary = input('enter the salary: ')
        cmpany = input('enter the company name: ')
        phnnumber = input('enter the phone number: ')
        emailid = input('enter the email id: ')
        password = input('enter the password: ')
        sql = 'INSERT INTO `employees`(`empcode`, `empname`, `designation`, `Salary`, `cmpname`, `phnnumber`, `emailid`, `Password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (empcode ,empname, designation,salary,cmpany,phnnumber,emailid,password)
        mycursor.execute(sql , data)
        mydb.commit()
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
    