import sys
from PyQt5.QtCore import QMessageAuthenticationCode
from PyQt5.QtWidgets import * 
from untitled_python import * 



#-----------------------APP--------------#

app = QApplication(sys.argv)

pen_ana = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pen_ana)

pen_ana.show()



#----------------------------Critical--------------------#

def critical ():
    seçili = QMessageBox.critical(pen_ana,"Çık","Bu Uygulamdan Çıkış Yapma İstediğinize Eminmisniz",
    QMessageBox.Yes|QMessageBox.No)

    if seçili ==QMessageBox.No:
        ui.statusbar.showMessage("no butonu aktif edildi",10000)
    else:
        ui.statusbar.showMessage("yes butonu aktif edildi")


#----------------------Informatin------------------#

def information ():
    QMessageBox.information(pen_ana,"bilgi !","bu bir bilgilendirme mesajıdır.")




#----------------------------------Qestion-------------------
def qestion ():
    QMessageBox.question(pen_ana,"Soru","Bu bir Soru mesajidir",
                    QMessageBox.Yes|QMessageBox.No|QMessageBox.Save|QMessageBox.Open)


#------------------------Warmign------------------#
def warming():
    QMessageBox.warning(pen_ana,"dikat","bu bir uyarı mesajıdır")


#--------------------------------About-------------------#
def about():
    QMessageBox.about(pen_ana,"Geliştirici","<font size =5 Bu uygulama <b>Ferhat Çelik </b> tarafında geliştirilmiştir."
    
    "<br><br>"
    "<br> ""<br>"" Ferhat ÇElİK""<br>"" GİTHUB SAYFASINA BAK "
    "<br>"
    "<a href=\"https://www.yyu.edu.tr\" >YYU </a>"
    "<br><br>"
   "</font>" 
    )




#--------------------------Sinyal Solt--------------#
ui.pbt_critical.clicked.connect(critical)
ui.pbt_information.clicked.connect(information)
ui.pbt_qeston.clicked.connect(qestion )
ui.pbt_warming.clicked.connect(warming)
ui.pbt_about.clicked.connect(about)



sys.exit(app.exec_())