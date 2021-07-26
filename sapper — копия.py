import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 625)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {	height: 100;	width: 100;}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cell_1 = QPushButton(self.centralwidget)
        self.cell_1.setObjectName(u"cell_1")
        self.cell_1.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")
        icon = QIcon()
        icon.addFile("cell.jpg", QSize(), QIcon.Normal, QIcon.Off)
        #icon.addFile("mine_fire.jpg", QSize(), QIcon.Normal, QIcon.On)
        
        self.cell_1.setIcon(icon)
        self.cell_1.setIconSize(QSize(100, 100))
        self.cell_1.setCheckable(True)

        self.verticalLayout.addWidget(self.cell_1)

        self.cell_2 = QPushButton(self.centralwidget)
        self.cell_2.setObjectName(u"cell_2")
        self.cell_2.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.cell_2.setCheckable(True)

        self.verticalLayout.addWidget(self.cell_2)

        self.cell_3 = QPushButton(self.centralwidget)
        self.cell_3.setObjectName(u"cell_3")
        self.cell_3.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout.addWidget(self.cell_3)

        self.cell_4 = QPushButton(self.centralwidget)
        self.cell_4.setObjectName(u"cell_4")
        self.cell_4.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout.addWidget(self.cell_4)

        self.cell_5 = QPushButton(self.centralwidget)
        self.cell_5.setObjectName(u"cell_5")
        self.cell_5.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout.addWidget(self.cell_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cell_6 = QPushButton(self.centralwidget)
        self.cell_6.setObjectName(u"cell_6")
        self.cell_6.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_2.addWidget(self.cell_6)

        self.cell_7 = QPushButton(self.centralwidget)
        self.cell_7.setObjectName(u"cell_7")
        self.cell_7.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_2.addWidget(self.cell_7)

        self.cell_8 = QPushButton(self.centralwidget)
        self.cell_8.setObjectName(u"cell_8")
        self.cell_8.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_2.addWidget(self.cell_8)

        self.cell_9 = QPushButton(self.centralwidget)
        self.cell_9.setObjectName(u"cell_9")
        self.cell_9.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_2.addWidget(self.cell_9)

        self.cell_10 = QPushButton(self.centralwidget)
        self.cell_10.setObjectName(u"cell_10")
        self.cell_10.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_2.addWidget(self.cell_10)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cell_11 = QPushButton(self.centralwidget)
        self.cell_11.setObjectName(u"cell_11")
        self.cell_11.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_3.addWidget(self.cell_11)

        self.cell_12 = QPushButton(self.centralwidget)
        self.cell_12.setObjectName(u"cell_12")
        self.cell_12.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_3.addWidget(self.cell_12)

        self.cell_13 = QPushButton(self.centralwidget)
        self.cell_13.setObjectName(u"cell_13")
        self.cell_13.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_3.addWidget(self.cell_13)

        self.cell_14 = QPushButton(self.centralwidget)
        self.cell_14.setObjectName(u"cell_14")
        self.cell_14.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_3.addWidget(self.cell_14)

        self.cell_15 = QPushButton(self.centralwidget)
        self.cell_15.setObjectName(u"cell_15")
        self.cell_15.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_3.addWidget(self.cell_15)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cell_16 = QPushButton(self.centralwidget)
        self.cell_16.setObjectName(u"cell_16")
        self.cell_16.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_4.addWidget(self.cell_16)

        self.cell_17 = QPushButton(self.centralwidget)
        self.cell_17.setObjectName(u"cell_17")
        self.cell_17.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_4.addWidget(self.cell_17)

        self.cell_18 = QPushButton(self.centralwidget)
        self.cell_18.setObjectName(u"cell_18")
        self.cell_18.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_4.addWidget(self.cell_18)

        self.cell_19 = QPushButton(self.centralwidget)
        self.cell_19.setObjectName(u"cell_19")
        self.cell_19.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_4.addWidget(self.cell_19)

        self.cell_20 = QPushButton(self.centralwidget)
        self.cell_20.setObjectName(u"cell_20")
        self.cell_20.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_4.addWidget(self.cell_20)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cell_21 = QPushButton(self.centralwidget)
        self.cell_21.setObjectName(u"cell_21")
        self.cell_21.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_5.addWidget(self.cell_21)

        self.cell_22 = QPushButton(self.centralwidget)
        self.cell_22.setObjectName(u"cell_22")
        self.cell_22.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_5.addWidget(self.cell_22)

        self.cell_23 = QPushButton(self.centralwidget)
        self.cell_23.setObjectName(u"cell_23")
        self.cell_23.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_5.addWidget(self.cell_23)

        self.cell_24 = QPushButton(self.centralwidget)
        self.cell_24.setObjectName(u"cell_24")
        self.cell_24.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_5.addWidget(self.cell_24)

        self.cell_25 = QPushButton(self.centralwidget)
        self.cell_25.setObjectName(u"cell_25")
        self.cell_25.setStyleSheet(u"QPushButton {	height: 100;	width: 100;}")

        self.verticalLayout_5.addWidget(self.cell_25)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 592, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sapper", None))
        self.cell_1.setText("")
        self.cell_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.cell_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


class Sapper(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    sapper = Sapper()
    sys.exit(app.exec_())
