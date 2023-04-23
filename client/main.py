import sys
from client import Ui_MainWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

