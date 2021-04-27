# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 620)
        MainWindow.setStyleSheet("background-color: rgb(70, 72, 102);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 691, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(51, 51, 51);\n"
"border-radius: 15px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(120, 160, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.name.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.course = QtWidgets.QLineEdit(self.frame)
        self.course.setGeometry(QtCore.QRect(120, 240, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.course.setFont(font)
        self.course.setStyleSheet("QLineEdit\n"
"{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"\n"
"}")
        self.course.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.course.setObjectName("course")
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        self.btn_ok.setGeometry(QtCore.QRect(350, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_preview = QtWidgets.QPushButton(self.frame)
        self.btn_preview.setGeometry(QtCore.QRect(190, 410, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btn_preview.setFont(font)
        self.btn_preview.setStyleSheet("QPushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}")
        self.btn_preview.setObjectName("btn_preview")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(120, 320, 131, 31))
        self.timeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit.setMaximumTime(QtCore.QTime(18, 30, 59))
        self.timeEdit.setMinimumTime(QtCore.QTime(7, 30, 0))
        self.timeEdit.setTime(QtCore.QTime(7, 30, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.room = QtWidgets.QComboBox(self.frame)
        self.room.setGeometry(QtCore.QRect(450, 320, 69, 31))
        self.room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.room.setObjectName("room")
        self.room.addItem("")
        self.room.addItem("")
        self.room.addItem("")
        self.room.addItem("")
        self.room.addItem("")
        self.room.addItem("")
        self.room.addItem("")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setPlaceholderText(_translate("MainWindow", "                                Fullname"))
        self.course.setPlaceholderText(_translate("MainWindow", "                             Course & Year"))
        self.btn_ok.setText(_translate("MainWindow", "OK"))
        self.btn_preview.setText(_translate("MainWindow", "Preview"))
        self.room.setItemText(0, _translate("MainWindow", "----"))
        self.room.setItemText(1, _translate("MainWindow", "1"))
        self.room.setItemText(2, _translate("MainWindow", "2"))
        self.room.setItemText(3, _translate("MainWindow", "3"))
        self.room.setItemText(4, _translate("MainWindow", "4"))
        self.room.setItemText(5, _translate("MainWindow", "5"))
        self.room.setItemText(6, _translate("MainWindow", "6"))
