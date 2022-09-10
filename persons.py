import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
import sqlite3
import addPerson


butonFont = QFont("Arial", 12)
yaziFont = QFont("Arial", 16)

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

class Person(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,500)

        baslik = QLabel("Kisilerim",self)
        baslik.setFont(yaziFont)
        baslik.move(210,70)
        resim = QLabel(self)
        resim.setPixmap(QPixmap('images/person.png'))
        resim.move(100,40)
        #################################################
        self.liste = QListWidget(self)
        self.liste.move(110,100)
        kisi = cursor.execute("SELECT *from kisiler")
        for i in kisi.fetchall():
            self.liste.addItem(str(i[0])+ "- "+i[1]+ " "+ i[2])


        #################################################
        addButon = QPushButton("Kisi Ekle",self)
        addButon.setFont(butonFont)
        addButon.move(380,100)
        addButon.clicked.connect(self.kisiEkle)
        #################################################
        updateButon = QPushButton("Duzenle", self)
        updateButon.setFont(butonFont)
        updateButon.move(380,140)
        updateButon.clicked.connect(self.kisiDuzenle)
        ##################################################
        displayButon = QPushButton("Goruntule",self)
        displayButon.setFont(butonFont)
        displayButon.move(380,180)
        displayButon.clicked.connect(self.kisiGoruntule)
        ##########################################
        deleteButon = QPushButton("Sil",self)
        deleteButon.setFont(butonFont)
        deleteButon.move(380,220)
        deleteButon.clicked.connect(self.kisiSil)





    def kisiEkle(self):
        self.ekle = kisiEkle.Ekle()
        self.ekle.show()
        self.close()
    def kisiSil(self):
        kisi = self.liste.currentItem().text()
        id = kisi.split("-")[0]
        onay = QMessageBox.question(self,"Uyari","Silmek istiyor musunuz??", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if (onay == QMessageBox.Yes):


            try :
                cursor.execute("DELETE from kisiler where kisi_id = ?",(id,))
                connect.commit()
                QMessageBox.information(self,"Bilgi","Kayit Silindi")

            except:
                QMessageBox.information(self,"Hata","Kayit Silinemedi")

            self.close()

    def kisiDuzenle(self):
        self.kisi = self.liste.currentItem().text()
        global kisi_id
        kisi_id = self.kisi.split("-")[0]

        self.duzenle = Duzenle()
        self.duzenle.show()
        self.close()

    def kisiGoruntule(self):
        self.kisi = self.liste.currentItem().text()
        global kisi_id
        kisi_id = self.kisi.split("-")[0]

        self.goruntule = Goruntule()
        self.goruntule.show()
        self.close()

class Goruntule(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kisi Goruntule")
        self.setGeometry(50,50,500,500)


        try:
            sorgu  = cursor.execute("SELECT * from kisiler where kisi_id = ?",(kisi_id))
            kisi_bilgi =sorgu.fetchall()
            self.kisi_id = kisi_bilgi[0][0]
            kisi_isim = kisi_bilgi[0][1]
            kisi_soyisim  = kisi_bilgi[0][2]
            kisi_yas = kisi_bilgi[0][3]
            kisi_adres = kisi_bilgi[0][4]


        except:
            QMessageBox.information(self,"Hata","Databasee ulasilamadi")


        baslik = QLabel("Kisi Duzenle",self)
        baslik.move(150,40)
        baslik.setFont(yaziFont)
        ################################
        resim = QLabel(self)
        resim.setPixmap(QPixmap('images/about.png'))
        resim.move(80, 40)
        ####################################
        self.isim =QLineEdit(self)
        self.isim.move(150,70)
        self.isim.setText(kisi_isim)
        self.isim.setReadOnly(True)
        ####################################
        self.soyisim =QLineEdit(self)
        self.soyisim.move(150,100)
        self.soyisim.setText(kisi_soyisim)
        self.soyisim.setReadOnly(True)
        ####################################
        self.yas = QComboBox(self)
        self.yas.move(150,130)
        self.yas.resize(80,25)
        for i in range(18,101):
            self.yas.addItem(str(i))
        self.yas.setCurrentText(kisi_yas)
        self.yas.setDisabled(True)
        ######################################
        self.adres = QTextEdit(self)
        self.adres.move(150,160)
        self.adres.setText(kisi_adres)
        self.adres.setReadOnly(True)

class Duzenle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kisi Duzenle")
        self.setGeometry(50,50,500,500)

        try:
            sorgu  = cursor.execute("SELECT * from kisiler where kisi_id = ?",(kisi_id))
            kisi_bilgi =sorgu.fetchall()
            self.kisi_id = kisi_bilgi[0][0]
            kisi_isim = kisi_bilgi[0][1]
            kisi_soyisim  = kisi_bilgi[0][2]
            kisi_yas = kisi_bilgi[0][3]
            kisi_adres = kisi_bilgi[0][4]


        except:
            QMessageBox.information(self,"Hata","Databasee ulasilamadi")


        baslik = QLabel("Kisi Duzenle",self)
        baslik.move(150,40)
        baslik.setFont(yaziFont)
        ################################
        resim = QLabel(self)
        resim.setPixmap(QPixmap('images/user.png'))
        resim.move(80, 40)
        ####################################
        self.isim =QLineEdit(self)
        self.isim.move(150,70)
        self.isim.setText(kisi_isim)
        ####################################
        self.soyisim =QLineEdit(self)
        self.soyisim.move(150,100)
        self.soyisim.setText(kisi_soyisim)
        ####################################
        self.yas = QComboBox(self)
        self.yas.move(150,130)
        self.yas.resize(80,25)
        for i in range(18,101):
            self.yas.addItem(str(i))
        self.yas.setCurrentText(kisi_yas)
        ######################################
        self.adres = QTextEdit(self)
        self.adres.move(150,160)
        self.adres.setText(kisi_adres)
        ######################################
        duzenleButon = QPushButton("Duzenle",self)
        duzenleButon.setFont(butonFont)
        duzenleButon.move(330,360)
        duzenleButon.clicked.connect(self.kisiGuncelle)
        ######################################


    def kisiGuncelle(self):

        kisi_id = self.kisi_id
        isim = self.isim.text()
        soyisim =self.soyisim.text()
        yas  = self.yas.currentText()
        adres = self.adres.toPlainText()
        print(kisi_id)
        print(isim)
        print(soyisim)
        print(yas)
        print(adres)

        try:
            cursor.execute("UPDATE kisiler set isim = ?, soyisim = ?, yas= ?, adres = ? where kisi_id = ?",(isim,soyisim,yas,adres,kisi_id))
            connect.commit()

            QMessageBox.information(self,"Bilgi","Kisi Guncellendi")
            self.close()
        except:
            QMessageBox.information(self,"Bilgi","Kisi Guncellenmedi")
























