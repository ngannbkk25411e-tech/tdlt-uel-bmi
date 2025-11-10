from tkinter import BitmapImage

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.find_solution)
    def find_solution(self):
        weight = float(self.lineEditWeight.text())
        height = float(self.lineEditHeight.text())
        bmi = self.pushButtonCalculate(weight, height)
        if bmi < 18.5:
            status = "Gầy"
        elif 18.5 <= bmi < 25:
            status = "Bình thường"
        elif 25 <= bmi < 30:
            status = "Thừa cân"
        else:
            status = "Béo phì"
        self.labelBMI.setText(f"BMI: {bmi} ({status})")

