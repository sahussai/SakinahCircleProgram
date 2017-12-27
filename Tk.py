from Tkinter import *
from Family import *
from DatabaseAccess import *
from ttk import *
import tkMessageBox
from MainWindow import *
from tkintertable import TableCanvas, TableModel



# This function is called when the Add button is pressed on the
# main window.
def add():
    new_root = Tk()
    new_root.resizable(0,0)

    FatherName_label = Label(new_root, text = 'Name of Father')
    FatherName_label.grid(row = 2, column = 1, padx = 5, pady = 5)
    FatherName_entry = Entry(new_root)
    FatherName_entry.grid(row = 2, column = 2, )

    MotherName_label = Label(new_root, text = 'Name of Mother')
    MotherName_label.grid(row = 3, column = 1, padx = 5, pady = 5)
    MotherName_entry = Entry(new_root)
    MotherName_entry.grid(row = 3, column = 2)

    ChildrenName_label = Label(new_root, text = 'Name(s) of Children\n(Separate with commas)')
    ChildrenName_label.grid(row = 4, column = 1, padx = 5, pady = 5)
    ChildrenName_entry = Entry(new_root)
    ChildrenName_entry.grid(row = 4, column = 2)

    PhoneNumber_label = Label(new_root, text = 'Phone Number(s)\n (Separate with commas)')
    PhoneNumber_label.grid(row = 5, column = 1, padx = 5, pady = 5)
    PhoneNumber_entry = Entry(new_root)
    PhoneNumber_entry.grid(row = 5, column = 2)

    Address_label = Label(new_root, text = 'Home Address\n (Separate with commas)')
    Address_label.grid(row = 6, column = 1, padx = 5, pady = 5)
    Address_entry = Entry(new_root)
    Address_entry.grid(row = 6, column = 2)

    close_button = Button(new_root, text = 'Exit', width = 10 ,command = new_root.destroy)
    close_button.grid(row = 50, column = 50, padx = 5, pady = 5)

    # This function is responsible for creating the Family object, using
    # data collected from the GUI. It runs when the Confirm button is
    # pressed on the Add window.
    def Confirm():
        addy = Address_entry.get()
        phny = PhoneNumber_entry.get()
        children = ChildrenName_entry.get()
        mname = MotherName_entry.get()
        fname = FatherName_entry.get()

        fam = Family(fname,mname)
        fam.addChildren(children)
        fam.set_Address(addy)
        fam.set_phoneNumber(phny)
        fam.generateID()
        fam.updateList()
        dbAccess.save(fam)
        Address_entry.delete(0,'end')
        MotherName_entry.delete(0,'end')
        FatherName_entry.delete(0,'end')
        ChildrenName_entry.delete(0,'end')
        ChildrenName_entry.delete(0,'end')

        tkMessageBox.showinfo(message="Information Added")
        updateList()
        new_root.destroy()


    add_button = Button(new_root, text = 'Confirm', width = 10, command=Confirm)
    add_button.grid(row = 50, column = 49, padx = 5, pady = 5)
    new_root.mainloop()


# This function selects an ID from the listbox and retrieves all information in the table associated with the ID.
def updateList():
    id_List = []
    listbox.delete(0,END);
    id_List = dbAccess.getIDList()
    for item in id_List:
        listbox.insert(END, item)

def deleteEntry():
    if tkMessageBox.askyesno('Delete Family','Are you sure you want to delete this family?'):
        entry = map(int, listbox.curselection())
        id_List = dbAccess.getIDList();
        ID = id_List[entry[0]]
        dbAccess.deleteFamily(ID)
        updateList()
    else:
        tkMessageBox.showinfo('Delete Family','Family not deleted.')

def viewEntry(entry):
    #entry = map(int, listbox.curselection())
    id_List = dbAccess.getIDList();
    ID = id_List[entry[0]]
    [inf1, inf2] = dbAccess.viewFamily(ID)

    finfo = inf1[0]
    cinfo = inf2[0]

    view_root = Tk()
    view_root.resizable(0,0)

    FatherName_label = Label(view_root, text = 'Name of Father:', justify = LEFT)
    FatherName_label.grid(row = 2, column = 1, padx = 5, pady = 5)
    FatherName_label1 = Label(view_root, text = finfo[1])
    FatherName_label1.grid(row = 2, column = 2, )

    MotherName_label = Label(view_root, text = 'Name of Mother:', justify = LEFT)
    MotherName_label.grid(row = 3, column = 1, padx = 5, pady = 5)
    MotherName_label1 = Label(view_root, text = finfo[2])
    MotherName_label1.grid(row = 3, column = 2)

    ChildrenName_label = Label(view_root, text = 'Name(s) of Children\n(Separated with commas):', justify = LEFT)
    ChildrenName_label.grid(row = 4, column = 1, padx = 5, pady = 5)
    ChildrenName_label1 = Label(view_root, text = cinfo[1:])
    ChildrenName_label1.grid(row = 4, column = 2)

    PhoneNumber_label = Label(view_root, text = 'Phone Number(s)\n (Separated with commas):',justify = LEFT)
    PhoneNumber_label.grid(row = 5, column = 1, padx = 5, pady = 5)
    PhoneNumber_label1 = Label(view_root, text = finfo[4])
    PhoneNumber_label1.grid(row = 5, column = 2)

    Address_label = Label(view_root, text = 'Home Address\n (Separated with commas):',justify = LEFT)
    Address_label.grid(row = 6, column = 1, padx = 5, pady = 5)
    Address_label1 = Label(view_root, text = finfo[3])
    Address_label1.grid(row = 6, column = 2)

    def paymentView():
        paymentview_root = Tk()
        paymentview_root.resizable(0,0)

        Sept_label = Label(paymentview_root,text = 'September')
        Sept_label.grid(row = 4, column = 4, padx = 5, pady = 5)
        Oct_label = Label(paymentview_root,text = 'October')
        Oct_label.grid(row = 4, column = 5, padx = 5, pady = 5)
        Nov_label = Label(paymentview_root,text = 'November')
        Nov_label.grid(row = 4, column = 6, padx = 5, pady = 5)
        Dec_label = Label(paymentview_root,text = 'December')
        Dec_label.grid(row = 4, column = 7, padx = 5, pady = 5)
        Jan_label = Label(paymentview_root,text = 'January')
        Jan_label.grid(row = 4, column = 8, padx = 5, pady = 5)
        Feb_label = Label(paymentview_root,text = 'February')
        Feb_label.grid(row = 4, column = 9, padx = 5, pady = 5)
        Mar_label = Label(paymentview_root,text = 'March')
        Mar_label.grid(row = 4, column = 10, padx = 5, pady = 5)
        Apr_label = Label(paymentview_root,text = 'April')
        Apr_label.grid(row = 4, column = 11, padx = 5, pady = 5)
        May_label = Label(paymentview_root,text = 'May')
        May_label.grid(row = 4, column = 12, padx = 5, pady = 5)
        Jun_label = Label(paymentview_root,text = 'June')
        Jun_label.grid(row = 4, column = 14, padx = 5, pady = 5)




        paymentview_root.mainloop()

    payment_button = Button(view_root,text = 'Payments', command = paymentView)
    payment_button.grid(row = 7, column = 1)

    view_root.mainloop()


def search():
    search_root = Tk()
    search_root.resizable(0,0)

    search_label = Label(search_root,text = 'Search Criteria: ', justify = LEFT)
    search_label.grid(row = 3, column = 3, padx = 5, pady = 5)

    search_criteria = Entry(search_root)
    search_criteria.grid(row = 4, column = 4, padx = 5, pady = 5)

    options = ['Father','Mother','Child','Phone Number','Address']
    search_options = Combobox(search_root, values = options)
    search_options.set(options[3]) # Initial value

    search_options.grid(row = 3, column = 4, padx = 5, pady = 5)

    def trySearch():
        ID = dbAccess.searchFamily(search_criteria.get())
        id_List = dbAccess.getIDList()
        entry = int(id_List.index(ID))
        test = [entry]
        viewEntry(test)


    search_ok = Button(search_root,text = 'Search',command = trySearch)
    search_ok.grid(row = 4, column = 5, padx = 5, pady = 5)



    search_root.mainloop()

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)






root = Tk()

gui = MainWindow(root)



# #root.resizable(0,0)
# root.geometry("+700+300")
# familyLabel = Label(root,text="Families:")
# familyLabel.grid(row=2, padx = 5, sticky = W + S)
# root.minsize(width=690, height=420)
# root.maxsize(width=690, height=420)
#
# # All database access operations will be done by this object
# dbAccess = DatabaseAccess()
#
# id_List = dbAccess.getIDList()
#
# scrollbar = Scrollbar(root)
# scrollbar.grid(row = 3,column = 2, rowspan = 3,sticky = N + S)
# #scrollbar.config(height = 16)
#
# listbox = Listbox(root, yscrollcommand=scrollbar.set)
# listbox.config(width=16, height=20)
# listbox.grid(row=3,column = 0,rowspan = 3, padx = 5)
# listbox.bind('<<ListboxSelect>>', onselect)
#
# root.grid_rowconfigure(1, minsize=10)
# root.grid_columnconfigure(4, minsize=50)
# #root.grid_rowconfigure(10, minsize=100)
#
#
# for item in id_List:
#     listbox.insert(END, item)
#
#
# scrollbar.config(command=listbox.yview)
#
#
# add_button = Button(root, text = 'Add' , width = 10, command = add)
# add_button.grid(row = 15, column = 9,padx = 5, pady = 2, sticky = E)
#
# exit_button = Button(root, text = 'Exit', width = 10, command = root.destroy)
# exit_button.grid(row = 15, column = 10,padx = 5, pady = 2, sticky = W)
#
# view_button = Button(root, text = 'View', width = 10, command = lambda: viewEntry(map(int, listbox.curselection())))
# view_button.grid(row = 14, column = 9, padx = 5, pady = 2, sticky = E)
#
# delete_button = Button(root, text = 'Delete', width = 10, command = deleteEntry)
# delete_button.grid(row = 14, column = 10, padx = 5, pady = 2, sticky = W)
#
# search_button = Button(root, text = 'Search', width = 10, command = search)
# search_button.grid(row = 13, column = 10, padx = 5, pady = 2, sticky = W)
#
# edit_button = Button(root, text = 'Edit', width = 10, command = search)
# edit_button.grid(row = 13, column = 9, padx = 5, pady = 2, sticky = E)
#
#
# root.grid_columnconfigure(9, minsize=10)
# root.grid_rowconfigure(5, minsize=5)
#
#
# #root.grid_columnconfigure(7, minsize=100)
# #root.grid_rowconfigure(4, minsize=100)
#
# displayFrame = Frame(root)
#
# height = 5
# width = 5
# for i in range(height): #Rows
#     for j in range(width): #Columns
#         b = Label(displayFrame, text="" , relief = RAISED, width = 10)
#         b.grid(row=i, column=j)
#
# displayFrame.grid(row = 3, column = 7, columnspan =4, rowspan = 10, padx = 5)
#
#



#tframe = Frame(root,width = 20, height  = 5)
#tframe.grid(row = 3, column = 7, columnspan =4)
#table = TableCanvas(tframe, rows = 4, cols = 4, sticky = W)
#table.createTableFrame()




root.mainloop()
