#Main point of interaction with the app
#Entry point

import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(sys.exec())

if __name__ == "__main__":
    main()