import tkinter as tk
import tkinter.filedialog as filedialog
import os

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

        self.horario_text = tk.Text(self.horario_frame, height=20, width=80, font='Helvetica 12')
        self.horario_text.pack(padx=10, pady=10)

        # Botón de carga
        load_button = tk.Button(self.horario_frame, text='Cargar horario', font='Helvetica 12 bold', command=self.load_horario)
        load_button.pack(pady=10)

        # Cargar archivo de ejemplo
        with open(f"{os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))}\ConexionBDD\horario_ejemplo.txt") as f:
            horario_text = f.read()
        self.horario_text.insert('end', horario_text)

    def open_horario_window(self):
        messagebox.showinfo('Horario', 'Abrir ventana de horario')

    def open_profesores_window(self):
        messagebox.showinfo('Profesores', 'Abrir ventana de profesores')

    def open_estudiantes_window(self):
        messagebox.showinfo('Estudiantes', 'Abrir ventana de estudiantes')

    def open_salas_window(self):
        messagebox.showinfo('Salas', 'Abrir ventana de salas')

    def open_asignaturas_window(self):
        messagebox.showinfo('Asignaturas', 'Abrir ventana de asignaturas')

    def load_horario(self):
        file_path = filedialog.askopenfilename(filetypes=[('Archivo de texto', '*.txt')])
        if file_path:
            with open(file_path) as f:
                horario_text = f.read()
            self.horario_text.delete('1.0', 'end')
            self.horario_text.insert('end', horario_text)

if __name__ == '__main__':
    # Creación de la ventana principal
    main_window = MainWindow()

    # Configuración
    main_window.mainloop()

