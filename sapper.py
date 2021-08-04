import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
#from PySide2.QtWidgets import *
import random

class SpecButton(QtWidgets.QPushButton):
    def __init__(self,parent):
        super().__init__(parent)
        super(Sapper)
        self.clickOn = 0
        self.textOut = None
        self.count = None

    

    def setCellIcon(self):
        if self.textOut == 0:
            self.setIcon(QIcon("number_0.png"))
        if self.textOut == 1:
            self.setIcon(QIcon("number_1.png"))
        if self.textOut == 2:
            self.setIcon(QIcon("number_2.png"))
        if self.textOut == 3:
            self.setIcon(QIcon("number_3.png"))
        if self.textOut == 4:
            self.setIcon(QIcon("number_4.png"))
        if self.textOut == 5:
            self.setIcon(QIcon("number_5.png"))
        if self.textOut == 6:
            self.setIcon(QIcon("number_6.png"))
        if self.textOut == 7:
            self.setIcon(QIcon("number_7.png"))
        if self.textOut == 8:
            self.setIcon(QIcon("number_8.png"))
        if self.textOut == 'M':
            self.setIcon(QIcon("mine_fire.png"))
        if self.textOut == 'outM':
            self.setIcon(QIcon("mine_ok.png"))
            

    def mousePressEvent(self, event):
        if self.cell == 99:return()
        if sapper.lose == 1: return()
        if event.button() == Qt.RightButton:
            if self.clickOn != 1:
                self.textOut = 'outM'
                sapper.nMine -= 1
                sapper.count-=1
        elif event.button() == Qt.LeftButton:
            if self.clickOn == 0 and sapper.pole[self.cell] == 0 :
                sapper.clickIfZero(self.cell)
            if self.textOut == None:
                sapper.count-=1
            if self.textOut == 'outM':
                sapper.nMine += 1
            self.clickOn = 1
            self.textOut = sapper.pole[self.cell]
            if sapper.pole[self.cell] == 'M':
                sapper.lose = 1
                sapper.timer.stop()
        sapper.lcdNumber.display(sapper.nMine)
        self.setCellIcon()
        if sapper.count == 0:
            #sapper.status('win')
            sapper.timer.stop()
            sapper.score = sapper.time
            sapper.createScore()
        super().mousePressEvent(event)


            
            
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        #MainWindow.resize(336, 421)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_2.addWidget(self.lcdNumber, 0, 0, 1, 1)

        self.cell_status = SpecButton(self.centralwidget)
        self.cell_status.setObjectName(u"cell_status")
        self.cell_status.setMaximumSize(QSize(100, 100))

        self.gridLayout_2.addWidget(self.cell_status, 0, 1, 1, 1)

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setEnabled(True)

        self.gridLayout_2.addWidget(self.lcdNumber_2, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

##        icon = QIcon("cell.jpg")
##        
##        self.cell_5 = SpecButton(self.centralwidget)
##        self.cell_5.setObjectName(u"cell_5")
##        self.cell_5.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_5.setIcon(icon)
##        self.cell_5.setIconSize(QSize(50, 50))
##
##        self.gridLayout.addWidget(self.cell_5, 4, 0, 1, 1)
##
##        self.cell_11 = SpecButton(self.centralwidget)
##        self.cell_11.setObjectName(u"cell_11")
##        self.cell_11.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_11.setIcon(icon)
##        self.cell_11.setIconSize(QSize(50, 50))
##
##        self.gridLayout.addWidget(self.cell_11, 0, 2, 1, 1)
##
##        self.cell_19 = SpecButton(self.centralwidget)
##        self.cell_19.setObjectName(u"cell_19")
##        self.cell_19.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_19.setIcon(icon)
##        self.cell_19.setIconSize(QSize(50, 50))
##
##        self.gridLayout.addWidget(self.cell_19, 3, 3, 1, 1)
##
##        self.cell_15 = SpecButton(self.centralwidget)
##        self.cell_15.setObjectName(u"cell_15")
##        self.cell_15.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_15.setIcon(icon)
##        self.cell_15.setIconSize(QSize(50, 50))
##
##        self.gridLayout.addWidget(self.cell_15, 4, 2, 1, 1)
##
##        self.cell_25 = SpecButton(self.centralwidget)
##        self.cell_25.setObjectName(u"cell_25")
##        self.cell_25.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_25.setIcon(icon)
##        self.cell_25.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_25, 4, 4, 1, 1)
##
##        self.cell_2 = SpecButton(self.centralwidget)
##        self.cell_2.setObjectName(u"cell_2")
##        self.cell_2.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_2.setIcon(icon)
##        self.cell_2.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_2, 1, 0, 1, 1)
##
##        self.cell_7 = SpecButton(self.centralwidget)
##        self.cell_7.setObjectName(u"cell_7")
##        self.cell_7.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_7.setIcon(icon)
##        self.cell_7.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_7, 1, 1, 1, 1)
##
##        self.cell_13 = SpecButton(self.centralwidget)
##        self.cell_13.setObjectName(u"cell_13")
##        self.cell_13.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_13.setIcon(icon)
##        self.cell_13.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_13, 2, 2, 1, 1)
##
##        self.cell_10 = SpecButton(self.centralwidget)
##        self.cell_10.setObjectName(u"cell_10")
##        self.cell_10.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_10.setIcon(icon)
##        self.cell_10.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_10, 4, 1, 1, 1)
##
##        self.cell_20 = SpecButton(self.centralwidget)
##        self.cell_20.setObjectName(u"cell_20")
##        self.cell_20.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_20.setIcon(icon)
##        self.cell_20.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_20, 4, 3, 1, 1)
##
##        self.cell_23 = SpecButton(self.centralwidget)
##        self.cell_23.setObjectName(u"cell_23")
##        self.cell_23.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_23.setIcon(icon)
##        self.cell_23.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_23, 2, 4, 1, 1)
##
##        self.cell_21 = SpecButton(self.centralwidget)
##        self.cell_21.setObjectName(u"cell_21")
##        self.cell_21.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_21.setIcon(icon)
##        self.cell_21.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_21, 0, 4, 1, 1)
##
##        self.cell_4 = SpecButton(self.centralwidget)
##        self.cell_4.setObjectName(u"cell_4")
##        self.cell_4.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_4.setIcon(icon)
##        self.cell_4.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_4, 3, 0, 1, 1)
##
##        self.cell_9 = SpecButton(self.centralwidget)
##        self.cell_9.setObjectName(u"cell_9")
##        self.cell_9.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_9.setIcon(icon)
##        self.cell_9.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_9, 3, 1, 1, 1)
##
##        self.cell_16 = SpecButton(self.centralwidget)
##        self.cell_16.setObjectName(u"cell_16")
##        self.cell_16.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_16.setIcon(icon)
##        self.cell_16.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_16, 0, 3, 1, 1)
##
##        self.cell_3 = SpecButton(self.centralwidget)
##        self.cell_3.setObjectName(u"cell_3")
##        self.cell_3.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_3.setIcon(icon)
##        self.cell_3.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_3, 2, 0, 1, 1)
##
##        self.cell_18 = SpecButton(self.centralwidget)
##        self.cell_18.setObjectName(u"cell_18")
##        self.cell_18.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_18.setIcon(icon)
##        self.cell_18.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_18, 2, 3, 1, 1)
##
##        self.cell_6 = SpecButton(self.centralwidget)
##        self.cell_6.setObjectName(u"cell_6")
##        self.cell_6.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_6.setIconSize(QSize(50, 50))
##        self.cell_6.setIcon(icon)
##        self.cell_6.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_6, 0, 1, 1, 1)
##
##        self.cell_8 = SpecButton(self.centralwidget)
##        self.cell_8.setObjectName(u"cell_8")
##        self.cell_8.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_8.setIcon(icon)
##        self.cell_8.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_8, 2, 1, 1, 1)
##
##        self.cell_12 = SpecButton(self.centralwidget)
##        self.cell_12.setObjectName(u"cell_12")
##        self.cell_12.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_12.setIcon(icon)
##        self.cell_12.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_12, 1, 2, 1, 1)
##
##        self.cell_22 = SpecButton(self.centralwidget)
##        self.cell_22.setObjectName(u"cell_22")
##        self.cell_22.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_22.setIcon(icon)
##        self.cell_22.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_22, 1, 4, 1, 1)
##
##        self.cell_1 = SpecButton(self.centralwidget)
##        self.cell_1.setObjectName(u"cell_1")
##        self.cell_1.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_1.setIcon(icon)
##        self.cell_1.setIconSize(QSize(50, 50))
##
##        self.gridLayout.addWidget(self.cell_1, 0, 0, 1, 1)
##
##        self.cell_14 = SpecButton(self.centralwidget)
##        self.cell_14.setObjectName(u"cell_14")
##        self.cell_14.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_14.setIcon(icon)
##        self.cell_14.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_14, 3, 2, 1, 1)
##
##        self.cell_24 = SpecButton(self.centralwidget)
##        self.cell_24.setObjectName(u"cell_24")
##        self.cell_24.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_24.setIcon(icon)
##        self.cell_24.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_24, 3, 4, 1, 1)
##
##        self.cell_17 = SpecButton(self.centralwidget)
##        self.cell_17.setObjectName(u"cell_17")
##        self.cell_17.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")
##        self.cell_17.setIcon(icon)
##        self.cell_17.setIconSize(QSize(50, 50))
##        
##        self.gridLayout.addWidget(self.cell_17, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 336, 21))
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043a\u043e\u0440\u0434\u044b", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u043a\u0430\u044f", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.cell_status.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

class Record(QtWidgets.QListView):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Dialog")
        self.pushButton.setText("Close Dialog")

    def btnClosed(self):
        self.close()


class Sapper(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.cell_button =dict()
        self.score = None
        self.size = 5                            #размер поля
        self.startMine = 5
        self.time = 0
    
        self.difEasy()

        self.action_5.triggered.connect(self.exit)
        self.action_2.triggered.connect(self.new_game)
        self.action_4.triggered.connect(self.record)
        self.action_6.triggered.connect(self.difEasy)
        self.action_7.triggered.connect(self.difNormal)

        #self.cell_status.clicked.connect(self.digit_status)
        


        self.createScore()



    def lcdTimer(self):
        if self.time != 0:
            self.timer.stop()
            self.time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.setInterval(1000)
        self.timer.start()
        
    def logic(self):
        self.nMine = self.startMine
        self.cell_status.setIcon(QIcon("icon.png"))
        self.lcdNumber.display(self.nMine)
        self.lcdTimer()
        self.count = 25
        for i in self.cell_button.keys():
            self.cell_button[i].setIcon(QIcon("cell.png"))
            self.cell_button[i].textOut = None
            self.cell_button[i].clickOn = 0
        
        def counterMine(x):
            n = 0
            for i in x:
                if self.pole[i] == 'M':
                    n += 1
            return(n)
        self.lose = 0
        self.sap = None
        self.counter = 0
        self.count = self.size**2
        self.cells = [n for n in range(1,self.size**2+1)]
        self.pole = {a:0 for a in self.cells}
        self.zero = dict()
        random.shuffle(self.cells)
        for cell in self.cells:
            self.counter+=1
            if self.counter <= self.startMine:      #первые nMine случайных ячеек - мины
                 self.pole[cell] = 'M'
            else:                               #остальные ячейки заполняем количеством мин
                if cell == 1:   #верхний левый угол
                    self.pole[cell] = counterMine([cell+1,cell+self.size,cell+self.size+1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell+1,cell+self.size,cell+self.size+1]
                elif cell == self.size: # нижний левый угол
                    self.pole[cell] = counterMine([cell-1,cell+self.size,cell+self.size-1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-1,cell+self.size,cell+self.size-1]
                elif cell == self.size*(self.size-1)+1: #верхний правый угол
                    self.pole[cell] = counterMine([cell-self.size,cell-self.size+1,cell+1])
                    if self.pole[cell] == 0:
                        self.zero[cell] =[cell-self.size,cell-self.size+1,cell+1]
                elif cell == self.size**2: #нижний правый угол
                    self.pole[cell] = counterMine([cell-self.size,cell-self.size-1,cell-1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-self.size,cell-self.size-1,cell-1]
                elif cell%self.size == 1:
                    self.pole[cell] = counterMine([cell-self.size,cell-self.size+1,cell+1,cell+self.size,cell+self.size+1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-self.size,cell-self.size+1,cell+1,cell+self.size,cell+self.size+1]
                elif cell < self.size:
                    self.pole[cell] = counterMine([cell-1,cell+1,cell+self.size-1,cell+self.size,cell+self.size+1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-1,cell+1,cell+self.size-1,cell+self.size,cell+self.size+1]
                elif cell%self.size == 0:
                    self.pole[cell] = counterMine([cell-self.size-1,cell-self.size,cell-1,cell+self.size-1,cell+self.size])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-self.size-1,cell-self.size,cell-1,cell+self.size-1,cell+self.size]
                elif cell > self.size*(self.size-1):
                    self.pole[cell] = counterMine([cell-1,cell-self.size-1,cell-self.size,cell-self.size+1,cell+1])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-1,cell-self.size-1,cell-self.size,cell-self.size+1,cell+1]
                else:
                    self.pole[cell] = counterMine([cell-self.size-1,cell-1,cell+self.size-1,cell+self.size,cell+self.size+1,cell+1,cell-self.size+1,cell-self.size])
                    if self.pole[cell] == 0:
                        self.zero[cell] = [cell-self.size-1,cell-1,cell+self.size-1,cell+self.size,cell+self.size+1,cell+1,cell-self.size+1,cell-self.size]
        for n in self.cell_button.keys():
            self.cell_button[n].cell = n
        self.cell_status.cell = 99


        
    
    def clickIfZero(self,n):
        for i in self.zero[n]:
            if self.cell_button[i].textOut == None:
                self.count-=1
                self.cell_button[i].textOut = self.pole[i]
                self.cell_button[i].setCellIcon()
            if self.cell_button[i].textOut == 'outM':
                    self.nMine += 1
                    self.cell_button[i].textOut = self.pole[i]
                    self.cell_button[i].setCellIcon()
                    

    def new_game(self):
        self.nMine = self.startMine
        self.logic()

    def createScore(self):
        try:
            with open(sys.path[0]+'/score', encoding='utf-8') as file:
                scoreList = [int(x.rstrip()[x.rstrip().find('.')+2:]) for x in file if 'Best' not in x and x.rstrip()[x.rstrip().find('.')+2:] !='---']
                if self.score != None:
                    scoreList += [self.score]
                scoreList.sort()
            with open(sys.path[0]+'/score', 'w', encoding='utf-8') as file:
                file.write('Best:\n')
                count = 0
                for i in scoreList:
                    count += 1
                    if count >= 11: break
                    if i == None: i = '---'
                    file.write(str(count)+ '. ' + str(i)+'\n')
                for i in 'n'*9:
                    count += 1
                    if count >= 11: break
                    file.write(str(count)+ '. ---\n')
        except FileNotFoundError:
            with open(sys.path[0]+'/score', 'w',encoding='utf-8') as file:
                file.write('Best:\n1. ---\n2. ---\n3. ---\n4. ---\n5. ---\n6. ---\n7. ---\n8. ---\n9. ---\n10. ---\n')
                
    def record(self,start='yes'):
        dialog = ClssDialog(self)
        dialog.enterScore()
        dialog.exec_()

    def showTime(self):
        self.time += 1
        self.lcdNumber_2.display(self.time)
        
    def exit(self):
        sys.exit(app.exec_())

    def difNormal(self):
        self.startMine = 20
        self.size = 10
        i = 0
        j = 0
        n = 1
        for I in 'i'*10:
            for J in 'j'*10:   
                exec('self.cell_'+ str(n)+ ' = SpecButton(self.centralwidget)')
                exec('self.cell_'+ str(n)+'.setObjectName(u"cell_'+str(n)+'")')
                exec('self.cell_'+str(n)+'.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")')
                exec('self.cell_'+str(n)+'.setIcon(QIcon("cell.jpg"))')
                exec('self.cell_'+str(n)+'.setIconSize(QSize(50, 50))')
    
                exec('self.gridLayout.addWidget(self.cell_'+str(n)+', ' + str(j) + ', '+str(i)+', 1, 1)')

                j+=1
                n+=1
            i+=1
            j=0
        for n in range(1,101):
            exec('self.cell_button['+str(n)+']=self.cell_'+ str(n))
        self.logic()
        self.setFixedSize(656, 741)

    def difEasy(self):
        self.startMine = 5
        for i in self.cell_button.keys():
            self.cell_button[i].hide()
        self.size = 5
        i = 0
        j = 0
        n = 1
        for I in 'i'*5:
            for J in 'j'*5:   
                exec('self.cell_'+ str(n)+ ' = SpecButton(self.centralwidget)')
                exec('self.cell_'+ str(n)+'.setObjectName(u"cell_'+str(n)+'")')
                exec('self.cell_'+str(n)+'.setStyleSheet(u"QPushButton {	height: 50;	width: 50;}")')
                exec('self.cell_'+str(n)+'.setIcon(QIcon("cell.jpg"))')
                exec('self.cell_'+str(n)+'.setIconSize(QSize(50, 50))')
    
                exec('self.gridLayout.addWidget(self.cell_'+str(n)+', ' + str(j) + ', '+str(i)+', 1, 1)')

                j+=1
                n+=1
            i+=1
            j=0
        for n in range(1,26):
            exec('self.cell_button['+str(n)+']=self.cell_'+ str(n))
        self.logic()
        self.setFixedSize(336, 421)   


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog,self).__init__(parent)
        self.resize(200, 400)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QtWidgets.QListView(self)
        self.listView.move(10,10)
        self.listView.setObjectName(u"listView")
        self.listView.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listView.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listView.setMidLineWidth(5)
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.verticalLayout.addWidget(self.listView)

        self.model = QStandardItemModel() #этот блок для вывода списка Рекорды
        self.listView.setModel(self.model)

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        self.listView.setGeometry(10,10,width-20,height-20)
    def enterScore(self):
        with open(sys.path[0]+'/score', encoding='utf-8') as file:
            file = file.readlines()
        for i in file:
            item = QStandardItem(i)
            self.model.appendRow(item)
        sapper.score = None
        
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sapper = Sapper()
    sys.exit(app.exec_())
