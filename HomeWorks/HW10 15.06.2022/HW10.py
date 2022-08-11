import time
from threading import Thread
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QGridLayout, QCheckBox, QPushButton, QSlider, \
    QComboBox
from PySide6.QtCore import QThreadPool
import cv2  # pip install opencv-python

hours = 0
minutes = 0
seconds = 0

pause = True


class MainWindow(QWidget):  # MainWindow - класс наследник(дочерний) от класса QWidget(родитель)
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)  # тут происходит вызов конструктора для родителя

        self.setWindowTitle(title)
        self.resize(width, height)

        self.image_data = None

        self.layout = QGridLayout()  # экземпляр класса интерфейса grid(сетка)
        self.setLayout(self.layout)  # вкладываем QGridLayout -> MainWindow(QWidget)

        # # часы
        # hours_label = ttk.Label(frm, text="00")
        # hours_label.grid(column=0, row=0)
        self.hours_label = QLabel('00')  # экзампляр строки текста
        self.layout.addWidget(self.hours_label, 0, 0)

        # # двоеточие
        # ttk.Label(frm, text=":").grid(column=1, row=0)
        # self.layout.addWidget(QLabel(':'), column=1, row=0)
        self.layout.addWidget(QLabel(':'), 0, 1)

        # # минуты
        # minutes_label = ttk.Label(frm, text="00")
        # minutes_label.grid(column=2, row=0)
        self.minutes_label = QLabel('00')  # экзампляр строки текста
        # self.layout.addWidget(self.minutes_label, column=2, row=0)
        self.layout.addWidget(self.minutes_label, 0, 2)

        #
        # # двоеточие
        # ttk.Label(frm, text=":").grid(column=3, row=0)
        # self.layout.addWidget(QLabel(':'), column=3, row=0)
        self.layout.addWidget(QLabel(':'), 0, 3)

        #
        # # секунды
        # seconds_label = ttk.Label(frm, text="00")
        # seconds_label.grid(column=4, row=0)
        self.seconds_label = QLabel('00')  # экзампляр строки текста
        # self.layout.addWidget(self.seconds_label, column=4, row=0)
        self.layout.addWidget(self.seconds_label, 0, 4)

        #
        # # кнопка стоп
        # Button(text="Stop",  # текст кнопки
        #        background="#555",  # фоновый цвет кнопки
        #        foreground="#ccc",  # цвет текста
        #        padx="20",  # отступ от границ до содержимого по горизонтали
        #        pady="8",  # отступ от границ до содержимого по вертикали
        #        font="16",  # высота шрифта
        #        command=stop_timer,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
        #        ).grid(column=3, row=1)
        self.push_button_stop = QPushButton('Stop')  # экзампляр строки ввода текста
        self.push_button_stop.clicked.connect(self.stop_timer)
        # self.layout.addWidget(self.push_button_stop, column=3, row=1)  # вкладываем QLineEdit -> QGridLayout
        self.layout.addWidget(self.push_button_stop, 1, 3)  # вкладываем QLineEdit -> QGridLayout

        #
        # # кнопка старт
        # Button(text="Start",  # текст кнопки
        #        background="#555",  # фоновый цвет кнопки
        #        foreground="#ccc",  # цвет текста
        #        padx="20",  # отступ от границ до содержимого по горизонтали
        #        pady="8",  # отступ от границ до содержимого по вертикали
        #        font="16",  # высота шрифта
        #        command=start_new_thread,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
        #        ).grid(column=1, row=1)
        self.push_button_start = QPushButton('Start')  # экзампляр строки ввода текста
        self.push_button_start.clicked.connect(self.start_new_thread)
        # self.layout.addWidget(self.push_button_start, column=1, row=1)  # вкладываем QLineEdit -> QGridLayout
        self.layout.addWidget(self.push_button_start, 1, 1)  # вкладываем QLineEdit -> QGridLayout

        #
        # # кнопка reset
        # Button(text="Reset",  # текст кнопки
        #        background="#555",  # фоновый цвет кнопки
        #        foreground="#ccc",  # цвет текста
        #        padx="20",  # отступ от границ до содержимого по горизонтали
        #        pady="8",  # отступ от границ до содержимого по вертикали
        #        font="16",  # высота шрифта
        #        command=reset_timer,  # мы ССЫЛАЕМСЯ на функцию, если поставить () - то это вызов функции
        #        ).grid(column=2, row=1)
        self.push_button_reset = QPushButton('Reset')  # экзампляр строки ввода текста
        self.push_button_reset.clicked.connect(self.reset_timer)
        # self.layout.addWidget(self.push_button_reset, column=2, row=1)  # вкладываем QLineEdit -> QGridLayout
        self.layout.addWidget(self.push_button_reset, 1, 2)  # вкладываем QLineEdit -> QGridLayout

        self.show()

    def reset_timer(self):
        global hours
        hours = 0.0
        global minutes
        minutes = 0.0
        global seconds
        seconds = 0.0

        # self.seconds_label.config(text=f"{seconds}")
        self.seconds_label.setText(f"{seconds}")
        # self.minutes_label.config(text=f"{minutes}")
        self.minutes_label.setText(f"{minutes}")
        # self.hours_label.config(text=f"{hours}")
        self.hours_label.setText(f"{hours}")

    @staticmethod
    def stop_timer(self):
        global pause
        pause = False

    def start_timer(self):
        global pause
        pause = True

        global hours
        # hours = 0
        global minutes
        # minutes = 0
        global seconds
        # seconds = 0

        # код до цикла
        while pause:
            # seconds = seconds + 1
            seconds += 1

            if seconds > 59:
                minutes += 1
                seconds = 0

            if minutes > 59:
                hours += 1
                minutes = 0

            if hours > 23:
                seconds = 0
                minutes = 0
                hours = 0

            time.sleep(0.00001)
            # self.seconds_label.config(text=f"{seconds}")
            self.seconds_label.setText(f"{seconds}")
            # self.minutes_label.config(text=f"{minutes}")
            self.minutes_label.setText(f"{minutes}")
            # self.hours_label.config(text=f"{hours}")
            self.hours_label.setText(f"{hours}")
            print(f"{hours}:{minutes}" + ":" + str(seconds))

    @staticmethod
    def start_new_thread(self):
        # self.threadpool.start()
        Thread(
            target=self.start_timer()
        ).start()  # Используйте для вызова функции в отдельный поток, тогда остальная часть окна не
        # будет виснуть


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'image analyse')  # создаём инстанс (экземпляр) класса
# пока класс не умрёт, эта часть кода не затронется
app.exec()  # очистка памяти
