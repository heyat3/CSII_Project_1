from typing import final

from PyQt6.QtWidgets import *
from gui import *
import csv
import os

class Logic(QMainWindow, Ui_Project1):
    def __init__(self):
        """
        hides labels, resets values, makes a csv file with a header if there isn't one
        also checks for change in input and if submit button was pressed
        redirects to check_text() and submit() respectively

        :return None:
        """
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

        self.no1: int = 0
        self.no2: any = 0
        self.no3: any = 0
        self.final: int = 0
        if not os.path.exists('data.csv'):
            with open('data.csv', 'w', newline='') as data_csv:
                data_writer = csv.writer(data_csv, delimiter='\t')
                data_writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Final'])


    def check_text(self):
        """
        should be actively checking the text in the attempt input box
        to only have that number of input boxes show

        :return None:
        """
        self.label_no1.hide()
        self.input_no1.hide()
        self.label_no2.hide()
        self.input_no2.hide()
        self.label_no3.hide()
        self.input_no3.hide()
        self.label_remind.setText('')

        self.name: str = self.input_student.text().strip()
        self.tries: int = self.input_attempt.text().strip()

        try:
            self.tries = int(self.tries)
            if self.tries < 1 or self.tries > 3:
                raise ValueError
        except(TypeError, ValueError):
            self.label_remind.setText('Please enter a valid number (1-3)')
            self.tries = 0
            self.label_no1.hide()
            self.input_no1.hide()
            self.label_no2.hide()
            self.input_no2.hide()
            self.label_no3.hide()
            self.input_no3.hide()
            return

        if self.tries == 1:
            self.label_no1.show()
            self.input_no1.show()
            #self.label_remind.setText('Zeroes will not be calculated')

            self.no2, self.no3 = 'N/A', 'N/A'
            if self.no1 != '':
                self.button_submit.show()
                self.label_remind.setText('')

        elif self.tries == 2:
            self.label_no1.show()
            self.input_no1.show()
            self.label_no2.show()
            self.input_no2.show()
            #self.label_remind.setText('Zeroes will not be calculated')

            self.no3 = 'N/A'
            if self.no1 != '' and self.no2 != '':
                self.button_submit.show()
                self.label_remind.setText('')

        else:
            self.label_no1.show()
            self.input_no1.show()
            self.label_no2.show()
            self.input_no2.show()
            self.label_no3.show()
            self.input_no3.show()
            #self.label_remind.setText('Zeroes will not be calculated')

            if self.no1 != '' and self.no2 != '' and self.no3 != '':
                self.button_submit.show()
                self.label_remind.setText('')

    def submit(self):
        """
        checks if input is valid
        final grade is calculated by taking the average of the two highest scores

        :return None:
        """
        if self.tries == 1:
            try:
                self.no1 = int(self.input_no1.text().strip())

                if self.no1 < 0 or self.no1 > 100:
                    raise ValueError
            except(TypeError, ValueError):
                self.label_remind.setText('Please enter a valid number (0-100)')
                return

        elif self.tries == 2:
            try:
                self.no1 = int(self.input_no1.text().strip())
                self.no2 = int(self.input_no2.text().strip())

                if self.no1 < 0 or self.no1 > 100:
                    raise ValueError
                if self.no2 < 0 or self.no2 > 100:
                    raise ValueError
            except(TypeError, ValueError):
                self.label_remind.setText('Please enter a valid number (0-100)')
                return

        else:
            try:
                self.no1 = int(self.input_no1.text().strip())
                self.no2 = int(self.input_no2.text().strip())
                self.no3 = int(self.input_no3.text().strip())

                if self.no1 < 0 or self.no1 > 100:
                    raise ValueError
                if self.no2 < 0 or self.no2 > 100:
                    raise ValueError
                if self.no3 < 0 or self.no3 > 100:
                    raise ValueError
            except(TypeError, ValueError):
                self.label_remind.setText('Please enter a valid number (0-100)')
                return

        grades: list = [self.no1, self.no2, self.no3]

        final_sum: int = 0
        counter: int = 0
        for i in grades:
            if i == "N/A":
                continue
            final_sum += i
            counter += 1
        if counter == 3:
            sorted_list: list = grades
            sorted_list.sort()
            lowest: int = sorted_list[0]
            final_sum -= lowest
            counter -= 1
        self.final: int = final_sum / counter

        grades.insert(0, self.name)
        grades.append(self.final)

        with open('data.csv', 'a', newline='') as data_csv:
            data_writer: csv.writer = csv.writer(data_csv, delimiter='\t')
            data_writer.writerow(grades)

        self.input_student.setText('')
        self.input_attempt.setText('')
        self.label_remind.setText('')
        self.input_no1.setText('')
        self.input_no2.setText('')
        self.input_no3.setText('')

        self.label_no1.hide()
        self.input_no1.hide()
        self.label_no2.hide()
        self.input_no2.hide()
        self.label_no3.hide()
        self.input_no3.hide()