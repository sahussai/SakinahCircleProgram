import sqlite3
from Family import *

conn = sqlite3.connect('Data.db')

# conn.execute('''CREATE TABLE FAMILY
#        (ID CHAR(50) PRIMARY KEY NOT NULL,
#       FATHER  CHAR(50)    NOT NULL,
#       MOTHER  CHAR(50)    NOT NULL,
#       ADDRESS  CHAR(50)    NOT NULL,
#       PHONE_NUMBER    CHAR(50)    NOT NULL,
#       CHILDREN    CHAR(50)    NOT NULL,
#       FEES    CHAR(50)    NOT NULL
#       );''')

# conn.execute('''CREATE TABLE CHILDREN
#        (ID CHAR(50) PRIMARY KEY NOT NULL,
#        CHILD1  CHAR(50)    NOT NULL,
#        CHILD2  CHAR(50)    NOT NULL,
#        CHILD3  CHAR(50)    NOT NULL,
#        CHILD4    CHAR(50)    NOT NULL,
#       CHILD5    CHAR(50)    NOT NULL,
#        CHILD6    CHAR(50)    NOT NULL
#        );''')

conn.execute('''CREATE TABLE PAYMENT
        (ID CHAR(50) PRIMARY KEY NOT NULL,
        SEPTEMBER  CHAR(50)    NOT NULL,
        OCTOBER  CHAR(50)    NOT NULL,
        NOVEMBER  CHAR(50)    NOT NULL,
        DECEMBER    CHAR(50)    NOT NULL,
        JANUARY    CHAR(50)    NOT NULL,
        FEBRUARY    CHAR(50)    NOT NULL,
        MARCH    CHAR(50)    NOT NULL,
        APRIL    CHAR(50)    NOT NULL,
        MAY    CHAR(50)    NOT NULL,
        JUNE    CHAR(50)    NOT NULL
        );''')


#fam = Family('Syed Iqbal Hussain','Rashida Iqbal')
#fam.set_Address('3504 87 St NW T6K0J4')
#fam.Children = 'Uzair Hussain'
#fam.set_nChildren()
#fam.set_Fees()
#fam.set_phoneNumber('7806651751')
#fam.generateID()
#sql_list = fam.updateList()

#sql_list = ['3218','Abeer Hussain','Uzair Hussain','Zubair Hussain','','','']

#db = conn.cursor()
#db.execute("INSERT INTO CHILDREN(ID, CHILD1, CHILD2, CHILD3, CHILD4, CHILD5, CHILD6)"
#    "VALUES(?,?,?,?,?,?,?)", sql_list)



#db.execute("SELECT * FROM FAMILY;")
#test = db.fetchall()

#for item in test:
#    for it in item:
#        print(it)
#    print("====================")

conn.commit()

conn.close()