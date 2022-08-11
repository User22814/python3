import time
from threading import Thread
import sys
import datetime

import requests
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel
from bs4 import BeautifulSoup

course_dollar = 0.0
course_euro = 0.0
course_gbp = 0.0
course_cny = 0.0
course_pln = 0.0
course_rub = 0.0

url = "https://myfin.by/converter.html"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}
response = requests.get(url=url, headers=headers)
print(response)
print(response.status_code)

if response.status_code == 200:  # 200 - удачный ответ
    with open(file='data.html', mode='wb') as file:
        file.write(response.content)


def get_course():
    global course_dollar
    global course_euro
    global course_cny
    global course_gbp
    global course_pln
    global course_rub
    # while True:
    if response.status_code == 200:  # 200 - удачный ответ
        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup)
        # print(type(soup))

        # data = soup.find_all('div', class_="converter-container converter-container-in-grid")[-1]
        # data = soup.find_all('div', id="bestm_buy")
        data = soup.find_all('input', class_="input_calc form-control form-input-sum bestmb")
        # print(data)
        # print(len(data))
        data_for_dollar = data[0]
        # print(data_for_dollar)
        dollar1 = str(data_for_dollar).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_usd" inputmode="decimal" type="tel" value="')[
            -1]
        # print(dollar1)
        dollar2 = str(dollar1).split(sep='"/>')
        # print(dollar2)
        dollar = tuple(
            [
                'DOLLAR',
                float(dollar2[0])
            ]
        )
        print(dollar)
        course_dollar = dollar[-1]

        data_for_euro = data[1]
        euro1 = str(data_for_euro).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_eur" inputmode="decimal" type="tel" value="')[
            -1]
        # print(euro1)
        euro2 = str(euro1).split(sep='"/>')
        # print(euro2)
        euro = tuple(
            [
                'EURO',
                float(euro2[0])
            ]
        )
        print(euro)
        course_euro = euro[-1]

        data_for_gbp = data[2]
        gbp1 = str(data_for_gbp).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_gbp" inputmode="decimal" type="tel" value="')[
            -1]
        # print(gbp1)
        gbp2 = str(gbp1).split(sep='"/>')
        # print(gbp2)
        gbp = tuple(
            [
                'GBP',
                float(gbp2[0])
            ]
        )
        print(gbp)
        course_gbp = gbp[-1]

        data_for_cny = data[3]
        cny1 = str(data_for_cny).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_cny" inputmode="decimal" type="tel" value="')[
            -1]
        # print(cny1)
        cny2 = str(cny1).split(sep='"/>')
        # print(cny2)
        cny = tuple(
            [
                'CNY',
                float(cny2[0])
            ]
        )
        print(cny)
        course_cny = cny[-1]

        data_for_pln = data[4]
        pln1 = str(data_for_pln).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_pln" inputmode="decimal" type="tel" value="')[
            -1]
        # print(pln1)
        pln2 = str(pln1).split(sep='"/>')
        # print(pln2)
        pln = tuple(
            [
                'PLN',
                float(pln2[0])
            ]
        )
        print(pln)
        course_pln = pln[-1]

        data_for_rub = data[5]
        rub1 = str(data_for_rub).split(
            sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_rub" inputmode="decimal" type="tel" value="')[
            -1]
        # print(rub1)
        rub2 = str(rub1).split(sep='"/>')
        # print(rub2)
        rub = tuple(
            [
                'RUB',
                float(rub2[0])
            ]
        )
        print(rub)
        course_rub = rub[-1]
        # print(course_dollar)
        # print(course_pln)
        # print(course_rub)
        # print(course_cny)
        # print(course_gbp)
        # print(course_euro)

    else:
        print("ошибка получения данных!")
    # time.sleep(5.0)
    # print('Курс обновлён')


def update():
    while True:
        now = datetime.datetime.now()
        sec = now.strftime("%S")
        print("Sec:", sec)
        print((int(sec) // 10) % 2)
        if (int(sec) // 10) % 2 == 1:
            get_course()
            time.sleep(10)
            print('Курс обновлён')


Thread(target=update).start()


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.label_euro = QLabel()
        layout.addWidget(self.label_euro)

        self.label_gbp = QLabel()
        layout.addWidget(self.label_gbp)

        self.label_cny = QLabel()
        layout.addWidget(self.label_cny)

        self.label_pln = QLabel()
        layout.addWidget(self.label_pln)

        self.label_rub = QLabel()
        layout.addWidget(self.label_rub)

        self.line_edit.textChanged.connect(self.line_edit_text_changed)

        self.show()

    def line_edit_text_changed(self, text):
        try:
            text_euro = round(course_euro * float(text), 3)
            self.label_euro.setText("Ваша сумма: " + str(text_euro) + " EURO")

            text_gbp = round(course_gbp * float(text), 3)
            self.label_gbp.setText("Ваша сумма: " + str(text_gbp) + " GBP")

            text_cny = round(course_cny * float(text), 3)
            self.label_cny.setText("Ваша сумма: " + str(text_cny) + " CNY")

            text_pln = round(course_pln * float(text), 3)
            self.label_pln.setText("Ваша сумма: " + str(text_pln) + " PLN")

            text_rub = round(course_rub * float(text), 3)
            self.label_rub.setText("Ваша сумма: " + str(text_rub) + " RUB")
        except Exception as error:
            self.label_euro.setText('ошибка ввода данных')
            self.label_gbp.setText('ошибка ввода данных')
            self.label_cny.setText('ошибка ввода данных')
            self.label_pln.setText('ошибка ввода данных')
            self.label_rub.setText('ошибка ввода данных')


app = QApplication(sys.argv)
mw = MainWindow()
app.exec()
