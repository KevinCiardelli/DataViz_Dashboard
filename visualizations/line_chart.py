from visualizations.base_visuals import VisualizationArea
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd

class LineChart(VisualizationArea):
    def __init__(self, data: pd.DataFrame):
        super().__init__()
        self.data = data
        self.plot()

    def plot(self):
        fig, ax = plt.subplots()
        canvas = FigureCanvas(fig)

        for product in self.data['Product'].unique():
            product_data = self.data[self.data['Product'] == product]
            ax.plot(product_data['Date'], product_data['Sales'], label=product)

        ax.set_xlabel('Date')
        ax.set_ylabel('Sales')
        ax.set_title('Monthly Sales Data')
        ax.legend()

        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.setLayout(layout)
