#!/usr/bin/env python3
import sys
import os
import subprocess
import threading
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QStackedWidget, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QColor, QPalette, QFont

class CommandExecutor(QMainWindow):
    # Variabile per il percorso delle icone
    icon_path = ''  # Sostituisci con il percorso della cartella in cui salvi le immagini png

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Command Executor GUI")
        self.setGeometry(100, 100, 500, 400)
        
        # Apply a dark palette for a modern look
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Background, QColor(30, 30, 30))
        dark_palette.setColor(QPalette.Button, QColor(50, 50, 50))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Window, QColor(50, 50, 50))
        self.setPalette(dark_palette)

        # Central widget and stacked layout
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Main menu
        self.main_menu = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_menu.setLayout(self.main_layout)

        # Add title to main menu
        self.main_title = QLabel("Home")
        self.main_title.setFont(QFont("Arial", 20, QFont.Bold))
        self.main_title.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.main_title)

        # Buttons for submenus with modern icons
        self.system_menu_button = QPushButton("Sys manager")
        self.system_menu_button.clicked.connect(self.show_system_menu)
        self.main_layout.addWidget(self.system_menu_button)

        self.application_menu_button = QPushButton("Applications")
        self.application_menu_button.setIcon(QIcon(os.path.join(self.icon_path, 'app-icon.png')))  # Using the icon path
        self.application_menu_button.clicked.connect(self.show_application_menu)
        self.main_layout.addWidget(self.application_menu_button)

        self.close_button = QPushButton(" Exit ")
        self.close_button.setIcon(QIcon(os.path.join(self.icon_path, 'close-icon.png')))  # Using the icon path
        self.close_button.clicked.connect(self.close)
        self.main_layout.addWidget(self.close_button)

        self.central_widget.addWidget(self.main_menu)

        # System commands menu
        self.system_menu = QWidget()
        self.system_layout = QVBoxLayout()
        self.system_menu.setLayout(self.system_layout)

        # Add title to system menu
        self.system_title = QLabel("Sys Commands")
        self.system_title.setFont(QFont("Arial", 18, QFont.Bold))
        self.system_title.setAlignment(Qt.AlignCenter)
        self.system_layout.addWidget(self.system_title)

        self.shutdown_button = QPushButton("")
        self.shutdown_button.setIcon(QIcon(os.path.join(self.icon_path, 'system-icon.png')))  # Using the icon path
        self.shutdown_button.clicked.connect(lambda: self.execute_command("shutdown"))
        self.system_layout.addWidget(self.shutdown_button)

        self.reboot_button = QPushButton("")
        self.reboot_button.setIcon(QIcon(os.path.join(self.icon_path, 'reboot-icon.png')))  # Using the icon path
        self.reboot_button.clicked.connect(lambda: self.execute_command("reboot"))
        self.system_layout.addWidget(self.reboot_button)

        self.suspend_button = QPushButton("")
        self.suspend_button.setIcon(QIcon(os.path.join(self.icon_path, 'suspend-icon.png')))  # Using the icon path
        self.suspend_button.clicked.connect(lambda: self.execute_command("suspend"))
        self.system_layout.addWidget(self.suspend_button)

        self.back_button_system = QPushButton("")
        self.back_button_system.setIcon(QIcon(os.path.join(self.icon_path, 'back-icon.png')))  # Using the icon path
        self.back_button_system.clicked.connect(self.show_main_menu)
        self.system_layout.addWidget(self.back_button_system)

        self.central_widget.addWidget(self.system_menu)

        # Applications menu
        self.application_menu = QWidget()
        self.application_layout = QVBoxLayout()
        self.application_menu.setLayout(self.application_layout)

        # Add title to application menu
        self.application_title = QLabel("App Launcher")
        self.application_title.setFont(QFont("Arial", 18, QFont.Bold))
        self.application_title.setAlignment(Qt.AlignCenter)
        self.application_layout.addWidget(self.application_title)

        self.firefox_button = QPushButton("Firefox")
        self.firefox_button.clicked.connect(lambda: self.execute_command("firefox"))
        self.application_layout.addWidget(self.firefox_button)

        self.terminal_button = QPushButton("Terminal")
        self.terminal_button.clicked.connect(lambda: self.execute_command("terminal"))
        self.application_layout.addWidget(self.terminal_button)

        self.thunar_button = QPushButton("Thunar")
        self.thunar_button.clicked.connect(lambda: self.execute_command("thunar"))
        self.application_layout.addWidget(self.thunar_button)

        self.back_button_app = QPushButton("")
        self.back_button_app.setIcon(QIcon(os.path.join(self.icon_path, 'back-icon.png')))  # Using the icon path
        self.back_button_app.clicked.connect(self.show_main_menu)
        self.application_layout.addWidget(self.back_button_app)

        self.central_widget.addWidget(self.application_menu)

        # Show main menu by default
        self.central_widget.setCurrentWidget(self.main_menu)

        # Set up timer to refresh the UI every 5 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_ui)
        self.timer.start(5000)  # 5000 ms = 5 seconds

    def refresh_ui(self):
        """Refresh the interface every 5 seconds to avoid lag."""
        # In a real app, you might want to update some UI elements here
        self.update()  # This refreshes the UI

    def show_main_menu(self):
        self.central_widget.setCurrentWidget(self.main_menu)

    def show_system_menu(self):
        self.central_widget.setCurrentWidget(self.system_menu)

    def show_application_menu(self):
        self.central_widget.setCurrentWidget(self.application_menu)

    def execute_command(self, command):
        """Execute the command in a separate thread to avoid blocking the UI."""
        def run_command():
            try:
                if command == "shutdown":
                    os.system("sudo shutdown now")
                    response = "Shutdown initiated"
                elif command == "reboot":
                    os.system("sudo shutdown -r now")
                    response = "Reboot initiated"
                elif command == "suspend":
                    os.system("systemctl suspend")
                    response = "Suspend initiated"
                elif command == "firefox":
                    subprocess.run(["firefox"], check=True)
                    response = "Firefox launched"
                elif command == "terminal":
                    subprocess.run(["kitty"], check=True)
                    response = "Terminal launched"
                elif command == "thunar":
                    subprocess.run(["Thunar"], check=True)
                    response = "Thunar launched"
                else:
                    response = "Unknown command"
            except Exception as e:
                response = f"Error: {str(e)}"

        # Run the command in a separate thread to avoid blocking the UI
        threading.Thread(target=run_command, daemon=True).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    executor = CommandExecutor()
    executor.show()
    sys.exit(app.exec_())
