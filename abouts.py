from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap


butonFont = QFont("Arial", 12)
yaziFont = QFont("Arial", 14)

class Hakkinda(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hakkinda")
        self.setGeometry(50,50,400,400)
        self.setStyleSheet(("background-color:#ccffff"))

        self.baslik = QLabel("Hakkinda - Yardim", self)
        self.baslik.setFont(yaziFont)
        self.baslik.move(100,20)
        self.yazi = QLabel("Bu program sifirdan ileri seviye"
                           "\npython dersleri ogrencileri icin\nozel olarak tasarlandi.\n"
                           "Bu program ile birlikte artik\n"
                           "Python programlama beceriniz\n"
                           "cok daha iyi seviyeye gelecektir",self)
        self.yazi.setFont(yaziFont)
        self.yazi.move(80,80)
        self.resim = QLabel(self)
        self.resim.setPixmap(QPixmap('images/about.png'))
        self.resim.move(10,10)
