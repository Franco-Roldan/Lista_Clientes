from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
import mysql.connector

root = Tk()
root.title("Lista de Clientes")
root.geometry("1200x700")

#Conecto la base de datos y la inicializo

db, c = database()
 
init_db()

# ----------------- 
# FUNCIONES

def mostrar(): # MOSTRAR LISTADO DE REGISTROS 
    c.execute("SELECT * FROM cliente")
    filas = c.fetchall()
    
    tree.delete(*tree.get_children())

    for fila in filas:
        tree.insert("", END, fila[0], values=(fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]))

def insertar(cliente): #INSERTAR LOS DATOS DEL CLIENTE EN LA TABLA
    c.execute("""
                INSERT INTO cliente (dni_cliente, Nombre_Apel, CUIT, mail, tel, direccion, localidad) VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (cliente["DNI"],cliente["Nombre"],cliente["CUIT"],cliente["MAIL"],cliente["Telefono"],cliente["Direccion"],cliente["Localidad"]))    
    db.commit()
    mostrar()

def addCliente(): #OBTENER DATOS DEL CLIENTE Y ENVIARLOS A INSERTAR()

    def guardar(): # FUNCION PARA TOMAR LOS DATOS DEL CLIENTE
        if not  (e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get() and e7.get() ):
            messagebox.showerror("Error","Todos los campos son obligatorios")
            return

        #LOS ATRIBUTOS DEL CLIENTE SE GUARDAN EN UN DICC
        cliente = { 
            "DNI"   : e1.get(),
            "Nombre": e2.get(),
            "CUIT"  : e3.get(),
            "MAIL"  : e4.get(),
            "Telefono" : e5.get(),
            "Direccion": e6.get(),
            "Localidad": e7.get()
        }
        insertar(cliente)
        top.destroy()
    
    #-----------------------------------
    #VENTANA EMERGENTE PARA CARGA DE REGISTRO
    top = Toplevel()
    top.title("Nuevo Cliente")
    top.config(bg="#555")
    top.resizable(0,0)
    
    l1 = Label(top, text="DNI" ,fg="#ffffff", bg="#555")
    e1 = Entry(top, width=40, font=("Arial", 11))
    l1.grid(row=0, column=0,pady=10)
    e1.grid(row=0, column=1, padx=15)

    l2 = Label(top, text="Nombre" ,fg="#ffffff", bg="#555")
    e2 = Entry(top, width=40, font=("Arial", 11))
    l2.grid(row=1, column=0, pady=10)
    e2.grid(row=1, column=1, padx=15)

    l3 = Label(top, text="CUIT" ,fg="#ffffff", bg="#555")
    e3 = Entry(top, width=40, font=("Arial", 11))
    l3.grid(row=2, column=0, pady=10)
    e3.grid(row=2, column=1, padx=15)

    l4 = Label(top, text="MAIL" ,fg="#ffffff", bg="#555")
    e4 = Entry(top, width=40, font=("Arial", 11))
    l4.grid(row=3, column=0,pady=10)
    e4.grid(row=3, column=1, padx=15)

    l5 = Label(top, text="Telefono" ,fg="#ffffff", bg="#555")
    e5 = Entry(top, width=40, font=("Arial", 11))
    l5.grid(row=4, column=0,pady=10)
    e5.grid(row=4, column=1, padx=15)

    l6 = Label(top, text="Dirección" ,fg="#ffffff", bg="#555")
    e6 = Entry(top, width=40, font=("Arial", 11))
    l6.grid(row=5, column=0,pady=10)
    e6.grid(row=5, column=1, padx=15)

    l7 = Label(top, text="Localidad" ,fg="#ffffff", bg="#555")
    e7 = Entry(top, width=40, font=("Arial", 11))
    l7.grid(row=6, column=0,pady=10)
    e7.grid(row=6, column=1, padx=15)


    guardar = Button(top, text="Guardar",padx=20, command=guardar, bg="#66BB6A", font=("Arial", 11))
    guardar.grid(row=7,column=0,columnspan=2,pady=10)

    top.mainloop()
    #-----------------------------------

def deleteCliente(): #ELIMINAR REGISTRO DE LA TABLA

    try:
        id = tree.selection()[0]
        c.execute("SELECT * FROM cliente WHERE id_cliente = %s",(id, ))
        cliente = c.fetchone()
        alerta = messagebox.askokcancel("Advertencia!", "Estas seguro de querer eliminar al cliente "+cliente[2]+" ?")
        if alerta:
            c.execute("DELETE FROM cliente WHERE id_cliente = %s",(id, ))
            db.commit()
            mostrar()
        else: 
            pass
    except: 
        alerta = messagebox.showinfo("Advertencia!", "Seleccione un registro para Eliminarlo")
        
def update(cliente, id_cliente): #ACTUALIZAR DATOS DE REGISTRO
    c.execute("""
                UPDATE cliente SET dni_cliente=%s, Nombre_Apel=%s, CUIT=%s, mail=%s, tel=%s, direccion=%s, localidad=%s where id_cliente = %s
    """, (cliente["DNI"],cliente["Nombre"],cliente["CUIT"],cliente["MAIL"],cliente["Telefono"],cliente["Direccion"],cliente["Localidad"],id_cliente))    
    db.commit()
    mostrar()


def  updateCliente(): #TOMAR LOS DATOS DEL REDISTRO Y ENVIARLOS A LOS ENTRY
    def guardar(): # GUARDO LOS DATOS ACTUALIZADOS DEL REGISTRO Y ENVIARLOS COMO PARAMETROS A UPDATE()
        if not  (e1.get() and e2.get() and e3.get() and e4.get() and e5.get() and e6.get() and e7.get() ):
            messagebox.showerror("Error","Todos los campos son obligatorios")
            return
        
        id_cliente = id
        #LOS ATRIBUTOS DEL CLIENTE SE GUARDAN EN UN DICC
        cliente = { 
            "DNI"   : e1.get(),
            "Nombre": e2.get(),
            "CUIT"  : e3.get(),
            "MAIL"  : e4.get(),
            "Telefono" : e5.get(),
            "Direccion": e6.get(),
            "Localidad": e7.get()
        }
        update(cliente, id_cliente)
        top2.destroy()
    try:
        global id
        id = tree.selection()[0]
        c.execute("SELECT * FROM cliente WHERE id_cliente = %s",(id, ))
        cliente= c.fetchone()

        DatosActual = {
            "DNI" : cliente[1],
            "Nombre" : cliente[2],
            "CUIT" : cliente[3],
            "MAIL" : cliente[4],
            "telefono" : cliente[5],
            "Direccion" : cliente[6],
            "Localidad" : cliente[7]
        }
        #VENTANA EMERGENTE PARA LA ACTUALIZACION DE REGISTROS
        top2 = Toplevel()
        top2.title("Editar Cliente")
        top2.config(bg="#333")
        top2.resizable(0,0)
        
        l1 = Label(top2, text="DNI" ,fg="#ffffff", bg="#333")
        e1 = Entry(top2, width=40)
        e1.insert(0, DatosActual["DNI"])
        l1.grid(row=0, column=0,pady=10)
        e1.grid(row=0, column=1, padx=15)

        l2 = Label(top2, text="Nombre" ,fg="#ffffff", bg="#333")
        e2 = Entry(top2, width=40)
        e2.insert(0, DatosActual["Nombre"])
        l2.grid(row=1, column=0, pady=10)
        e2.grid(row=1, column=1, padx=15)

        l3 = Label(top2, text="CUIT" ,fg="#ffffff", bg="#333")
        e3 = Entry(top2, width=40)
        e3.insert(0, DatosActual["CUIT"])
        l3.grid(row=2, column=0, pady=10)
        e3.grid(row=2, column=1, padx=15)

        l4 = Label(top2, text="MAIL" ,fg="#ffffff", bg="#333")
        e4 = Entry(top2, width=40)
        e4.insert(0, DatosActual["MAIL"])
        l4.grid(row=3, column=0,pady=10)
        e4.grid(row=3, column=1, padx=15)

        l5 = Label(top2, text="Telefono" ,fg="#ffffff", bg="#333")
        e5 = Entry(top2, width=40)
        e5.insert(0, DatosActual["telefono"])
        l5.grid(row=4, column=0,pady=10)
        e5.grid(row=4, column=1, padx=15)

        l6 = Label(top2, text="Dirección" ,fg="#ffffff", bg="#333")
        e6 = Entry(top2, width=40)
        e6.insert(0, DatosActual["Direccion"])
        l6.grid(row=5, column=0,pady=10)
        e6.grid(row=5, column=1, padx=15)

        l7 = Label(top2, text="Localidad" ,fg="#ffffff", bg="#333")
        e7 = Entry(top2, width=40)
        e7.insert(0, DatosActual["Localidad"])
        l7.grid(row=6, column=0,pady=10)
        e7.grid(row=6, column=1, padx=15)


        guardar = Button(top2, text="Guardar", command=guardar, padx=20, bg="#66BB6A", font=("Arial", 11))
        guardar.grid(row=7,column=0,columnspan=2,pady=10)

        top2.mainloop()
        #-----------------------------------
    except: 
        alerta = messagebox.showinfo("Advertencia!", "Seleccione un registro para Actualizarlo")


# INTERFAZ PRINCIPAL

# FRAME DE BOTONES
menu = Frame()
menu.place(x=0,y=0, width=1400, height=120)
menu.config(bg="#555")

titulo = Label(menu, text="Lista de Clientes", font=("Arial", 20), bg="#555", fg="#ffffff")
titulo.place(x=20,y=20,width=250,height=50)

btn = Button(menu, text="Agregar", command=addCliente, font=("Arial", 11))
btn.place(x=10,y=80, width=80, height=30)  

btn2 = Button(menu, text="Eliminar", command=deleteCliente, font=("Arial", 11))
btn2.place(x=100,y=80, width=80, height=30)  

btn3 = Button(menu, text="Editar", command=updateCliente, font=("Arial", 11))
btn3.place(x=190,y=80, width=80, height=30)  

# FRAME PARA TABLA DE REGISTROS
frame2 = Frame()
frame2.place(x=0,y=120,)

tree = ttk.Treeview(frame2)
tree["columns"] = ("DNI", "NOMBRE", "CUIT", "MAIL", "TELEFONO","DIRECCION","LOCALIDAD")

tree.column("#0", width=0, stretch=NO)

tree.column("DNI")
tree.column("NOMBRE")
tree.column("CUIT")
tree.column("MAIL")
tree.column("TELEFONO")
tree.column("DIRECCION")
tree.column("LOCALIDAD")

tree.heading("#0", text= "")
tree.heading("DNI", text= "DNI")
tree.heading("NOMBRE", text= "NOMBRE")
tree.heading("CUIT", text= "CUIT")
tree.heading("MAIL", text= "MAIL")
tree.heading("TELEFONO", text= "TELEFONO")
tree.heading("DIRECCION", text= "DIRECCION")
tree.heading("LOCALIDAD", text= "LOCALIDAD")

tree.grid(column=0,row=0)

mostrar()
root.mainloop()