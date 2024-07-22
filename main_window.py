#Main window of intercation
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from control_panel import ControlPanel
from visualizations.base_visuals import VisualizationArea

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataViz Dashboard")

        self.control_panel = ControlPanel()
        self.visualization_area = VisualizationArea()

        layout = QVBoxLayout()
        layout.addWidget(self.control_panel)
        layout.addWidget(self.visualization_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
 