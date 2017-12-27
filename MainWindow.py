from Tkinter import *
from ttk import *
from Family import *
from DatabaseAccess import *
import tkMessageBox



class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Sakinah Circle Program")
        master.geometry("+700+300")
        familyLabel = Label(master, text="Families:")
        familyLabel.grid(row=2, padx=5, sticky=W + S)
        master.minsize(width=690, height=420)
        master.maxsize(width=690, height=420)

        # All database access operations will be done by this object
        dbAccess = DatabaseAccess()

        id_List = dbAccess.getIDList()

        scrollbar = Scrollbar(master)
        scrollbar.grid(row=3, column=2, rowspan=3, sticky=N + S)
        # scrollbar.config(height = 16)

        listbox = Listbox(master, yscrollcommand=scrollbar.set)
        listbox.config(width=16, height=20)
        listbox.grid(row=3, column=0, rowspan=3, padx=5)
        listbox.bind('<<ListboxSelect>>', onselect)

        master.grid_rowconfigure(1, minsize=10)
        master.grid_columnconfigure(4, minsize=50)
        # master.grid_rowconfigure(10, minsize=100)


        for item in id_List:
            listbox.insert(END, item)

        scrollbar.config(command=listbox.yview)

        # add_button = Button(master, text='Add', width=10, command=add)
        # add_button.grid(row=15, column=9, padx=5, pady=2, sticky=E)

        exit_button = Button(master, text='Exit', width=10, command=master.destroy)
        exit_button.grid(row=15, column=10, padx=5, pady=2, sticky=W)

        # view_button = Button(master, text='View', width=10, command=lambda: viewEntry(map(int, listbox.curselection())))
        # view_button.grid(row=14, column=9, padx=5, pady=2, sticky=E)

        delete_button = Button(master, text='Delete', width=10, command=lambda : deleteEntry(listbox,dbAccess))
        delete_button.grid(row=14, column=10, padx=5, pady=2, sticky=W)

        search_button = Button(master, text='Search', width=10, command=search)
        search_button.grid(row=13, column=10, padx=5, pady=2, sticky=W)

        edit_button = Button(master, text='Edit', width=10, command=search)
        edit_button.grid(row=13, column=9, padx=5, pady=2, sticky=E)

        master.grid_columnconfigure(9, minsize=10)
        master.grid_rowconfigure(5, minsize=5)

        # master.grid_columnconfigure(7, minsize=100)
        # master.grid_rowconfigure(4, minsize=100)

        displayFrame = Frame(master)

        height = 5
        width = 5
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                b = Label(displayFrame, text="", relief=RAISED, width=10)
                b.grid(row=i, column=j)

        displayFrame.grid(row=3, column=7, columnspan=4, rowspan=10, padx=5)



def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)


def trySearch():
    ID = dbAccess.searchFamily(search_criteria.get())
    id_List = dbAccess.getIDList()
    entry = int(id_List.index(ID))
    test = [entry]
    viewEntry(test)

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

    search_ok = Button(search_root,text = 'Search',command = trySearch)
    search_ok.grid(row = 4, column = 5, padx = 5, pady = 5)


def updateList(listbox,dbAccess):
    id_List = []
    listbox.delete(0,END);
    id_List = dbAccess.getIDList()
    for item in id_List:
        listbox.insert(END, item)

def deleteEntry(listbox, dbAccess):
    if tkMessageBox.askyesno('Delete Family','Are you sure you want to delete this family?'):
        entry = map(int, listbox.curselection())
        id_List = dbAccess.getIDList();
        ID = id_List[entry[0]]
        dbAccess.deleteFamily(ID)
        updateList(listbox,dbAccess)
    else:
        tkMessageBox.showinfo('Delete Family','Family not deleted.')



