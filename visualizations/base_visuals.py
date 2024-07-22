from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class VisualizationArea(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Visualization Area")
        layout.addWidget(self.label)
        self.setLayout(layout)

        