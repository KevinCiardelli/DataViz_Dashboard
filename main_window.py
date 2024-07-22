#Main window of intercation
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog
from control_panel import ControlPanel
from visualizations.base_visuals import VisualizationArea
from visualizations.line_chart import LineChart
from data_loader import DataLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataViz Dashboard")

        self.control_panel = ControlPanel()
        self.visualization_area = VisualizationArea()

        self.control_panel.load_button.clicked.connect(self.load_data)

        layout = QVBoxLayout()
        layout.addWidget(self.control_panel)
        layout.addWidget(self.visualization_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
 
    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if file_path:
            data = DataLoader.load_csv(file_path)
            self.visualization_area = LineChart(data)
            self.setCentralWidget(self.visualization_area)
