from PySide2 import QtWidgets, QtCore
 
 
class PushButtonRight(QtWidgets.QPushButton):
 
    def __init__(self, string):
        super().__init__(string)
 
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            print('left click')
        elif event.button() == QtCore.Qt.RightButton:
            print('right click')
 
        QtWidgets.QPushButton.mousePressEvent(self, event)
 
app = QtWidgets.QApplication([])
window = PushButtonRight('Нажми меня')
window.show()
app.exec_()
