from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_Project1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_no1.hide()
        self.input_no1.hide()
        self.label_no2.hide()
        self.input_no2.hide()
        self.label_no3.hide()
        self.input_no3.hide()

        self.input_attempt.textChanged.connect(self.check_text)
        self.button_submit.clicked.connect(lambda : self.submit())

        self.no1 = 0
        self.no2 = 0
        self.no3 = 0

        with open('data.csv', 'w', newline='') as data_csv:
            data_writer = csv.writer(data_csv, delimiter='\t')
            data_writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Final'])


    def check_text(self):
        self.name = self.input_student.text().strip()
        self.tries = self.input_attempt.text().strip()

        try:
            self.tries = int(self.tries)
            if self.tries < 0 or self.tries > 3:
                raise ValueError
        except(TypeError, ValueError):
            self.label_remind.setText('Please enter a valid number (1-3)')

        if self.tries == 1:
            self.label_no1.show()
            self.input_no1.show()
        elif self.tries == 2:
            self.label_no1.show()
            self.input_no1.show()
            self.label_no2.show()
            self.input_no2.show()
        else:
            self.label_no1.show()
            self.input_no1.show()
            self.label_no2.show()
            self.input_no2.show()
            self.label_no3.show()
            self.input_no3.show()

        if self.input_no1.text().strip() == '':
            self.no1 = 0
        else:
            self.no1 = self.input_no1.text().strip()
        if self.input_no2.text().strip() == '':
            self.no2 = 0
        else:
            self.no2 = self.input_no2.text().strip()
        if self.input_no3.text().strip() == '':
            self.no3 = 0
        else:
            self.no3 = self.input_no3.text().strip()


    def submit(self):
        grades = [self.name, self.no1, self.no2, self.no3]

        with open('data.csv', 'a', newline='') as data_csv:
            data_writer = csv.writer(data_csv, delimiter='\t')
            data_writer.writerow(grades)

        self.input_student.setText('')
        self.input_attempt.setText('')
        self.label_remind.setText('')

        self.label_no1.hide()
        self.input_no1.hide()
        self.label_no2.hide()
        self.input_no2.hide()
        self.label_no3.hide()
        self.input_no3.hide()