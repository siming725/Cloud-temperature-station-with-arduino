import os,sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication([])
view = QWebEngineView()
view.load(QUrl('file:///'+os.getcwd().replace('\\','/')+'/index.html'))
view.show()
app.exec_()
