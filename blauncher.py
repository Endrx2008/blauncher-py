import subprocess
import os
import tkinter as tk
from tkinter import messagebox

def Menu_tab():
    # Funzione che crea e mostra il menu iniziale
    for widget in frame.winfo_children():
        widget.destroy()  # Pulisce il frame prima di aggiungere il menu

    # Aggiungi le opzioni del menu principale
    label_menu = tk.Label(frame, text="Menu", font=("Arial", 16))
    label_menu.pack(pady=10)

    # Creazione delle opzioni nel menu
    button_option1 = tk.Button(frame, text="Shutdown", command=lambda: os.system ("sudo shutdown now"))
    button_option1.pack(pady=5)

    button_option2 = tk.Button(frame, text="Reboot", command=lambda: os.system ("sudo shutdown -r now"))
    button_option2.pack(pady=5)

    button_option2 = tk.Button(frame, text="Suspend", command=lambda: os.system ("systemctl suspend"))
    button_option2.pack(pady=5)

    # Pulsante per tornare indietro al menu principale
    button_exit = tk.Button(frame, text="Back", command=lambda: main())  # Torna al menu
    button_exit.pack(pady=5)

def Ap_tab():
    # Funzione che crea e mostra il menu del sottomenu
    for widget in frame.winfo_children():
        widget.destroy()  # Pulisce il frame prima di aggiungere il sottomenu

    # Aggiungi le opzioni del sottomenu
    label_menu = tk.Label(frame, text="Launcher", font=("Arial", 16))
    label_menu.pack(pady=10)

    # Creazione delle opzioni nel sottomenu
    button_option1 = tk.Button(frame, text="Firefox", command=lambda: subprocess.run(["firefox"]))
    button_option1.pack(pady=5)

    button_option2 = tk.Button(frame, text="Terminal", command=lambda: subprocess.run(["kitty"]))
    button_option2.pack(pady=5)

    button_option3 = tk.Button(frame, text="Thunar", command=lambda: subprocess.run(["Thunar"]))
    button_option3.pack(pady=5)

    # Pulsante per tornare indietro al menu principale
    button_exit = tk.Button(frame, text="Back", command=lambda: main())  # Torna al menu
    button_exit.pack(pady=5)

# Funzione per avviare le applicazioni
def main():
    # Funzione che crea e mostra il menu del sottomenu
    for widget in frame.winfo_children():
        widget.destroy()  # Pulisce il frame prima di aggiungere il sottomenu

    # Aggiungi le opzioni del sottomenu
    label_menu = tk.Label(frame, text="Home", font=("Arial", 16))
    label_menu.pack(pady=10)

    # Creazione delle opzioni nel sottomenu
    button_option1 = tk.Button(frame, text="Boot Menu", command=lambda: Menu_tab())
    button_option1.pack(pady=5)

    button_option2 = tk.Button(frame, text="Launcher", command=lambda: Ap_tab())
    button_option2.pack(pady=5)

# Creazione della finestra principale
root = tk.Tk()
root.title("MENU - Menu")
root.geometry("300x300")

# Creazione di un frame per i pulsanti
frame = tk.Frame(root)
frame.pack(pady=20)

# Creazione del pulsante per uscire dall'app
exit_button = tk.Button(root, text="Esci", command=root.quit)
exit_button.pack(pady=20)

# start della funzione principale
main()

# Avvio della finestra grafica
root.mainloop()
