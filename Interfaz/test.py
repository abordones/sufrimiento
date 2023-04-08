import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import os
import pandas as pd


from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.geometry('800x600')
        self.title('Horario de clases')

        # Barra superior
        menu_bar = tk.Menu(self)
        horario_menu = tk.Menu(menu_bar, tearoff=0)
        horario_menu.add_command(label='Horario actual', command=self.open_horario_window)
        horario_menu.add_command(label='Profesores', command=self.open_profesores_window)
        horario_menu.add_command(label='Estudiantes', command=self.open_estudiantes_window)
        horario_menu.add_command(label='Salas', command=self.open_salas_window)
        horario_menu.add_command(label='Asignaturas', command=self.open_asignaturas_window)
        menu_bar.add_cascade(label='Horario', menu=horario_menu)
        self.config(menu=menu_bar)

        # Barra inferior
        contact_label = tk.Label(self, text='Contáctenos', font='Helvetica 12 bold')
        contact_label.pack(side=tk.BOTTOM, pady=10)

        # Separador
        separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)

        # Centro
        self.horario_frame = tk.Frame(self)
        self.horario_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

        self.horario_label = tk.Label(self.horario_frame, text='Horario de clases', font='Helvetica 16 bold')
        self.horario_label.pack(side=tk.TOP, pady=5)

        self.horario_tree = ttk.Treeview(self.horario_frame)
        self.horario_tree.pack(fill=tk.BOTH, expand=1)

        # Botón de carga
        load_button = tk.Button(self.horario_frame, text='Cargar horario', font='Helvetica 12 bold', command=lambda: self.load())
        load_button.pack(pady=10)

        # Cargar archivo de ejemplo
        file_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, "ConexionBDD", "horario_ejemplo.xlsx"))
        self.load()

    def open_horario_window(self):
        messagebox.showinfo('Horario', 'Abrir ventana de horario')

    def open_profesores_window(self):
        messagebox.showinfo('Profesores', 'Abrir ventana de profesores')

    def open_estudiantes_window(self):
        messagebox.showinfo('Estudiantes', 'Abrir ventana de estudiantes')

    def open_salas_window(self):
        messagebox.showinfo('Salas', 'Abrir ventana de salas')

    def open_asignaturas_window(self):
        # Abrir ventana de asignaturas
        asignaturas_window = tk.Toplevel(self)
        asignaturas_window.geometry('400x400')
        asignaturas_window.title('Asignaturas')

        # Separador
        separator = tk.Frame(asignaturas_window, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)

        # Centro
        asignaturas_frame = tk.Frame(asignaturas_window)
        asignaturas_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

        asignaturas_label = tk.Label(asignaturas_frame, text='Asignaturas', font='Helvetica 16 bold')
        asignaturas_label.pack(side=tk.TOP, pady=5)

        # Tabla de asignaturas
        asignaturas_tree = ttk.Treeview(asignaturas_frame, name='asignaturas_tree')
        asignaturas_tree.pack(fill=tk.BOTH, expand=1)

        # Cargar archivo de ejemplo
        file_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, "ConexionBDD", "asignaturas_ejemplo.xlsx"))
        asignaturas_df = pd.read_excel(file_path)

        # Convertir el dataframe en una lista de tuplas
        asignaturas_data = [tuple(x) for x in asignaturas_df.values]

        # Configurar columnas del Treeview
        asignaturas_tree['columns'] = asignaturas_df.columns
        for col in asignaturas_df.columns:
            asignaturas_tree.heading(col, text=col)

        # Insertar datos en el Treeview
        for row in asignaturas_data:
            asignaturas_tree.insert("", "end", values=row)

    def load(self):
        # Cargar archivo de horario
        file_path = filedialog.askopenfilename(filetypes=[('Archivo de Excel', '*.xlsx')])
        if file_path:
            # Cargar el archivo excel usando pandas
            horario_df = pd.read_excel(file_path)

            # Convertir el dataframe en una lista de tuplas
            horario_data = [tuple(x) for x in horario_df.values]

            # Eliminar cualquier widget existente en el frame de horario
            for widget in self.horario_frame.winfo_children():
                widget.destroy()

            # Configurar columnas del Treeview
            self.horario_tree['columns'] = horario_df.columns
            for col in horario_df.columns:
                self.horario_tree.heading(col, text=col)

            # Insertar datos en el Treeview
            for row in horario_data:
                self.horario_tree.insert("", "end", values=row)


    def load_asignaturas(self):
        file_path = filedialog.askopenfilename(filetypes=[('Archivo de Excel', '*.xlsx')])
        if file_path:
            # Cargar el archivo excel usando pandas
            asignaturas_df = pd.read_excel(file_path)

            # Convertir el dataframe en una lista de tuplas
            asignaturas_data = [tuple(x) for x in asignaturas_df.values]

            # Eliminar cualquier widget existente en el frame de asignaturas
            if hasattr(self, 'horario_tree'):
                self.horario_tree.destroy()

            # Crear un Treeview para mostrar la tabla
            asignaturas_tree = ttk.Treeview(self.asignaturas_frame, columns=asignaturas_df.columns, show='headings')
            for col in asignaturas_df.columns:
                asignaturas_tree.heading(col, text=col)
            for row in asignaturas_data:
                asignaturas_tree.insert("", "end", values=row)
            asignaturas_tree.pack(fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    # Creación de la ventana principal
    main_window = MainWindow()

    # Configuración
    main_window.mainloop()