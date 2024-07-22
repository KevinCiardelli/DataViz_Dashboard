from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.load_button = QPushButton("Load Data")
        layout.addWidget(self.load_button)

        self.setLayout(layout)

