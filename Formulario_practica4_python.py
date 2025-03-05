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
        
        import sys
        if sys.platform.startswith('win'):
            import locale
            locale.setlocale(locale.LC_ALL, 'esp_esp')
        
        # Obtener directorio actual y crear ruta del archivo
        current_dir = os.getcwd()
        self.file_path = os.path.join(current_dir, "registro.txt")
        
        # Crear frame principal
        main_frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(main_frame, text="Registro UNACH 2025", 
                             font=('Arial', 16, 'bold'),
                             bg=bg_color)
        title_label.pack(pady=(10, 30))
        
        # Campos del formulario
        form_frame = tk.Frame(main_frame, bg=bg_color)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        labels = ['Nombre', 'Apellidos', 'Telefono', 'Estatura', 'Edad']
        self.entries = {}
        
        for i, label in enumerate(labels):
            label_frame = tk.Frame(form_frame, bg=bg_color)
            label_frame.pack(fill=tk.X, pady=6
                             )
            
            lbl = tk.Label(label_frame, text=label, font=('Arial', 10, 'bold'),
                    bg=bg_color, anchor='e', width=15)
            lbl.pack(side=tk.LEFT, padx=(10, 10))
            
            self.entries[label] = tk.Entry(label_frame, width=20)
            self.entries[label].pack(side=tk.LEFT)
        
        # Selección de género
        gender_frame = tk.LabelFrame(form_frame, text="Genero", bg=bg_color, 
                                    font=('Arial', 10, 'bold'), padx=10, pady=10)
        gender_frame.pack(fill=tk.X, pady=10, padx=50)
        
        self.gender_var = tk.StringVar()
        tk.Radiobutton(gender_frame, text="Masculino", variable=self.gender_var,
                      value="Masculino", bg=bg_color).pack(side=tk.LEFT, padx=20)
        tk.Radiobutton(gender_frame, text="Femenino", variable=self.gender_var,
                      value="Femenino", bg=bg_color).pack(side=tk.LEFT, padx=20)
        
        # Botones principales (GUARDAR y BORRAR)
        button_frame = tk.Frame(main_frame, bg=bg_color)
        button_frame.pack(pady=20)
        
        # Botón GUARDAR
        self.save_button = tk.Button(button_frame, text="GUARDAR", command=self.save_data,
                                   bg='lime', width=10, height=2)
        self.save_button.pack(side=tk.LEFT, padx=10)
        
        # Botón BORRAR 
        self.clear_button = tk.Button(button_frame, text="BORRAR", command=self.clear_form,
                                    bg='red', width=10, height=2)
        self.clear_button.pack(side=tk.LEFT, padx=10)
        
        # Botón FINALIZAR 
        finish_frame = tk.Frame(main_frame, bg=bg_color)
        finish_frame.pack(fill=tk.X, pady=10)
        self.finish_button = tk.Button(finish_frame, text="FINALIZAR", command=self.finish,
                                     bg='orange', width=10, height=1)
        self.finish_button.pack(side=tk.RIGHT, padx=20)

    def validate_form(self):
        for field, entry in self.entries.items():
            if not entry.get().strip():
                messagebox.showwarning("Error", f"Por favor, complete el campo {field}")
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
            data = (f"Nombre: {self.entries['Nombre'].get()}\n"
                   f"Apellidos: {self.entries['Apellidos'].get()}\n"
                   f"Telefono: {self.entries['Telefono'].get()}\n"
                   f"Estatura: {self.entries['Estatura'].get()}\n"
                   f"Edad: {self.entries['Edad'].get()}\n"
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
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()