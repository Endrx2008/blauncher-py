#!/usr/bin/env python3
import sys
import os
import subprocess
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QStackedWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QColor, QPalette, QFont

class CommandExecutor(QMainWindow):
    # Percorso delle icone (modifica se necessario)
    icon_path = '/home/endrx/Scrivania/codes/python/pyblauncher/Private/'

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Command Executor GUI")
        self.setGeometry(100, 100, 500, 400)
        self.set_dark_palette()

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Creazione dei menu tramite una funzione helper
        self.main_menu = self.create_menu(
            title="Home",
            buttons=[
                {"text": "Sys manager", "callback": self.show_system_menu},
                {"text": "Applications", "callback": self.show_application_menu,
                 "icon": os.path.join(self.icon_path, 'app-icon.png')},
                {"text": " Exit ", "callback": self.close,
                 "icon": os.path.join(self.icon_path, 'close-icon.png')}
            ],
            title_font_size=20
        )

        self.system_menu = self.create_menu(
            title="Sys Commands",
            buttons=[
                {"text": "", "callback": lambda: self.execute_command("shutdown"),
                 "icon": os.path.join(self.icon_path, 'system-icon.png'),
                 "style": "background-color: red; color: black;"},
                {"text": "", "callback": lambda: self.execute_command("reboot"),
                 "icon": os.path.join(self.icon_path, 'reboot-icon.png'),
                 "style": "background-color: green; color: black;"},
                {"text": "", "callback": lambda: self.execute_command("suspend"),
                 "icon": os.path.join(self.icon_path, 'suspend-icon.png'),
                 "style": "background-color: blue; color: black;"},
                {"text": "", "callback": self.show_main_menu,
                 "icon": os.path.join(self.icon_path, 'back-icon.png')}
            ],
            title_font_size=18
        )

        self.application_menu = self.create_menu(
            title="App Launcher",
            buttons=[
                {"text": "Firefox", "callback": lambda: self.execute_command("firefox"),
                 "style": "background-color: blue; color: black;"},
                {"text": "Github", "callback": lambda: self.execute_command("git"),
                 "style": "background-color: blue; color: black;"},
                {"text": "GPT", "callback": lambda: self.execute_command("GPT"),
                 "style": "background-color: blue; color: black;"},
                {"text": "Codium", "callback": lambda: self.execute_command("cdm"),
                 "icon": os.path.join(self.icon_path, '/usr/share/icons/Sours-Full-Color/apps/scalable/codium.svg'),
                 "style": "background-color: #FF7F50; color: black;"},
                {"text": "Arduino", "callback": lambda: self.execute_command("ard"),
                 "style": "background-color: white; color: black;"},
                {"text": "Gimp", "callback": lambda: self.execute_command("gimp"),
                 "style": "background-color: brown; color: black;"},
                {"text": "Filemanager", "callback": lambda: self.execute_command("pcmn"),
                 "style": "background-color: green; color: black;"},
                {"text": "Okular", "callback": lambda: self.execute_command("klr"),
                 "style": "background-color: orange; color: black;"},
                {"text": "Discord", "callback": lambda: self.execute_command("dis"),
                 "style": "background-color: purple; color: black;"},
                {"text": "", "callback": self.show_main_menu,
                 "icon": os.path.join(self.icon_path, 'back-icon.png')}
            ],
            title_font_size=18
        )

        # Aggiungi i menu al widget centrale
        self.central_widget.addWidget(self.main_menu)
        self.central_widget.addWidget(self.system_menu)
        self.central_widget.addWidget(self.application_menu)
        self.central_widget.setCurrentWidget(self.main_menu)

        # Timer per aggiornare l'interfaccia ogni 5 secondi
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_ui)
        self.timer.start(5000)

    def set_dark_palette(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(30, 30, 30))
        palette.setColor(QPalette.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.Window, QColor(50, 50, 50))
        self.setPalette(palette)

    def create_menu(self, title, buttons, title_font_size):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        title_label = QLabel(title)
        title_label.setStyleSheet("color: yellow;")
        title_label.setFont(QFont("Arial", title_font_size, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        for btn in buttons:
            button = QPushButton(btn.get("text", ""))
            if "icon" in btn:
                button.setIcon(QIcon(btn["icon"]))
            if "style" in btn:
                button.setStyleSheet(btn["style"])
            button.clicked.connect(btn["callback"])
            layout.addWidget(button)
        return widget

    def refresh_ui(self):
        self.update()

    def show_main_menu(self):
        self.central_widget.setCurrentWidget(self.main_menu)

    def show_system_menu(self):
        self.central_widget.setCurrentWidget(self.system_menu)

    def show_application_menu(self):
        self.central_widget.setCurrentWidget(self.application_menu)

    def execute_command(self, command):
        def run_command():
            try:
                if command == "shutdown":
                    os.system("kitty -e sudo shutdown now")
                elif command == "reboot":
                    os.system("kitty -e sudo shutdown -r now")
                elif command == "suspend":
                    os.system("systemctl suspend")
                elif command == "dis":
                    os.system("discord")
                elif command == "klr":
                    os.system("okular")
                elif command == "firefox":
                    subprocess.run(["firefox"], check=True)
                elif command == "gimp":
                    subprocess.run(["/home/endrx/.gimp"], check=True)
                elif command == "git":
                    subprocess.run(["firefox", "https://github.com/"], check=True)
                elif command == "cdm":
                    subprocess.run(["codium"], check=True)
                elif command == "ard":
                    subprocess.run(["arduino"], check=True)
                elif command == "GPT":
                    subprocess.run(["firefox", "https://chatgpt.com"], check=True)
                elif command == "pcmn":
                    subprocess.run(["pcmanfm-qt"], check=True)
            except Exception as e:
                print(f"Errore eseguendo {command}: {e}")
        threading.Thread(target=run_command, daemon=True).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommandExecutor()
    window.show()
    sys.exit(app.exec_())
