from tkinter import *
from tkinter import messagebox
from random import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import copy
re_get=0
i=0
got_i=0
root=Tk()
listbox=Listbox(root,selectmode=EXTENDED)
listbox_yougot=Listbox(root,selectmode=EXTENDED)
root.title("Rinachan Lots")
root.geometry("700x700")
root.resizable(0,0)
keys={}
yougots={}
def download():
    if len(keys)==0:
        messagebox.showwarning("error!", "please input value more than 1.")
        return
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    k_keys=[]
    for kk in keys.keys():
        k_keys.append(int(kk))
    for i in range(len(k_keys)):
        text2save = keys[k_keys[i]]+'\n'
        f.write(text2save)
    f.close()
def openfile():
    filename = filedialog.askopenfilename()

    fileHandle = open(filename, 'r')
    getFromFile=(fileHandle.read()).split('\n')
    for j in range(len(getFromFile)):
        global i
        if(getFromFile[j]==''):
            continue
        keys[i] = getFromFile[j]
        listbox.insert(i, getFromFile[j])
        input_box.delete("0", END)
        i = i + 1
    fileHandle.close()
def random_select():
    if int(len(keys))==0:
        messagebox.showwarning("error!", "please input value more than 1.")
        return
    global i
    check_value=[]
    for keysss in keys.keys():
        check_value.append(int(keysss))
    print(check_value)
    keys_value=check_value[randrange(0,len(check_value))]
    print(keys_value)
    newArray=[]
    global got_i
    for j in yougots.keys():
        newArray.append(int(j))
    if got_i in newArray:
        got_i=0
        print("hi")
        for k in newArray:
            if(got_i==int(k)):
                got_i+=1
            elif(got_i!=int(k)):
                break
    global re_get
    re_get=check_value
    yougots[got_i]=keys[keys_value]
    listbox_yougot.insert(got_i,yougots[got_i])
    messagebox.showinfo("What You Get!", keys[keys_value])
    var.set(f"What You Got: {keys[keys_value]}")
    got_i+=1
    print(yougots.keys())

def delete_all():
    if int(len(keys))==0:
        messagebox.showwarning("error!", "lot box is empty!.")
        return
    listbox.delete(0,END)
    global i
    i=0
    keys.clear()
def delete_button():
    try:
        selected = listbox.get(listbox.curselection())
        print(selected)
        global i
        i=i-1
        for key,value in keys.items():
            if value==selected:
                key_find=key
        del keys[key_find]
        listbox.delete(ANCHOR)
    except:
        return

def insert_fun(event):
    if(Entry.get(input_box)==""):
        messagebox.showwarning("error!","please input value")
        return
    global i
    newArray=[]
    for j in keys.keys():
        newArray.append(int(j))
    if i in newArray:
        print("3")
        i=0
        for k in newArray:
            if(i==int(k)):

                i+=1
            elif(i!=int(k)):
                break

    keys[i]=Entry.get(input_box)
    listbox.insert( i,Entry.get(input_box))
    i = i + 1
    input_box.delete("0",END)


input_box = Entry(root, width=20)
fileUpload_Button=Button(width=10,text="upload lots",command=openfile)
fileDownload_Button=Button(width=10,text="download lots",command=download)
delete=Button(width=10,text="delete this",command=delete_button)
delete.place(x=50,y=625)
fileUpload_Button.place(x=160,y=650)
delete_all=Button(width=10,text="delete All",command=delete_all)
fileDownload_Button.place(x=50,y=650)
delete_all.place(x=160,y=625)
input_box.place(x=255,y=20)
random=Button(width=10,text="Drawing Lots",command=random_select)
random.place(x=300,y=60)
listbox.place(x=50, y=100, width=200, height=500)
listbox_yougot.place(x=450,y=100,width=200,height=500)
var=StringVar()
Text_Slot=Label(root,textvariable=var,font=('Arial',20))
Text_Slot2=Label(root,text="Type and press enter!",font=('Arial',20))
def delete_got():
    try:
        selected = listbox_yougot.get(listbox_yougot.curselection())
        print(selected)
        global got_i
        got_i=got_i-1
        for key,value in yougots.items():
            if value==selected:
                key_find=key
        del yougots[key_find]
        listbox_yougot.delete(ANCHOR)
        print(yougots.keys())
    except:
        return

delete_got=Button(width=10,text="delete this lot",command=delete_got)
delete_got.place(x=450,y=625)

def delete_all_got():
    if int(len(yougots))==0:
        messagebox.showwarning("error!", "Drawing First!")
        return
    listbox_yougot.delete(0,END)
    global got_i
    got_i=0
    yougots.clear()
delete_all_got=Button(width=10,text="delete all",command=delete_all_got)
delete_all_got.place(x=560,y=625)

def download_yougot():
    if len(yougots) == 0:
        messagebox.showwarning("error!", "please draw!")
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    got_kk=[]
    for c in yougots.keys():
        got_kk.append(int(c))
    for i in range(len(yougots)):
        text2save = yougots[got_kk[i]]+'\n'
        f.write(text2save)
    f.close()
download_got=Button(width=22,text="download those",command=download_yougot)
download_got.place(x=450,y=650)
root.bind('<Return>', insert_fun)

def swap_button():
    if len(yougots)==0:
        messagebox.showwarning("error!", "Drawing First!")
        return

    global keys
    keys.clear()
    keys=copy.deepcopy(yougots)
    listbox.delete(0, END)
    global i
    i=0
    for k in range(len(yougots)):
        listbox.insert(k, keys[k])
        i=i+1



swap_button=Button(width=15,text="<-move to lots",command=swap_button)
swap_button.place(x=280,y=265)
Text_Slot2.place(x=20,y=20)
Text_Slot.place(x=450,y=65)
root.mainloop()