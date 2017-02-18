from tkinter import *
import time
from tkinter.messagebox import *

root = Tk()
root.geometry("1600x800+0+0")
root.title("triComptage")

Tops = Frame(root, width=1600, height=50, bg="pale green")
Tops.pack(side=TOP)

f1 = Frame(root, width=100, height=700)
f1.pack(side=LEFT)

f2 = Frame(root, width=200, height=700, bg="pale green")
f2.pack(side=RIGHT)

f3 = Frame(root, width=50, height=300, bg="pale green")
f3.pack(side=TOP)

f4 = Frame(root, width=300, height=300)
f4.pack(side=TOP)

# =======================Time======================
localtime = time.asctime(time.localtime(time.time()))
# =======================Info======================
lblInfo = Label(Tops, font=('Script MT Bold', 50, 'bold'), text="triComptage", fg="sea green")
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('Script MT Bold', 20, 'bold'), text=localtime, fg="sea green")
lblInfo.grid(row=1, column=0)


# =========================================================================


def Quitter():
    root.destroy()


def Reset():
    num.set("")
    del entries[:]
    del tab[:]
    del labels[:]


# ========================================================================


label = Label(f3, text="=================== Entrer le nombre d'élements à trier   !==================================",
              font=('Script MT Bold', 20)).grid(row=0, column=0)

num = StringVar()
entries = []


def Verification():
    if (num.get()) in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '14', '15', '18', '19', '20']:
        i = 0
        while (i < int(num.get())):
            entries.append(Entry(f1, width=20, bg="pale green", bd=2, font=('arial', 12)))
            entries[i].grid(row=i, column=1)
            i += 1

    else:
        showerror('Erreur', 'Entrer que des entiers <=20 svp!!')


# ============================tri=============================

maxval = 200

def counting_sort(array,maxval):
    #Initialisation des variables
    m = maxval + 1
    #Initialisation du tableau de comptage à 0
    count = [0] * m
    #Création du tableau de comptage
    for a in array:
        count[a] += 1
    #Création du tableau trié
    i = 0
    for a in range(m):
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return (array,count)


labels = []


def affiche_tab():
    i = 0
    for item in tab:
        labels.append(Label(f4, width=5, text=item, relief="solid", height=1, padx=2, pady=0))
        labels[i].grid(row=1, column=i + 1, padx=2, pady=0)
        i += 1


tab = []


def triEntry():
    for item in entries:
        tab.append(int(item.get()))
    counting_sort(tab, maxval)
    affiche_tab()


mEntry = Entry(f3, textvar=num, width=40, font=(15))
mEntry.grid(row=1, column=0)

mbutton = Button(f3, text='OK', font=" arial 12 bold", command=Verification)
mbutton.grid(row=2, column=0)

# ================================================frame3==================
btnTri = Button(f2, padx=30, pady=8, bd=16, fg="black", font=('Script MT Bold', 22), width=7,
                text="Trier", bg="pale green", command=triEntry).grid(row=1, column=1)

reset_button = Button(f2, padx=30, pady=8, bd=16, fg="black", font=('Script MT Bold', 22), width=7,
                      text="Rénitialiser", bg="pale green", command=Reset).grid(row=2, column=1)

btnQuitter = Button(f2, padx=30, pady=8, bd=16, fg="black", font=('Script MT Bold', 22), width=7,
                    text="Quitter", bg="pale green", command=Quitter).grid(row=3, column=1)



root.mainloop()
