import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class CoolingProcessPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Процесс охлаждения тела')

        layout = QVBoxLayout()

        self.initial_temp_input = QLineEdit(self)
        self.initial_temp_input.setPlaceholderText('Начальная температура (°C)')
        layout.addWidget(self.initial_temp_input)

        self.env_temp_input = QLineEdit(self)
        self.env_temp_input.setPlaceholderText('Температура окружающей среды (°C)')
        layout.addWidget(self.env_temp_input)

        self.coefficient_input = QLineEdit(self)
        self.coefficient_input.setPlaceholderText('Коэффициент теплообмена (1/с)')
        layout.addWidget(self.coefficient_input)

        self.plot_button = QPushButton('Построить график', self)
        self.plot_button.clicked.connect(self.plot_cooling_process)
        layout.addWidget(self.plot_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_cooling_process(self):
        try:
            T0 = float(self.initial_temp_input.text())
            Tenv = float(self.env_temp_input.text())
            k = float(self.coefficient_input.text())
        except ValueError:
            self.show_error('введите корректные значения.')
            return
        
        t = np.linspace(0, 300, 1000) 
        T = Tenv + (T0 - Tenv) * np.exp(-k * t)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(t, T)
        ax.set_xlabel('X — время (с)')
        ax.set_ylabel('Y — температура тела (°C)')
        ax.set_title('Процесс охлаждения тела')
        ax.grid()
        self.canvas.draw()

    def show_error(self, message):
        error_label = QLabel(message, self)
        error_label.setStyleSheet("color: red;")
        self.layout().addWidget(error_label)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = CoolingProcessPlotter()
    plotter.resize(800, 600)
    plotter.show()
    sys.exit(app.exec_())