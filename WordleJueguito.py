import tkinter as tk
import random

palabras_posibles = ["perro", "gatos", "raton", "luzco", "calor", "campo", "piano"]
palabra_del_dia = random.choice(palabras_posibles)
MAX_INTENTOS = 6
intentos = MAX_INTENTOS
fila_actual = 0
matriz_entries = []
resultado_final = None

def palabra_correcta(palabra, objetivo):
    resultado = []
    usada = [False] * len(objetivo)

    for i in range(len(palabra)):
        if palabra[i] == objetivo[i]:
            resultado.append(f"[{palabra[i]}]")
            usada[i] = True
        else:
            resultado.append(None)

    for i in range(len(palabra)):
        if resultado[i] is not None:
            continue
        if palabra[i] in objetivo:
            for j in range(len(objetivo)):
                if palabra[i] == objetivo[j] and not usada[j]:
                    resultado[i] = f"({palabra[i]})"
                    usada[j] = True
                    break
        if resultado[i] is None:
            resultado[i] = palabra[i]

    return resultado

root = tk.Tk()
root.title("Wordle Tkinter Modo Oscuro")
root.configure(bg="#121212") 

etiqueta_intentos = tk.Label(root, text=f"Te quedan {intentos} intentos", font=('Helvetica', 14),
                            fg="#EEEEEE", bg="#121212")
etiqueta_intentos.pack(pady=5)

frame_resultado = tk.Frame(root, bg="#121212")
frame_resultado.pack(pady=10)

def crear_tablero():
    global matriz_entries, fila_actual, resultado_final, intentos, palabra_del_dia
    for widget in frame_resultado.winfo_children():
        widget.destroy()
    if resultado_final:
        resultado_final.destroy()
    matriz_entries = []
    fila_actual = 0
    intentos = MAX_INTENTOS
    palabra_del_dia = random.choice(palabras_posibles)
    etiqueta_intentos.config(text=f"Te quedan {intentos} intentos")

    for fila in range(MAX_INTENTOS):
        fila_entries = []
        for col in range(len(palabra_del_dia)):
            entry = tk.Entry(frame_resultado, width=2, font=('Helvetica', 24, 'bold'),
                             justify="center", bg="#1E1E1E", fg="#EEEEEE", insertbackground="#EEEEEE",
                             disabledbackground="#1E1E1E", disabledforeground="#EEEEEE", relief="flat")
            entry.grid(row=fila, column=col, padx=5, pady=5)
            entry.config(state="disabled")
            entry.bind("<KeyRelease>", lambda e, f=fila, c=col: manejar_tecla(e, f, c))
            fila_entries.append(entry)
        matriz_entries.append(fila_entries)

    activar_fila(0)

def activar_fila(fila):
    for entry in matriz_entries[fila]:
        entry.config(state="normal")
        entry.delete(0, tk.END)
    matriz_entries[fila][0].focus_set()

def manejar_tecla(evento, fila, col):
    entrada = matriz_entries[fila][col]
    texto = entrada.get()
    if len(texto) > 1:
        entrada.delete(1, tk.END)
        texto = entrada.get()
    if texto and texto.isalpha():
        if col < len(palabra_del_dia) - 1:
            matriz_entries[fila][col + 1].focus_set()
    elif evento.keysym == "BackSpace":
        if col > 0 and not texto:
            matriz_entries[fila][col - 1].focus_set()

def leer_palabra_de_fila(fila):
    letras = []
    for entry in matriz_entries[fila]:
        letras.append(entry.get().lower())
    return ''.join(letras)

def mostrar_resultado(resultado):
    global fila_actual
    for i, letra in enumerate(resultado):
        color = "#2E2E2E"  
        fg_color = "white"
        if letra.startswith("["):
            color = "#388E3C"  
            letra = letra[1:-1]
        elif letra.startswith("("):
            color = "#FBC02D"  
            fg_color = "white"
            letra = letra[1:-1]
        matriz_entries[fila_actual][i].delete(0, tk.END)
        matriz_entries[fila_actual][i].insert(0, letra.upper())
        matriz_entries[fila_actual][i].config(state="disabled", disabledbackground=color, disabledforeground=fg_color)

    fila_actual += 1
    if fila_actual < MAX_INTENTOS:
        activar_fila(fila_actual)

def confirmar(event=None):
    global intentos, palabra_del_dia, resultado_final

    palabra = leer_palabra_de_fila(fila_actual)
    if len(palabra) != len(palabra_del_dia):
        return

    resultado = palabra_correcta(palabra, palabra_del_dia)
    mostrar_resultado(resultado)

    if palabra == palabra_del_dia:
        resultado_final = tk.Label(root, text="¡Ganaste! 🎉 Nueva palabra...", fg="#81C784", bg="#121212",
                                  font=('Helvetica', 16, 'bold'))
        resultado_final.pack(pady=10)
        palabra_del_dia = random.choice(palabras_posibles)
        intentos = MAX_INTENTOS
        etiqueta_intentos.config(text=f"Te quedan {intentos} intentos")
        root.after(2000, crear_tablero)
    else:
        intentos -= 1
        etiqueta_intentos.config(text=f"Te quedan {intentos} intentos")
        if intentos == 0:
            resultado_final = tk.Label(root, text=f"Game Over 😵\nLa palabra era '{palabra_del_dia.upper()}'",
                                      fg="#E57373", bg="#121212", font=('Helvetica', 16, 'bold'))
            resultado_final.pack(pady=10)
            for fila in matriz_entries:
                for entry in fila:
                    entry.config(state="disabled")
        else:
            activar_fila(fila_actual)

crear_tablero()
root.bind("<Return>", confirmar)
root.mainloop()
