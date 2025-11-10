from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEx import MainWindowEx

app=QApplication([])
my_gui=MainWindowEx()
my_gui.setupUi(QMainWindow())
my_gui.showWindow()
app.exec()
