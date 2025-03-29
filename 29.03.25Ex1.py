# Нужно установить библиотеки PyQt5 и matplotlib
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class TrajectoryPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Траектория броска тела')
        layout = QVBoxLayout()
        self.speed_input = QLineEdit(self)
        self.speed_input.setPlaceholderText('Начальная скорость (м/с)')
        layout.addWidget(self.speed_input)

        self.angle_input = QLineEdit(self)
        self.angle_input.setPlaceholderText('Угол броска (градусы)')
        layout.addWidget(self.angle_input)

        self.plot_button = QPushButton('Построить траекторию', self)
        self.plot_button.clicked.connect(self.plot_trajectory)
        layout.addWidget(self.plot_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_trajectory(self):
        try:
            initial_speed = float(self.speed_input.text())
            angle = float(self.angle_input.text())
        except ValueError:
            self.show_error('Пожалуйста, введите корректные значения.')
            return

        angle_rad = np.radians(angle)

        g = 9.81 
        time_of_flight = (2 * initial_speed * np.sin(angle_rad)) / g

        t = np.linspace(0, time_of_flight, num=100)
        x = initial_speed * np.cos(angle_rad) * t
        y = initial_speed * np.sin(angle_rad) * t - 0.5 * g * t**2

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('X — расстояние (м)')
        ax.set_ylabel('Y — высота (м)')
        ax.set_title('Траектория броска тела')
        ax.grid()
        self.canvas.draw()

    def show_error(self, message):
        error_label = QLabel(message, self)
        error_label.setStyleSheet("color: red;")
        self.layout().addWidget(error_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = TrajectoryPlotter()
    plotter.resize(800, 600)
    plotter.show()
    sys.exit(app.exec_())