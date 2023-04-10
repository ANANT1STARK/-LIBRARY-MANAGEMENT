import mysql.connector as a

con = a.connect(host="localhost",user="root",passwd="",database="library1")
def addbook():
    book_name = input("enter the book name : ")
    book_code = input("enter the book code : ")
    no_of_books = input("enter the total book : ")
    subject = input("enter subject : ")
    data = (book_name,book_code,no_of_books,subject)
    command = 'insert into books values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(command,data)
    con.commit()
    print('data entered successfully')
def bookup(book_code,no_of_books):
    command = 'select total_book from books where BCODE=%s'
    data = (book_code,)
    c = con.cursor()
    c.execute(command,data)
    myresult = c.fetchone()
    t = myresult[0] + no_of_books
    sql = 'update books set total_book = %s where BCODE = %s'
    data =(t,book_code)
    c.execute(sql,data)
    con.commit()
    
def issueb():
    name_of_student = input("enter students name : ")
    book_name = input("enter book name : ")
    book_code = input("enter the book code : ")
    d = input("enter todays date : ")
    command = "insert into issue values(%s,%s,%s,%s)"
    data = (name_of_student,book_name,book_code,d)
    c = con.cursor()
    c.execute(command,data)
    con.commit()
    print("book issued to : ",name_of_student)
    bookup(book_code,-1)
def submitb():
    name_of_student = input("enter students name : ")
    book_name = input("enter book name : ")
    book_code = input("enter the book code : ")
    d = input("enter todays date : ")
    command = "insert into submit values(%s,%s,%s,%s)"
    data = (name_of_student,book_name,book_code,d)
    c = con.cursor()
    c.execute(command,data)
    con.commit()
    print("book submitted  from : ",name_of_student)
    bookup(book_code,1)
def dbook():
    book_code =input('enter the book code : ')
    a = 'delete from books where BCODE=%s'
    data = (book_code,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
addbook()