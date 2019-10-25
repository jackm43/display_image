import sys
from PyQt4 import QtGui
import urllib.request

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)

        url = 'http://www.google.com/images/srpr/logo1w.png'
        data = urllib.request.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(QtGui.QPixmap(image))

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()