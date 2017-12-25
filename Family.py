import random as r
import sqlite3


class Family:
    Father = ''
    Mother = ''
    nChildren = 0
    Children = []
    Fees = 0
    Address = ''
    phoneNumber = '' # maybe add primary and secondary phone number...
    ID = 0
    sql_list = [ID,Father, Mother, Children, Fees, Address, phoneNumber]

    def __init__(self, fname, mname):
        self.Father = fname
        self.Mother = mname

    def addChildren(self, names):
        indexes = names.find(',')
        if indexes == -1: # If there are no commas, we assume only one name is given
            self.Children = [names]
            self.nChildren = 1
            self.Fees = '100'
        else:
            li = names.split(',')
            self.Fees = '200'
            for name in li:
                self.Children.append(name.strip())
            self.nChildren = len(self.Children)

    def set_Address(self, address):
        self.Address = address

    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def generateID(self):
        self.ID = str(r.randint(1000,9999))
        # make sure the ID is unique
        conn = sqlite3.connect('Data.db')
        db = conn.cursor()
        db.execute("SELECT ID FROM FAMILY")
        id_list = db.fetchall();
        while self.ID in id_list:
            self.ID = str(r.randint(1000,9999))

        conn.close()

    # Updates sql_list with the latest values of Members, and returns it.
    # Purpose is to create a convenient way to insert data into the database
    def updateList(self):
        self.sql_list = [self.ID,self.Father,self.Mother,self.Address, self.phoneNumber,self.nChildren,self.Fees]
        return self.sql_list



    # This function is no longer necessary; Saving to Database is done by the DatabaseAccess class
    def save(self):
        conn = sqlite3.connect('Data.db')
        db = conn.cursor()
        db.execute("INSERT INTO FAMILY(ID, FATHER, MOTHER, ADDRESS, PHONE_NUMBER, CHILDREN, FEES)"
            "VALUES(?,?,?,?,?,?,?)", self.sql_list)

        #create a sql_list for children. Pad with empty strings
        sql_list_Child = self.Children
        if (len(sql_list_Child) < 6):
            for i in range(1,6 - len(sql_list_Child) + 1):
                sql_list_Child.append('')
        sql_list_Child.insert(0,self.ID)

        db.execute("INSERT INTO CHILDREN(ID, CHILD1, CHILD2, CHILD3, CHILD4, CHILD5, CHILD6)"
        "VALUES(?,?,?,?,?,?,?)", (sql_list_Child,))


        conn.commit()
        conn.close()

