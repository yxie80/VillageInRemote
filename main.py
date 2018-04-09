        
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:45:05 2018

@author: Nan
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

from Client import Client

class main(QDialog):
    client = Client()    
    filename = ''
    
    def __init__(self):
        super(main, self).__init__()
        loadUi('uploadModule.ui', self)
        self.setWindowTitle('File uploading!')
        self.submitButton.clicked.connect(self.on_submitButton_clicked)
#        self.submitButton.clicked.connect(self.open_selectionModule)
        
    @pyqtSlot()
    def on_submitButton_clicked(self):
        # set the file path in the lineEdit into filename
        self.filename = self.filePathInput.text()     
#        self.label_2.setText(self.filename)
        # call the upload function in an object of Client, and use filename as input arg
        self.client.upload_file(self.filename)
        if self.client.output == "File Not Found!":
            self.label_2.setText(self.client.output)
        elif self.client.output == "SyntaxError, file path should be C:/Users/data.csv":
            self.label_2.setText(self.client.output)
        elif self.client.output == 'Pass':
            self.newD = SelectionModule() # once the file has been successfully read, create an object of new ui
            self.newD.show() # show second widget
            self.hide() # hide the main widget
            self.newD.track_label.setText(str(self.client.listOfFields))
#        self.label_3.setText(self.client.output)
        
#    def open_selectionModule(self):
#        self.newD = SelectionModule(self)
#        self.newD.show()


class SelectionModule(QDialog):
   
    def __init__(self):
        super(SelectionModule,self).__init__()
        loadUi('selectionModule.ui',self)
        self.setWindowTitle('Question selection!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = main()
    widget.show()


>>>>>>> master:main.py
    sys.exit(app.exec_())