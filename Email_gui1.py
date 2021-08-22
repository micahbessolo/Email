from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.see_email_button = QtWidgets.QPushButton(self.centralwidget)
        self.see_email_button.setGeometry(QtCore.QRect(60, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.see_email_button.setFont(font)
        self.see_email_button.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF\n"
"    padding-left: 20px;\n"
"    rgb(203, 203, 203)padding-right: 20px;\n"
"}")
        self.see_email_button.setObjectName("see_email_button")
        self.enter_email_box = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_email_box.setGeometry(QtCore.QRect(60, 30, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_email_box.setFont(font)
        self.enter_email_box.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF\n"
"    padding-left: 20px;\n"
"    rgb(203, 203, 203)padding-right: 20px;\n"
"    background-color: rgb(125, 125, 125);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solidrgb(58, 58, 58);\n"
"}")
        self.enter_email_box.setObjectName("enter_email_box")
        self.enter_greeting_box = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_greeting_box.setGeometry(QtCore.QRect(60, 70, 701, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enter_greeting_box.setFont(font)
        self.enter_greeting_box.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF\n"
"    padding-left: 20px;\n"
"    rgb(203, 203, 203)padding-right: 20px;\n"
"}")
        self.enter_greeting_box.setObjectName("enter_greeting_box")
        self.fullText = QtWidgets.QTextEdit(self.centralwidget)
        self.fullText.setGeometry(QtCore.QRect(60, 170, 701, 221))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fullText.setFont(font)
        self.fullText.setObjectName("fullText")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(60, 420, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF\n"
"    padding-left: 20px;\n"
"    rgb(203, 203, 203)padding-right: 20px;\n"
"}")
        self.send_button.setObjectName("send_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.see_email_button.setText(_translate("MainWindow", "See email"))
        self.enter_email_box.setPlaceholderText(_translate("MainWindow", "Enter email address"))
        self.enter_greeting_box.setPlaceholderText(_translate("MainWindow", "Enter greeting"))
        self.fullText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.send_button.setText(_translate("MainWindow", "Send Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
