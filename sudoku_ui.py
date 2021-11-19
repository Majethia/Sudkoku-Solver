from PyQt5 import QtCore, QtGui, QtWidgets
import sudoku_solver
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 400, 250, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(300, 150, 250, 250))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 250, 250))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 0 0 0 0 0 0 0 0</span></p></body></html>")
        self.solution = QtWidgets.QLabel(self.centralwidget)
        self.solution.setGeometry(QtCore.QRect(150, 430, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solution.setFont(font)
        self.solution.setAlignment(QtCore.Qt.AlignCenter)
        self.solution.setObjectName("solution")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku Slover"))
        self.label.setText(_translate("MainWindow", "Sudoku Solver"))
        self.pushButton.setText(_translate("MainWindow", "Find Solution"))
        self.label_2.setText(_translate("MainWindow", "Type the sudoku below"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">1 0 0 9 0 4 0 8 2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 5 2 6 8 0 3 0 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">8 6 4 2 0 0 9 1 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 1 0 0 4 9 8 0 6</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">4 9 8 3 0 0 7 0 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">6 0 7 0 1 0 0 9 3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 8 6 0 3 5 2 0 9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">5 0 9 0 0 2 1 3 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:12pt; color:#ce9178;\">0 3 0 4 9 7 0 0 8</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Example"))
        self.solution.setText(_translate("MainWindow", "0 0 0 | 0 0 0 | 0 0 0\n"
"0 0 0 | 0 0 0 | 0 0 0 \n"
"0 0 0 | 0 0 0 | 0 0 0 \n"
"- - - - - - - - - - - - - \n"
"0 0 0 | 0 0 0 | 0 0 0 \n"
"0 0 0 | 0 0 0 | 0 0 0 \n"
"0 0 0 | 0 0 0 | 0 0 0\n"
"- - - - - - - - - - - - -\n"
"0 0 0 | 0 0 0 | 0 0 0\n"
"0 0 0 | 0 0 0 | 0 0 0\n"
"0 0 0 | 0 0 0 | 0 0 0"))

        self.pushButton.clicked.connect(lambda: self.find_solution())

    def find_solution(self):
        a = self.textEdit.toPlainText()
        b = a.replace(" ","")
        c = str(b.replace("\n",""))
        answer = sudoku_solver.main(c)
        self.solution.setText(answer)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
