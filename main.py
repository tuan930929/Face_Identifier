import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        trainingButton = QtGui.QPushButton("Training")
        detectButton = QtGui.QPushButton("Detect")
        quitButton = QtGui.QPushButton("Quit")

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(trainingButton)
        hbox.addWidget(detectButton)
        hbox.addWidget(quitButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setFixedSize(500,50)
        self.move(300,300)
        self.setWindowTitle('Timekeeper by Face Application')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()