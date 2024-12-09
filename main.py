import tkinter as tk
from tkinter import ttk, messagebox

def mostrar_frame(frame):
    # Oculta todos los frames
    for f in frames.values():
        f.pack_forget()
    # Muestra el frame seleccionado
    frame.pack(fill="both", expand=True)

def procesar_descarga(tipo):
    url = url_entry.get().strip()
    if url:
        messagebox.showinfo("Descarga", f"Descargando {tipo} de: {url}")
    else:
        messagebox.showwarning("Error", "Por favor, ingresa una URL válida.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Descargas de YouTube")
root.geometry("960x460")
root.resizable(False, False)

# Crear un contenedor para los frames
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Diccionario para almacenar los frames
frames = {}

# Frame inicial (pantalla de bienvenida)
frame_bienvenida = tk.Frame(main_frame)
ttk.Label(frame_bienvenida, text="Bienvenido al Gestor de Descargas", font=("Helvetica", 16)).pack(pady=50)
frames["bienvenida"] = frame_bienvenida

# Frame para descargar video
frame_video = tk.Frame(main_frame)
ttk.Label(frame_video, text="Descargar Video de YouTube", font=("Helvetica", 14)).pack(pady=10)
url_entry = ttk.Entry(frame_video, width=50)
url_entry.pack(pady=10)
ttk.Button(frame_video, text="Descargar Video", command=lambda: procesar_descarga("video")).pack(pady=10)
frames["video"] = frame_video

# Frame para descargar audio
frame_audio = tk.Frame(main_frame)
ttk.Label(frame_audio, text="Descargar Audio de YouTube", font=("Helvetica", 14)).pack(pady=10)
url_entry = ttk.Entry(frame_audio, width=50)
url_entry.pack(pady=10)
ttk.Button(frame_audio, text="Descargar Audio", command=lambda: procesar_descarga("audio")).pack(pady=10)
frames["audio"] = frame_audio



# Menú
menu_bar = tk.Menu(root)
menu_descargas = tk.Menu(menu_bar, tearoff=0)
menu_descargas.add_command(label="Menu Principal", command=lambda: mostrar_frame(frames["bienvenida"]))
menu_descargas.add_command(label="Descargar Video", command=lambda: mostrar_frame(frames["video"]))
menu_descargas.add_command(label="Descargar Audio", command=lambda: mostrar_frame(frames["audio"]))
menu_bar.add_cascade(label="Opciones", menu=menu_descargas)

# Configurar el menú
root.config(menu=menu_bar)

# Mostrar el frame de bienvenida al inicio
mostrar_frame(frames["bienvenida"])

# Ejecutar aplicación
root.mainloop()
