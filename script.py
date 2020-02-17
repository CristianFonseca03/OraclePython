import cx_Oracle
from tkinter import *
from tkinter import messagebox
import sys
import json

window = Tk()
window.title("Distribuidos")

window.geometry('700x200')

lbl = Label(window, text="Ingrese la consulta a ejecutar")
 
lbl.grid(column=0, row=0)

txt = Entry(window,width=60)
 
txt.grid(column=1, row=0)

def clicked():
    btn.config(state="disable")
    try:
        conn_str='HR/1234@127.0.0.1:1521/XE'
        db_conn = cx_Oracle.connect(conn_str)
        conn_str_1='HR/1234@10.57.4.235:1521/XE'
        db_conn_1 = cx_Oracle.connect(conn_str_1)
        conn_str_2='HR/1234@10.57.4.68:1521/XE'
        db_conn_2 = cx_Oracle.connect(conn_str_2)
    except cx_Oracle.DatabaseError:
        messagebox.showerror("Error", "Ha ocurrido un error al conectar.")
        sys.exit(0)
    else:
        cursor = db_conn.cursor()
        cursor_1 = db_conn_1.cursor()
        cursor_2 = db_conn_2.cursor()
        try:
            cursor.execute(txt.get())
            cursor_1.execute(txt.get())
            cursor_2.execute(txt.get())
        except cx_Oracle.DatabaseError:
            messagebox.showerror("Error", "Sentencia SQL no valida.")
            btn.config(state="normal")
        else:
            db_conn.commit()
            db_conn_1.commit()
            db_conn_2.commit()
            messagebox.showinfo("Mensaje", "Sentencias ejecutadas con exito")
            btn.config(state="normal")
            
btn = Button(window, text="Ejecutar", command=clicked)
 
btn.grid(column=2, row=0)

window.mainloop()
