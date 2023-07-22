from tkinter import *


window=Tk()
window.minsize(width=400,height=400)
window.title("FOR EGZERSİZE AND NOTE")
window.config(padx=20,pady=20)
window.config(bg="#03D1FB")
my_lab=Label(window)
my_lab.config(fg="red")
my_lab.config(text="WELCOME")
my_lab.pack()
def ileri():
    window2=Tk()
    window2.minsize(width=400,height=400)
    labelw = Label(window2)
    labelw.config(text="username")
    labelw.pack()
    ent3=Entry(window2)
    ent3.config(width=30)
    ent3.pack()
    labela = Label(window2)
    labela.config(text="password")
    labela.pack()
    ent4 =Entry(window2)
    ent4.config(width=30)
    ent4.pack()

    def giris2():
        message_label = Label()
        bilgi3 = ent3.get()
        bilgi4 = ent4.get()
        if bilgi3=="osman123" and bilgi4=="1234":
            message_label = Label(window2)
            message_label.config(text="giriş başarılı!",fg="green")
            message_label.pack()

        elif bilgi3 != "osman123" or bilgi4 !="1234":
            message_label = Label(window2)
            message_label.config(text="hatalı kullanıcı adı ya da şifre", fg="red")
            message_label.pack()

        message_label = Label(window2)
        message_label.config(text="", font=("Arial", 20, "bold"))
        message_label.pack()
    but56 = Button(window2)
    but56.config(text="giriş yap!")
    but56.pack(side="bottom" and "right")
    but56.config(command=giris2)
    def page3():
        win3=Tk()
        win3.config(bg="green")
        win3.config(padx=20,pady=20)
        win3.minsize(width=340,height=340)
        win3.title("İŞLEMLER")
        label45=Label(win3)
        label45.config(text="Aşağıdaki günlerden herhangi birini seçerek notlar alabilirsiniz")
        label45.config(width=50,height=8)
        label45.pack(anchor="s")
        mylistbox=Listbox(win3)
        days_list=["notlarım","e devlet şifrem","instagram şifrem","twitter şifrem"]
        for x in range(len(days_list)):
                mylistbox.insert(x,days_list[x])
        text34=Text(win3)
        text34.config(bg="black",fg="white")
        def select_days(event):
             items=mylistbox.get(mylistbox.curselection())
             text34.insert(END,items)
             text34.pack()

        mylistbox.bind('<<ListboxSelect>>',select_days)
        mylistbox.pack()








    but89=Button(window2)
    but89.config(text="ileri")
    but89.config(command=page3)
    but89.pack()

my_but=Button(window)
my_but.config(text="ileri")
my_but.config(command=ileri)
my_but.pack(side="bottom" and "right")

lab2=Label(text="isminizi nedir ? :")
lab2.config(fg="Black")
lab2.config(bg="yellow")
lab2.config(padx=20,pady=20)
lab2.pack()
ent=Entry(window)
ent.config(width=30)
ent.pack()

lab5=Label(window)
lab5.config(text="soyisminizi giriniz :")
lab5.config(fg="Black")
lab5.config(bg="light blue")
lab5.config(padx=20,pady=20)
lab5.pack()
ent2=Entry(window)
ent2.config(width=30)
ent2.pack()
def kaydet(bilgi1,bilgi2):
    bilgi1=ent.get()
    bilgi2=ent2.get()


but2=Button(window)
but2.config(text="kaydet")
but2.config(bg="white")
but2.pack()
def sil():
    ent.delete(0,END)
    ent2.delete(0,END)
mybut3=Button(window)
mybut3.config(text="Silmek için tıklayınız")
mybut3.config(command=sil)
mybut3.pack(side="bottom"and"left")




window.mainloop()
















