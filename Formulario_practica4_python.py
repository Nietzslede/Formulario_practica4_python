import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Registro")
        bg_color = 'MediumPurple'
        self.root.configure(bg=bg_color)
        
        # Establecer la codificación por defecto
        import sys
        if sys.platform.startswith('win'):
            import locale
            locale.setlocale(locale.LC_ALL, 'esp_esp')
        
        # Obtener directorio actual y crear ruta del archivo
        current_dir = os.getcwd()
        self.file_path = os.path.join(current_dir, "registro.txt")
        
        # Crear frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        style = ttk.Style()
        style.configure('TFrame', background=bg_color)
        style.configure('TLabelframe', background=bg_color)
        style.configure('TLabelframe.Label', background=bg_color)
        
        # Título
        title_label = tk.Label(main_frame, text="Registro UNACH 2025", 
                             font=('Microsoft YaHei UI', 12, 'bold'),
                             bg='MediumPurple')
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Campos del formulario
        labels = ['Nombre:', 'Apellidos:', 'Telefono:', 'Estatura:', 'Edad:']
        self.entries = {}
        
        for i, label in enumerate(labels):
            tk.Label(main_frame, text=label, font=('Microsoft Sans Serif', 8, 'bold'),
                    bg='MediumPurple').grid(row=i+1, column=0, pady=10, padx=10, sticky=tk.W)
            self.entries[label] = tk.Entry(main_frame)
            self.entries[label].grid(row=i+1, column=1, pady=10, padx=10)
        
        # Selección de género
        gender_frame = ttk.LabelFrame(main_frame, text="Genero", padding="10")
        gender_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.W+tk.E)
        
        self.gender_var = tk.StringVar()
        tk.Radiobutton(gender_frame, text="Masculino", variable=self.gender_var,
                      value="Masculino", bg='MediumPurple').pack(side=tk.LEFT, padx=20)
        tk.Radiobutton(gender_frame, text="Femenino", variable=self.gender_var,
                      value="Femenino", bg='MediumPurple').pack(side=tk.LEFT, padx=20)
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)
        
        tk.Button(button_frame, text="GUARDAR", command=self.save_data,
                 bg='lime').pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="FINALIZAR", command=self.finish,
                 bg='orange').pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="BORRAR", command=self.clear_form,
                 bg='red').pack(side=tk.LEFT, padx=10)

    def validate_form(self):
        for field, entry in self.entries.items():
            if not entry.get().strip():
                messagebox.showwarning("Error", "Por favor, complete todos los campos")
                return False
        if not self.gender_var.get():
            messagebox.showwarning("Error", "Por favor, seleccione un genero")
            return False
        return True

    def save_data(self):
        if not self.validate_form():
            return
            
        # Crear el archivo si no existe
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                pass
            
        try:
            data = (f"Nombre: {self.entries['Nombre:'].get()}\n"
                   f"Apellidos: {self.entries['Apellidos:'].get()}\n"
                   f"Telefono: {self.entries['Telefono:'].get()}\n"
                   f"Estatura: {self.entries['Estatura:'].get()}\n"
                   f"Edad: {self.entries['Edad:'].get()}\n"
                   f"Genero: {self.gender_var.get()}\n"
                   f"Fecha de registro: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                   "----------------------------------------\n")
                
            with open(self.file_path, 'a', encoding='utf-8') as file:
                file.write(data)
            messagebox.showinfo("Exito", "Datos guardados exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los datos: {str(e)}")

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.gender_var.set('')

    def finish(self):
        if self.validate_form():
            self.save_data()
            messagebox.showinfo("Finalizado", 
                              "Registro finalizado. Los datos han sido guardados.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()