import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.geometry('400x300')
        self.title('Mi ventana principal')

        # Creación de un botón
        self.button = tk.Button(self, text='Mi botón', command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.5, anchor='center')

    def on_button_click(self):
        print('¡El botón fue clickeado!')

if __name__ == '__main__':
    # Creación de la ventana principal
    main_window = MainWindow()
    main_window.mainloop()
