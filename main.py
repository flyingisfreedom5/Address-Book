import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
import persons, addPerson, abouts

butonFont = QFont("Arial", 12)
yaziFont = QFont("Arial", 16)

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Adres Defteri")
        self.setGeometry(50,50,400,400)
        self.setStyleSheet(("background-color:#ccffff"))
        self.arayuz()


    def arayuz(self):
        kisilerButon = QPushButton("Kisi Listesi",self)
        kisilerButon.setStyleSheet("background-color:white")
        kisilerButon.resize(134,25)
        kisilerButon.move(150,50)
        kisilerButon.setFont(butonFont)
        kisilerButon.setIcon(QIcon('images/person.png'))
        kisilerButon.clicked.connect(self.kisiler)
        ######################################################
        ekleButon = QPushButton("Kisi Ekle", self)
        ekleButon.setStyleSheet("background-color:white")
        ekleButon.resize(134, 25)
        ekleButon.move(150, 100)
        ekleButon.setFont(butonFont)
        ekleButon.setIcon(QIcon('images/add.png'))
        ekleButon.clicked.connect(self.kisiEkle)
        #####################################################
        yardimButon = QPushButton("Hakkinda", self)
        yardimButon.setStyleSheet("background-color:white")
        yardimButon.resize(134, 25)
        yardimButon.move(150, 150)
        yardimButon.setFont(butonFont)
        yardimButon.setIcon(QIcon('images/about.png'))
        yardimButon.clicked.connect(self.hakkindaSayfasi)
        self.show()

    def kisiler(self):
        self.kisi = persons.Person()
        self.kisi.show()

    def kisiEkle(self):
        self.ekle = addPerson.Ekle()
        self.ekle.show()
    def hakkindaSayfasi(self):
        self.hakkinda = abouts.Hakkinda()
        self.hakkinda.show()



def main():
    uygulama = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(uygulama.exec_())

if __name__=='__main__':
    main()

