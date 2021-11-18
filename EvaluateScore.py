# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateScore.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score import Ui_dialog as score
import time
import sqlite3 as s
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(495, 499)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Footlight MT Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teamlist = QtWidgets.QListWidget(Form)
        self.teamlist.setObjectName("teamlist")
        self.verticalLayout.addWidget(self.teamlist)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.scorelist = QtWidgets.QListWidget(Form)
        self.scorelist.setObjectName("scorelist")
        self.verticalLayout_2.addWidget(self.scorelist)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.calculateBtn = QtWidgets.QPushButton(Form)
        self.calculateBtn.setObjectName("calculateBtn")
        self.verticalLayout_3.addWidget(self.calculateBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.datasetup()
        self.comboBox.addItems(self.tlist)
        self.calculateBtn.clicked.connect(self.calScore)
        self.p=0
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate Score"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.label_4.setText(_translate("Form", "Select Team"))
        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "Points"))
        self.calculateBtn.setText(_translate("Form", "Calculate Score"))
    def calScore(self):
        self.p=0
        self.teamlist.clear()
        self.scorelist.clear()
        item=self.comboBox.currentText()
        try:
             self.pcur.execute('select players from teams where name="{}";'.format(item))
             l=self.pcur.fetchall()
             self.tlist=[]
             for i in l:
                 for j in i:
                     if j not in self.tlist:
                        self.tlist.append(j)
             self.teamlist.addItems(self.tlist)
             self.calPoints(self.tlist)
             self.scorewin=QtWidgets.QDialog()
             self.scoreui=score()
             self.scoreui.setupUi(self.scorewin)
             self.scorewin.show()
             self.scoreui.scorecard.setText(str(sum(self.plist)))
             self.plist=[]
             self.scoreui.okscore.clicked.connect(self.c)
        except Exception as e:
             print(e)
    def c(self):
        self.scorewin.close()
    def calPoints(self,tlist):
        for i in self.tlist:
            self.pcur.execute('select value,ctg from stats where player="{}";'.format(i))
            temp=self.pcur.fetchone()
            self.playerScore(temp,i)
    def playerScore(self,temp,p):
        try:
            self.p2cur.execute('select * from match where Player="{}";'.format(p))
            x=self.p2cur.fetchone()
            self.score(x) 
        except Exception as e:
            print(e)
    def score(self,x):
        self.p=0
        runs=x[1]
        balls=x[2]
        field=x[9]+x[10]+x[11]
        four=x[3]
        six=x[4]
        bowled=x[5]
        maiden=x[6]
        given=x[7]
        wkt=x[8]
        self.p=runs/2
        if runs>=50:
          self.p=self.p+5
        if runs>=100:
          self.p=self.p+10
        try:
            economy=(given/bowled)*6
        except:
            economy=0
        if economy>3.5 and economy<=4.5:
            self.p=self.p+4
        if economy>=2 and economy<=3.5:
            self.p=self.p+7
        if economy<2:
            self.p=self.p+10
        self.p=self.p+wkt*10
        if wkt>=3:
            self.p=self.p+5
        if wkt>=5:
            self.p=self.p+10
        try:
            sr=(runs/balls)*100
        except:
            sr=0
        if sr>80 and sr<100:
            self.p=self.p+2
        if sr>100 :
            self.p=self.p+4

        self.p=self.p+four+six*2+field*10
        self.plist.append(self.p)
        self.scorelist.addItem(str(self.p))
    def datasetup(self):
        self.pconn=s.connect('CricketFantasyDB.db')
        self.pcur=self.pconn.cursor()
        self.p2cur=self.pconn.cursor()
        self.pcur.execute('select distinct name from teams;')
        self.record=self.pcur.fetchall()
        self.d={}
        self.plist=[]
        self.tlist=[]
        self.listx=[]
        for i in self.record:
            self.listx.append(i)
        for j in self.listx:
                self.tlist.append(j[0])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
