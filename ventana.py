from doctest import master
from tkinter import Entry, Label, Frame, Misc, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END, Toplevel
from typing import Any
from conexion import Registro_datos

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        frame1 = Frame(master, bg="#082338")
        frame1.place(x=0, y=0, width=300, height=1080)
        frame2 = Frame(master, bg="gray")
        frame2.place(x=300, y=0, width=225, height=1080)
        frame3 = Frame(master, bg="gray")
        frame3.place(x=526, y=0, width=1400, height=1020)

        self.buscar = StringVar()  # Define la variable de búsqueda
        self.btnnuevo = Button(frame1, text="Buscar", command=self.buscar_nombre, bg="white", fg="black", font=10)
        Entry(frame1, textvariable=self.buscar, font=('Arial', 12), width=24).place(x=40, y=10)  # Asigna self.buscar aquí
        
        self.btnnuevo.place(x=45, y=40, width=210, height=25)

        self.btnmodificar = Button(frame1, text="Modificar", command=self.agregar_datos, bg="white", fg="black", font=10)
        self.btnmodificar.place(x=45, y=75, width=210, height=25)

        self.legajo = StringVar()
        self.Apellido_y_nombre = StringVar()
        self.direccion = StringVar()
        self.localidad = StringVar()
        self.cp = StringVar()
        self.fecha_ingreso = StringVar()
        self.Antigüedad = StringVar()
        self.Fecha_Nacimiento = StringVar()
        self.Edad = StringVar()
        self.DNI = StringVar()
        self.nro = StringVar()
        self.cat = StringVar()
        self.oficina = StringVar()
        self.Nombre_Oficina = StringVar()
        self.Secretaria = StringVar()
        self.sindicato = StringVar()
        self.Sepelio = StringVar()
        self.Mutual = StringVar()
        self.solo_4 = StringVar()
        self.Seguro = StringVar()
        self.Coseguro = StringVar()
        self.PUESTO = StringVar()
        self.SEXO = StringVar()        
        self.ANTIGÜEDAD = StringVar()
        self.ESTUDIO = StringVar()
        self.buscar = StringVar()
        self.busca_producto = StringVar()
        self.Nro_De_Afiliado = StringVar()
        self.Fecha_De_Afiliacion = StringVar()
        self.basededatos = Registro_datos()
        
        
        lbl1= Label(frame2, text = 'Legajo',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=0)
        lbl1= Label(frame2, text = 'Apellido y Nombre',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=34)
        lbl1= Label(frame2, text ='Direccion',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=68)
        lbl1= Label(frame2, text ='Localidad', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=102)
        lbl1= Label(frame2, text ='Cp',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=136)
        lbl1= Label(frame2, text ='Fecha Ingreso',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=170)
        lbl1= Label(frame2, text ='Antigüedad',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=204)
        lbl1= Label(frame2, text ='Fecha Nacimiento', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=238)
        lbl1= Label(frame2, text ='Edad',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=272)
        lbl1= Label(frame2, text ='DNI',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=306)
        lbl1= Label(frame2, text ='Nro',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=340)
        lbl1= Label(frame2, text = 'Cat',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=374)           
        lbl1= Label(frame2, text = 'Sindicato',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=408)           
        lbl1= Label(frame2, text = 'Oficina',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=442)                    
        lbl1= Label(frame2, text = 'Nombre Oficina',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=476)                    
        lbl1= Label(frame2, text = 'Secretaria',fg='white', bg ='gray', font=(7))   
        lbl1.place(x=3, y= 510)                     
        lbl1= Label(frame2, text = 'Sindicato', fg='white',bg ='gray', font=(7))  
        lbl1.place(x=3, y=544)                        
        lbl1= Label(frame2, text = 'Sepelio',fg='white', bg ='gray', font=(7))    
        lbl1.place(x=3, y=578)                        
        lbl1= Label(frame2, text = 'Mutual',fg='white', bg ='gray', font=(7))   
        lbl1.place(x=3, y=612)                       
        lbl1= Label(frame2, text = 'Solo 4',fg='white', bg ='gray', font=(7)) 
        lbl1.place(x=3, y=646)                      
        lbl1= Label(frame2, text = 'Coseguro',fg='white', bg ='gray', font=(7))
        lbl1.place(x=3, y=680)                   
        lbl1= Label(frame2, text = 'Seguro', fg='white',bg ='gray', font=(7))
        lbl1.place(x=3, y=714)                    
        lbl1= Label(frame2, text = 'Puesto',fg='white', bg ='gray', font=(7))        
        lbl1.place(x=3, y=748)                    
        lbl1= Label(frame2, text = 'Sexo',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=782)                   
        lbl1= Label(frame2, text = 'Antiguedad',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=816)                    
        lbl1= Label(frame2, text = 'Estudio',fg='white', bg ='gray', font=(7))            
        lbl1.place(x=3, y=850) 
        lbl1= Label(frame2, text = 'Nro De Afiliado',fg='white', bg ='gray', font=(7))      
        lbl1.place(x=3, y=884)                    
        lbl1= Label(frame2, text = 'Fecha De Afiliacion',fg='white', bg ='gray', font=(7))            
        lbl1.place(x=3, y=918) 
            
        self.nombre=Entry(frame2,textvariable=self.legajo )
        self.nombre.place(x=3, y=21, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Apellido_y_nombre )
        self.nombre.place(x=3, y=55, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.direccion )
        self.nombre.place(x=3, y=89, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.localidad)
        self.nombre.place(x=3, y=123, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.cp)
        self.nombre.place(x=3, y=157, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.fecha_ingreso)        
        self.nombre.place(x=3, y=191, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Antigüedad )
        self.nombre.place(x=3, y=225, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Fecha_Nacimiento )
        self.nombre.place(x=3, y=259, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Edad)
        self.nombre.place(x=3, y=293, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.DNI )
        self.nombre.place(x=3, y=327, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.nro)
        self.nombre.place(x=3, y=361, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.cat)
        self.nombre.place(x=3, y=395, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.oficina )
        self.nombre.place(x=3, y=429, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Nombre_Oficina)
        self.nombre.place(x=3, y=463, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Secretaria)
        self.nombre.place(x=3, y=497, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.sindicato)
        self.nombre.place(x=3, y=531, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Sepelio)
        self.nombre.place(x=3, y=565, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Mutual)
        self.nombre.place(x=3, y=599, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.solo_4)
        self.nombre.place(x=3, y=633, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Coseguro)
        self.nombre.place(x=3, y=667, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Seguro)
        self.nombre.place(x=3, y=701, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.PUESTO)
        self.nombre.place(x=3, y=735, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.SEXO)
        self.nombre.place(x=3, y=769, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.ANTIGÜEDAD)
        self.nombre.place(x=3, y=803, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.ESTUDIO)
        self.nombre.place(x=3, y=837, width=200, height=16)
        self.nombre=Entry(frame2)
        self.nombre.place(x=3, y=871, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Nro_De_Afiliado)
        self.nombre.place(x=3, y=905, width=200, height=16)
        self.nombre=Entry(frame2,textvariable=self.Fecha_De_Afiliacion)
        self.nombre.place(x=3, y=939, width=200, height=16)
            
        self.tabla = ttk.Treeview(frame3, height=40)
        self.tabla.pack(fill='both', expand=True)   

        ladox = Scrollbar(frame3, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.place(x=0, y=1000, relwidth=0.9, height=20)  
        
        ladoy = Scrollbar(frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.place(x=1375, y=0, width=20, relheight=0.9) 
   
   
        frame3.rowconfigure(0, weight=1)
        self.tabla['columns'] = (
    'legajo', 'apellido_y_nombre', 'direccion', 'localidad', 'cp', 'fecha_ingreso', 
    'antiguedad', 'fecha_de_nacimiento', 'edad', 'dni', 'nro', 'cat', 'oficina', 
    'nombre_oficina', 'secretaria', 'sindicato', 'sepelio', 'mutual', 'solo_4', 
    'coseguro', 'seguro', 'puesto', 'sexo', 'antigüedad', 'estudio', 
    'Nro_De_Afiliado', 'Fecha_De_Afiliacion'
        )       
        self.mostrar_todo()   
        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.tabla.column('0', minwidth=150, width=10 , anchor='center')
        self.tabla.column('1', minwidth=350, width=300 , anchor='center' )
        self.tabla.column('2', minwidth=250, width=10 , anchor='center')
        self.tabla.column('3', minwidth=250, width=10 , anchor='center')
        self.tabla.column('4', minwidth=90, width=90, anchor='center')
        self.tabla.column('5', minwidth=150, width=10 , anchor='center')
        self.tabla.column('6', minwidth=150, width=10 , anchor='center' )
        self.tabla.column('7', minwidth=150, width=10 , anchor='center')
        self.tabla.column('8', minwidth=50, width=10 , anchor='center')
        self.tabla.column('9', minwidth=50, width=10 , anchor='center')
        self.tabla.column('10', minwidth=150, width=10 , anchor='center')
        self.tabla.column('11', minwidth=90, width=90 , anchor='center' )
        self.tabla.column('12', minwidth=150, width=10 , anchor='center')
        self.tabla.column('13', minwidth=300, width=30, anchor='center')
        self.tabla.column('14', minwidth=300, width=10 , anchor='center')
        self.tabla.column('15', minwidth=70, width=10 , anchor='center')
        self.tabla.column('16', minwidth=50, width=10, anchor='center' )
        self.tabla.column('17', minwidth=50, width=10 , anchor='center')
        self.tabla.column('18', minwidth=50, width=10, anchor='center')
        self.tabla.column('19', minwidth=70, width=10, anchor='center')
        self.tabla.column('20', minwidth=50, width=10 , anchor='center')
        self.tabla.column('21', minwidth=300, width=10, anchor='center' )
        self.tabla.column('22', minwidth=50, width=10 , anchor='center')
        self.tabla.column('24', minwidth=90, width=10, anchor='center')
        self.tabla.column('23', minwidth=60, width=10, anchor='center')
        self.tabla.column('25', minwidth=90, width=10, anchor='center')
        self.tabla.column('26', minwidth=150, width=30, anchor='center')
        
        self.tabla.heading('0', text='legajo', anchor ='center')
        self.tabla.heading('1', text='Apellido_y_nombre', anchor ='center')
        self.tabla.heading('2', text='direccion', anchor ='center')
        self.tabla.heading('3', text='localidad', anchor ='center')
        self.tabla.heading('4', text='CP', anchor ='center')
        self.tabla.heading('5', text='fecha ingreso', anchor ='center')
        self.tabla.heading('6', text='Antigüedad', anchor ='center')
        self.tabla.heading('7', text='Fecha Nacimiento', anchor ='center')
        self.tabla.heading('8', text='Edad', anchor ='center')
        self.tabla.heading('9', text='DNI', anchor ='center')
        self.tabla.heading('10', text='nro', anchor ='center')
        self.tabla.heading('11', text='cat', anchor ='center')
        self.tabla.heading('12', text='oficina', anchor ='center')
        self.tabla.heading('13', text='Nombre Oficina', anchor ='center')
        self.tabla.heading('14', text='Secretaria', anchor ='center')
        self.tabla.heading('15', text='sindicato', anchor ='center')
        self.tabla.heading('16', text='Sepelio', anchor ='center')
        self.tabla.heading('17', text='Mutual', anchor ='center')
        self.tabla.heading('18', text='solo_4', anchor ='center')
        self.tabla.heading('19', text='Coseguro', anchor ='center')
        self.tabla.heading('20', text='Seguro', anchor ='center')
        self.tabla.heading('21', text='puesto', anchor ='center')
        self.tabla.heading('22', text='sexo', anchor ='center')
        self.tabla.heading('24', text='antigüedad', anchor ='center')
        self.tabla.heading('23', text='estudio', anchor ='center')
        self.tabla.heading('25', text='Nro de afiliado', anchor ='center')
        self.tabla.heading('26', text='Fecha de afiliacion', anchor ='center')            
        estilo = ttk.Style(frame3)
        
        estilo.theme_use('default') #  ('clam', 'alt', 'default', 'classic')            estilo.configure(".",font= (12), foreground='#082338')        
        estilo.configure("Treeview", font= (10), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'gray')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
            
    def agregar_datos(self):
        self.tabla.focus()
        datos = (
            self.legajo.get(), self.Apellido_y_nombre.get(), self.direccion.get(), self.localidad.get(), self.cp.get(), 
            self.fecha_ingreso.get(), self.Antigüedad.get(), self.Fecha_Nacimiento.get(), self.Edad.get(), self.DNI.get(), 
            self.nro.get(), self.cat.get(), self.oficina.get(), self.Nombre_Oficina.get(), self.Secretaria.get(), 
            self.sindicato.get(), self.Sepelio.get(), self.Mutual.get(), self.solo_4.get(), self.Coseguro.get(), 
            self.Seguro.get(), self.PUESTO.get(), self.SEXO.get(), self.ANTIGÜEDAD.get(), self.ESTUDIO.get(), 
            self.Nro_De_Afiliado.get(), self.Fecha_De_Afiliacion.get()
        )
        
        self.tabla.insert('', 0, text=datos[0], values=datos)
        self.basededatos.inserta_datos(datos)
        
        for var in [
            self.legajo, self.Apellido_y_nombre, self.direccion, self.localidad, self.cp, self.fecha_ingreso, 
            self.Antigüedad, self.Fecha_Nacimiento, self.Edad, self.DNI, self.nro, self.cat, self.oficina, 
            self.Nombre_Oficina, self.Secretaria, self.sindicato, self.Sepelio, self.Mutual, self.solo_4, 
            self.Coseguro, self.Seguro, self.PUESTO, self.SEXO, self.ANTIGÜEDAD, self.ESTUDIO, 
            self.Nro_De_Afiliado, self.Fecha_De_Afiliacion
        ]:
            var.set("")

    def buscar_nombre(self):
        valor = self.buscar.get()  # Obtener el valor de búsqueda desde self.buscar
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla
        for row in self.basededatos.buscar_datos(valor):
            self.tabla.insert('', 0, text=row[0], values=row)

    def mostrar_todo(self):
        registros = self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)
        for row in self.basededatos.mostrar_legajo():
            self.tabla.insert('', 0, text=row[0], values=row)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        
        data = self.tabla.item(current_item)
        values = data['values']
        self.legajo.set(values[0])
        self.Apellido_y_nombre.set(values[1])
        self.direccion.set(values[2])
        self.localidad.set(values[3])
        self.cp.set(values[4])
        self.fecha_ingreso.set(values[5])
        self.Antigüedad.set(values[6])
        self.Fecha_Nacimiento.set(values[7])
        self.Edad.set(values[8])
        self.DNI.set(values[9])
        self.nro.set(values[10])
        self.cat.set(values[11])
        self.oficina.set(values[12])
        self.Nombre_Oficina.set(values[13])
        self.Secretaria.set(values[14])
        self.sindicato.set(values[15])
        self.Sepelio.set(values[16])
        self.Mutual.set(values[17])
        self.solo_4.set(values[18])
        self.Coseguro.set(values[19])
        self.Seguro.set(values[20])
        self.PUESTO.set(values[21])
        self.SEXO.set(values[22])
        self.ANTIGÜEDAD.set(values[23])
        self.ESTUDIO.set(values[24])
        self.Nro_De_Afiliado.set(values[25])
        self.Fecha_De_Afiliacion.set(values[26])

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        
        data = self.tabla.item(current_item)
        values = data['values']
        self.legajo.set(values[0])
        self.Apellido_y_nombre.set(values[1])
        self.direccion.set(values[2])
        self.localidad.set(values[3])
        self.cp.set(values[4])
        self.fecha_ingreso.set(values[5])
        self.Antigüedad.set(values[6])
        self.Fecha_Nacimiento.set(values[7])
        self.Edad.set(values[8])
        self.DNI.set(values[9])
        self.nro.set(values[10])
        self.cat.set(values[11])
        self.oficina.set(values[12])
        self.Nombre_Oficina.set(values[13])
        self.Secretaria.set(values[14])
        self.sindicato.set(values[15])
        self.Sepelio.set(values[16])
        self.Mutual.set(values[17])
        self.solo_4.set(values[18])
        self.Coseguro.set(values[19])
        self.Seguro.set(values[20])
        self.PUESTO.set(values[21])
        self.SEXO.set(values[22])
        self.ANTIGÜEDAD.set(values[23])
        self.ESTUDIO.set(values[24])
        self.Nro_De_Afiliado.set(values[25])
        self.Fecha_De_Afiliacion.set(values[26])
