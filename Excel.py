import openpyxl as xl
from Tkinter import *
import json
from Family import *


wb = xl.load_workbook('Test.xlsx')
print(wb.get_sheet_names())
ws = wb['Data']
Parent_names = []

for row in range(2,278):
    name = ws.cell(column = 2, row = row).value
    if name == None:
        continue
    else:
        index = name.find('/')
        if index == -1:
            Parent_names.append(name.strip())
        else:
            fname = name[0:index].strip()
            mname = name[index+1:].strip()
            Parent_names.append(name[0:index].strip())
            Parent_names.append(name[index+1:].strip())


print(99)

def addFamily(fname, mname, children, address, phonenum):
    fam = Family(fname,mname)
    fam.addChildren(children)
    fam.set_Address(address)
    fam.set_phoneNumber(phonenum)
    fam.generateID()
    fam.set_Fees()
    fam.save()

def test():
    print(FatherName_entry.get())
    fam = Family(FatherName_entry.get(),MotherName_entry.get())
    fam.addChildren(ChildrenName_entry.get())
    fam.set_Address(Address_entry.get())
    fam.set_phoneNumber(PhoneNumber_entry.get())
    fam.generateID()
    fam.set_Fees()
    fam.save()

root = Tk()

#Empty_label =Label(root, text = '')
#Empty_label.grid(row = 1, columnspan  = 20)

FatherName_label = Label(root, text = 'Name of Father')
FatherName_label.grid(row = 2, column = 1, padx = 5, pady = 5)
FatherName_entry = Entry(root)
fname = FatherName_entry.get()
FatherName_entry.grid(row = 2, column = 2, )

MotherName_label = Label(root, text = 'Name of Mother')
MotherName_label.grid(row = 3, column = 1, padx = 5, pady = 5)
MotherName_entry = Entry(root)
mname = MotherName_entry.get()
MotherName_entry.grid(row = 3, column = 2)

ChildrenName_label = Label(root, text = 'Name(s) of Children\n(Separate with commas)')
ChildrenName_label.grid(row = 4, column = 1, padx = 5, pady = 5)
ChildrenName_entry = Entry(root)
children = ChildrenName_entry.get()
ChildrenName_entry.grid(row = 4, column = 2)

PhoneNumber_label = Label(root, text = 'Phone Number(s)\n (Separate with commas)')
PhoneNumber_label.grid(row = 5, column = 1, padx = 5, pady = 5)
PhoneNumber_entry = Entry(root)
PhoneNumber_entry.grid(row = 5, column = 2)

Address_label = Label(root, text = 'Home Address\n (Separate with commas)')
Address_label.grid(row = 6, column = 1, padx = 5, pady = 5)
Address_entry = Entry(root)
Address_entry.grid(row = 6, column = 2)

close_button = Button(root, text = 'Exit', command = root.quit, width = 10)
close_button.grid(row = 50, column = 50, padx = 5, pady = 5)

add_button = Button(root, text = 'Add', width = 10, command=test )
add_button.grid(row = 50, column = 49, padx = 5, pady = 5)
root.mainloop()


