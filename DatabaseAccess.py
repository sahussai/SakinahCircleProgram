import sqlite3

# This class is created for the purpose of accessing the database file Data.db. It has functions to access and manipulate
# information in the database so all database operations can be implemented through this class.

class DatabaseAccess:


	# Function List:
	# getIDList(self)
	# save(self,family)
	# deleteFamily(self, ID)
	# viewFamily(self, ID)
	# searchFamily(self, ID)

    # This function retiurns a list of all the ID values stored in the table. It is used by the main GUI to display all
	# families currently in the database.
	# It does not accept any arguments.

	def getIDList(self):
		id_List = []
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()

		db.execute('SELECT ID FROM FAMILY')
		id_List1 = db.fetchall()

		conn.close()

		for item in id_List1:
			id_List.append(str(item[0]))

		return id_List

    # This function accepts a family object and stores the information in the FAMILY and CHILDREN tables
	# For children, if there are less than 6 children specified, the list is padded with empty strings
	# until the length of the list is 6.
	# It does not return anything.
	def save(self,family):
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()
		db.execute("INSERT INTO FAMILY(ID, FATHER, MOTHER, ADDRESS, PHONE_NUMBER, CHILDREN, FEES)"
            "VALUES(?,?,?,?,?,?,?)", family.sql_list)

        #create a sql_list for children. Pad with empty strings
		sql_list_Child = family.Children

		if len(sql_list_Child) < 6:
			for i in range(1,6 - len(sql_list_Child) + 1):
				sql_list_Child.append('')

		sql_list_Child.insert(0,family.ID)

		db.execute("INSERT INTO CHILDREN(ID, CHILD1, CHILD2, CHILD3, CHILD4, CHILD5, CHILD6)"
        "VALUES(?,?,?,?,?,?,?)", sql_list_Child)

		conn.commit()
		conn.close()

    # This function accesses Data.db and deletes all records with the given ID in the tables FAMILY and CHILDREN.
	def deleteFamily(self,ID):
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()

		db.execute("DELETE FROM FAMILY WHERE ID = ?",(ID,))
		db.execute("DELETE FROM CHILDREN WHERE ID = ?",(ID,))

		conn.commit()
		conn.close()

    # This function returns all information associated with the given ID in the tables FAMILY and CHILDREN. finfo contains
	# family information and cinfo contains children information.
	def viewFamily(self,ID):
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()
		db.execute("SELECT * FROM FAMILY WHERE ID=?",(ID,))
		finfo = db.fetchall()

		db.execute("SELECT * FROM CHILDREN WHERE ID=?",(ID,))
		cinfo = db.fetchall()

		conn.close()

		return [finfo, cinfo]

	# This function returns all payment information stored in the table PAYMENT associated with the given ID.
	# The data inside this table should only be changed via the edit function.
	def viewPayment(self,ID):
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()

		db.execute("SELECT * FROM PAYMENT WHERE ID=?", (ID,))
		info = db.fetchall()
		conn.close()

	# This function returns the ID associated with the family that contains the information specified by term. The ID should be given to viewFamily()
	# so that the information can be displayed.
	def searchFamily(self,term):
		ret = []
		conn = sqlite3.connect('Data.db')
		db = conn.cursor()
		db.execute("SELECT * FROM FAMILY WHERE PHONE_NUMBER=?",(term,))
		fam_info = db.fetchall()
		for item in fam_info:
			ret.append(str(item[0]))
		conn. close()

		return ret[0]