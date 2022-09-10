import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
import sqlite3


butonFont = QFont("Arial", 12)
yaziFont = QFont("Arial", 16)

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

class Ekle(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Kisi Ekle")

        baslik = QLabel("Kisi Ekle",self)
        baslik.move(210,40)
        baslik.setFont(yaziFont)
        resim = QLabel(self)
        resim.setPixmap(QPixmap('images/add.png'))
        resim.move(140,5)
        #####################################################
        self.isim = QLineEdit(self)
        self.isim.move(150,90)
        self.isim.setPlaceholderText("Lutfen bir isim giriniz")
        #######################################################
        self.soyisim = QLineEdit(self)
        self.soyisim.move(150,120)
        self.soyisim.setPlaceholderText("Lutfen bir soyisim giriniz")
        ########################################################
        self.yas = QComboBox(self)
        self.yas.move(150,150)
        self.yas.resize(80,25)
        for i in range(18,101):
            self.yas.addItem(str(i))
        ########################################################
        self.adres = QTextEdit(self)
        self.adres.move(150,180)
        ########################################################
        eklebuton = QPushButton("Ekle",self)
        eklebuton.setFont(butonFont)
        eklebuton.move(330,380)
        eklebuton.clicked.connect(self.ekle)



    def ekle(self):
        isim = self.isim.text()
        soyisim = self.soyisim.text()
        yas = self.yas.currentText()
        adres = self.adres.toPlainText()
        if(isim and soyisim and adres !=""):

            try:
                cursor.execute("INSERT into kisiler(isim,soyisim,yas,adres) VALUES (?,?,?,?)", (isim,soyisim,yas,adres))
                connect.commit()
                QMessageBox.information(self,"Bilgi","Veriler Eklendi!!!")
                self.isim.setText("")
                self.soyisim.setText("")
                self.yas.setCurrentIndex(0)
                self.adres.setText("")

            except:
                QMessageBox.information(self,"Hata","Veriler Eklenmedi!!!")
        else:
            QMessageBox.information(self, "Hata", "Alanlar Bos olamaz!!!")



