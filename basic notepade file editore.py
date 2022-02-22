from tkinter import *
import tkinter.messagebox as tmsg
import os
tk=Tk()

def file_saver():
    if os.path.isdir(entr1.get()):
        path=entr1.get()
        path1=entr2.get()+".txt"
        path=os.path.join(path,path1)
        if not os.path.isfile(path):
            try:
                flobj=open(path,"w")
                flobj.write(txt.get())
                flobj.close()
                tsmg.showinfo("FileSaver","File Saved Succesfully!")
            except:
                tmsg.showwarning("FileSaver","Not able to write in file")
        else:
            tmsg.showwarning("FileSaver","File Already Exixt,try other File name")
    else:
        tmsg.showwarning("FileSaver","Folder not found,Recheck or try other folder")


lblent1=Label(tk,text="Enter full path of folder where you want to save file:")
lblent1.grid(row=0,column=0)


entr1=Entry(tk)
entr1.grid(row=0,column=1)

lblent1=Label(tk,text="File name:")
lblent1.grid(row=1,column=0)

entr2=Entry(tk)
entr2.grid(row=1,column=1)

btn=Button(tk,text="SaveMe",fg="red",bg="yellow",command=file_saver)
btn.grid(row=1,column=2)

txt=Entry(tk,width=200,bg="magenta",fg="green")
txt.place(x=20,y=60)


tk.mainloop()

