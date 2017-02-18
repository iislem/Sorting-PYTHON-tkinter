from tkinter import *
import time
from tkinter.messagebox import *

root = Tk()
root.geometry("1600x800+0+0")
root.title("triRapide")

Tops = Frame(root, width=1600, height=50, bg="LightPink1")
Tops.pack(side=TOP)

f1 = Frame(root, width=100, height=700)
f1.pack(side=LEFT)

f2 = Frame(root, width=200, height=700, bg="Pink1")
f2.pack(side=RIGHT)

f3 = Frame(root, width=50, height=300, bg="Pink1")
f3.pack(side=TOP)

f4 = Frame(root, width=300, height=300)
f4.pack(side=TOP)

# ==============================Time==========================
localtime = time.asctime(time.localtime(time.time()))
# ==============================Info==========================
lblInfo = Label(Tops, font=('Script MT Bold', 50, 'bold'), text=" triRapide ", fg="HotPink4")
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('Script MT Bold', 20, 'bold'), text=localtime, fg="HotPink4")
lblInfo.grid(row=1, column=0)
# ===============================Frame2=========================

def Quitter():
    root.destroy()


def Reset():
    num.set("")
    del entries[:]
    del tab[:]
    del labels[:]


# =========================================================================


label = Label(f3, text="=================== Entrer le nombre d'élements à trier   !==================================",
              font=('Script MT Bold', 20)).grid(row=0, column=0)

num = StringVar()
entries = []


def Verification():
    if (num.get()) in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '18', '19', '20']:
        i = 0
        while (i < int(num.get())):
            entries.append(Entry(f1, width=20, bd=2, font=('arial', 12)))
            entries[i].grid(row=i, column=1, padx=2, pady=0)
            i += 1

    else:
        showerror('Erreur', 'Entrer que des entiers <=20 svp!!')

#============================tri=============================



def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)


labels = []

def affiche_tab():
    i = 0
    for item in tab:
        labels.append(Label(f4, width=5,text=item, relief="solid", height=1, padx=2, pady=0))
        labels[i].grid(row=1, column=i + 1, padx=2, pady=0)
        i += 1


tab = []
def triEntry():
    for item in entries:
        tab.append(int(item.get()))
    quickSort(tab)
    affiche_tab()




mEntry = Entry(f3, textvar=num, width=40, font=(15))
mEntry.grid(row=1, column=0)

mbutton = Button(f3, text='OK', font=" arial 12 bold", command=Verification)
mbutton.grid(row=2, column=0)

# ================================================frame3==================

btnTri = Button(f2, padx=30, pady=8, bd=10, fg="black", font=('Script MT Bold', 22), width=7,
                text="Trier", bg="Pink1", command=triEntry).grid(row=1, column=1)

reset_button = Button(f2, padx=30, pady=8, bd=10, fg="black", font=('Script MT Bold', 22), width=7,
                      text="Rénitialiser", bg="Pink1", command=Reset).grid(row=2, column=1)

btnQuitter = Button(f2, padx=30, pady=8, bd=10, fg="black", font=('Script MT Bold', 22), width=7,
                    text="Quitter", bg="Pink1", command=Quitter).grid(row=3, column=1)


root.mainloop()
