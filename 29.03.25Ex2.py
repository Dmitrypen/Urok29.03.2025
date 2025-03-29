# для работоспособности так же нужно установить PyQt5 и matplotlib
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
class HarmonicOscillationPlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Гармоническое колебание')

        layout = QVBoxLayout()

        self.amplitude_input = QLineEdit(self)
        self.amplitude_input.setPlaceholderText('Амплитуда (м)')
        layout.addWidget(self.amplitude_input)

        self.frequency_input = QLineEdit(self)
        self.frequency_input.setPlaceholderText('Частота (Гц)')
        layout.addWidget(self.frequency_input)

        self.phase_input = QLineEdit(self)
        self.phase_input.setPlaceholderText('Фаза (градусы)')
        layout.addWidget(self.phase_input)

        self.plot_button = QPushButton('Построить', self)
        self.plot_button.clicked.connect(self.plot_oscillation)
        layout.addWidget(self.plot_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_oscillation(self):
        try:
            amplitude = float(self.amplitude_input.text())
            frequency = float(self.frequency_input.text())
            phase = float(self.phase_input.text())
        except ValueError:
            self.show_error('Пожалуйста, введите корректные значения.')
            return

        phase_rad = np.radians(phase)

        t = np.linspace(0, 1, 1000)  # Время от 0 до 1 секунды с 1000 точками
        x = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(t, x)
        ax.set_xlabel('X — время (с)')
        ax.set_ylabel('Y — смещение (м)')
        ax.set_title('График гармонического колебания')
        ax.grid()
        self.canvas.draw()
    def show_error(self, message):
        error_label = QLabel(message, self)
        error_label.setStyleSheet("color: red;")
        self.layout().addWidget(error_label)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = HarmonicOscillationPlotter()
    plotter.resize(800, 600)
    plotter.show()
    sys.exit(app.exec_())
