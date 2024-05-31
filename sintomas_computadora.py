import tkinter as tk
from tkinter import ttk, messagebox

# Definición de signos de alerta
signos_alerta = [
    '¿Aparecen pantallazos azules al abrir aplicaciones o juegos?',
    '¿El PC o portátil tarda bastante en arrancar?',
    '¿El equipo hace pitidos cuando se enciende?',
    '¿Pueden producirse errores al instalar nuevos programas?',
    '¿El PC se vuelve más lento cuanto más tiempo está encendido?',
    '¿El sistema impide acceder a ciertos archivos del disco duro?',
    '¿Bloqueos repentinos del ratón o teclado?',
    '¿La memoria RAM no es reconocida por el dispositivo?',
    '¿El sistema operativo muestra una falta de memoria RAM?'
]

class TestSignosApp:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Test de Signos de Alerta")
        self.root.geometry("500x300")
        self.root.configure(bg="#f0f0f0")

        # Configuración de estilos
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 14), wraplength=400)

        # Inicialización de variables
        self.responses = []  # Lista para almacenar las respuestas del usuario
        self.current_question = 0  # Índice de la pregunta actual
        
        # Crear un marco para contener los widgets
        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(expand=True)
        
        # Crear una etiqueta para mostrar las preguntas
        self.label = ttk.Label(self.frame, text=signos_alerta[self.current_question])
        self.label.pack(pady=20)
        
        # Crear un marco para los botones de respuesta
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(pady=20)

        # Crear botón "Sí" y asociar la función de registro de respuestas
        self.yes_button = ttk.Button(self.button_frame, text="Sí", command=lambda: self.record_response('si'))
        self.yes_button.pack(side=tk.LEFT, padx=10)
        
        # Crear botón "No" y asociar la función de registro de respuestas
        self.no_button = ttk.Button(self.button_frame, text="No", command=lambda: self.record_response('no'))
        self.no_button.pack(side=tk.RIGHT, padx=10)
    
    def record_response(self, response):
        # Función para registrar la respuesta del usuario y pasar a la siguiente pregunta
        self.responses.append(response)
        self.current_question += 1
        if self.current_question < len(signos_alerta):
            # Actualizar la etiqueta con la siguiente pregunta
            self.label.config(text=signos_alerta[self.current_question])
        else:
            # Si no hay más preguntas, calcular el resultado
            self.calculate_result()
    
    def calculate_result(self):
        # Función para calcular el resultado basado en las respuestas del usuario
        conteo_si = self.responses.count('si')  # Contar cuántas respuestas "sí" hay
        if conteo_si >= 6:
            resultado = "¡Probablemente hay un problema grave con la memoria RAM! es recomendable revisarlas o cambiarla"
        elif conteo_si >= 3:
            resultado = "Puede haber un problema con la memoria RAM. Es recomendable revisarla para evitar problemas."
        else:
            resultado = "La memoria RAM parece estar funcionando correctamente puedes continuar sin problemas."
        
        # Mostrar el resultado en un cuadro de diálogo
        messagebox.showinfo("Resultado", f'Respondiste "sí" a {conteo_si} signos de alerta.\nResultado: {resultado}')
        self.root.destroy()  # Cerrar la ventana principal

if __name__ == "__main__":
    # Inicializar la aplicación
    root = tk.Tk()
    app = TestSignosApp(root)
    root.mainloop()  # Ejecutar el bucle principal de Tkinter


#Commit realizado por Revanngel. Saludos
