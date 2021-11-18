# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from newTeam import Ui_Dialog as newTeam
from score import Ui_dialog as saveCard
from EvaluateScore import Ui_Form as evaluateScore
import sqlite3 as s

pconn=s.connect('CricketFantasyDB.db')
pcur=pconn.cursor()


batsmen={'Kohli':'bat','Yuvraj':'bat','Rahane':'bat','Dhoni':'bat','Rohit':'bat'}
bowlers={'Axar':'bow','Pandya':'bow','Jadeja':'bow','Kedar':'bow'}
allrounders={'Dhawan':'ar','Ashwin':'ar','Bhuwaneshwar':'ar','Kartick':'ar'}
wicketkeepers={'Umesh':'wk','Bumrah':'wk'}
batsmenL=list(batsmen.keys())
bowlersL=list(bowlers.keys())
allroundersL=list(allrounders.keys())
wicketkeepersL=list(wicketkeepers.keys())
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.batno = QtWidgets.QLineEdit(self.centralwidget)
        self.batno.setObjectName("batno")
        self.horizontalLayout_5.addWidget(self.batno)
        self.label_bow = QtWidgets.QLabel(self.centralwidget)
        self.label_bow.setObjectName("label_bow")
        self.horizontalLayout_5.addWidget(self.label_bow)
        self.bowno = QtWidgets.QLineEdit(self.centralwidget)
        self.bowno.setObjectName("bowno")
        self.horizontalLayout_5.addWidget(self.bowno)
        self.labelar = QtWidgets.QLabel(self.centralwidget)
        self.labelar.setObjectName("labelar")
        self.horizontalLayout_5.addWidget(self.labelar)
        self.arno = QtWidgets.QLineEdit(self.centralwidget)
        self.arno.setObjectName("arno")
        self.horizontalLayout_5.addWidget(self.arno)
        self.wknolabel = QtWidgets.QLabel(self.centralwidget)
        self.wknolabel.setObjectName("wknolabel")
        self.horizontalLayout_5.addWidget(self.wknolabel)
        self.wkno = QtWidgets.QLineEdit(self.centralwidget)
        self.wkno.setObjectName("wkno")
        self.horizontalLayout_5.addWidget(self.wkno)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pointsAvailable = QtWidgets.QLineEdit(self.centralwidget)
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.horizontalLayout_2.addWidget(self.pointsAvailable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pointsUsed = QtWidgets.QLineEdit(self.centralwidget)
        self.pointsUsed.setObjectName("pointsUsed")
        self.horizontalLayout_3.addWidget(self.pointsUsed)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bat = QtWidgets.QRadioButton(self.centralwidget)
        self.bat.setObjectName("bat")
        self.horizontalLayout_4.addWidget(self.bat)
        self.bow = QtWidgets.QRadioButton(self.centralwidget)
        self.bow.setObjectName("bow")
        self.horizontalLayout_4.addWidget(self.bow)
        self.ar = QtWidgets.QRadioButton(self.centralwidget)
        self.ar.setObjectName("ar")
        self.horizontalLayout_4.addWidget(self.ar)
        self.wk = QtWidgets.QRadioButton(self.centralwidget)
        self.wk.setObjectName("wk")
        self.horizontalLayout_4.addWidget(self.wk)
        spacerItem2 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.teamNameShow = QtWidgets.QLineEdit(self.centralwidget)
        self.teamNameShow.setObjectName("teamNameShow")
        self.horizontalLayout_4.addWidget(self.teamNameShow)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerlist1 = QtWidgets.QListWidget(self.centralwidget)
        self.playerlist1.setObjectName("playerlist1")
        self.horizontalLayout.addWidget(self.playerlist1)
        self.playerlist2 = QtWidgets.QListWidget(self.centralwidget)
        self.playerlist2.setObjectName("playerlist2")
        self.horizontalLayout.addWidget(self.playerlist2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_team = QtWidgets.QAction(MainWindow)
        self.actionNew_team.setObjectName("actionNew_team")
        self.actionOpen_team = QtWidgets.QAction(MainWindow)
        self.actionOpen_team.setObjectName("actionOpen_team")
        self.actionSave_team = QtWidgets.QAction(MainWindow)
        self.actionSave_team.setObjectName("actionSave_team")
        self.actionEvaluate_team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_team.setObjectName("actionEvaluate_team")
        self.menuManage_Teams.addAction(self.actionNew_team)
        self.menuManage_Teams.addAction(self.actionOpen_team)
        self.menuManage_Teams.addAction(self.actionSave_team)
        self.menuManage_Teams.addAction(self.actionEvaluate_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.actionSlot)
        self.playerlist1.itemDoubleClicked.connect(self.movetolist2)
        self.playerlist2.itemDoubleClicked.connect(self.movetolist1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket Game"))
        self.label_7.setText(_translate("MainWindow", "Your Selections"))
        self.label_3.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.batno.setText(_translate("MainWindow", "##"))
        self.label_bow.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.bowno.setText(_translate("MainWindow", "##"))
        self.labelar.setText(_translate("MainWindow", "Allrounder(AR)"))
        self.arno.setText(_translate("MainWindow", "##"))
        self.wknolabel.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.wkno.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Points Available"))
        self.pointsAvailable.setText(_translate("MainWindow", "####"))
        self.label_2.setText(_translate("MainWindow", "Points Used"))
        self.pointsUsed.setText(_translate("MainWindow", "####"))
        self.bat.setText(_translate("MainWindow", "BAT"))
        self.bow.setText(_translate("MainWindow", "BOW"))
        self.ar.setText(_translate("MainWindow", "AR"))
        self.wk.setText(_translate("MainWindow", "WK"))
        self.label_4.setText(_translate("MainWindow", "Team name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_team.setText(_translate("MainWindow", "New team"))
        self.actionOpen_team.setText(_translate("MainWindow", "Open team"))
        self.actionSave_team.setText(_translate("MainWindow", "Save team"))
        self.actionEvaluate_team.setText(_translate("MainWindow", "Evaluate team"))
        
    def actionSlot(self,action):
        txt=action.text()
        if txt=='New team':
            self.playerlist1.clear()
            self.playerlist2.clear()
            self.teamNameWindow=QtWidgets.QDialog()
            self.dialog=newTeam()
            self.dialog.setupUi(self.teamNameWindow)
            self.teamNameWindow.show()
            self.dialog.pushButton.clicked.connect(self.getTname)
            self.bat.toggled.connect(self.checkplayerlist1)
            self.bat.setCheckable(True)
            self.bow.toggled.connect(self.checkplayerlist1)
            self.ar.toggled.connect(self.checkplayerlist1)
            self.wk.toggled.connect(self.checkplayerlist1)
            self.x=1000
            self.y=0
            self.playerNumberStats()

        elif txt=='Save team':
            playerSelected=[]
            l=list(batsmen)+list(bowlers)+list(allrounders)+list(wicketkeepers)
            t=batsmenL+bowlersL+allroundersL+wicketkeepersL
            for i in t:
                if i not in l:
                    playerSelected.append(i)
            self.saveList(playerSelected)

        elif txt=='Open team':
            self.clearData()
            try:
                self.openteamWindow=QtWidgets.QDialog()
                self.opendialog=newTeam()
                self.opendialog.setupUi(self.openteamWindow)
                self.openteamWindow.show()
                self.opendialog.pushButton.clicked.connect(self.openTname)
                
            except Exception as e:
                print(e)
        elif txt=='Evaluate team':
            self.clearData()
            try:
               self.ewin=QtWidgets.QWidget()
               self.eui=evaluateScore()
               self.eui.setupUi(self.ewin)
               self.ewin.show()
            except Exception as e:
                print(e)

    def checkplayerlist1(self):
        self.playerlist1.clear()
        if self.bat.isChecked():
            self.playerlist1.addItems(batsmen.keys())
        elif self.bow.isChecked():
            self.playerlist1.addItems(bowlers.keys())
        elif self.ar.isChecked():
            self.playerlist1.addItems(allrounders.keys())
        elif self.wk.isChecked():
            self.playerlist1.addItems(wicketkeepers.keys())
            
    def playerNumberStats(self):
        self.batno.setText(str(5-len(batsmen)))
        self.bowno.setText(str(4-len(bowlers)))
        self.arno.setText(str(4-len(allrounders)))
        self.wkno.setText(str(2-len(wicketkeepers)))
        self.pointsAvailable.setText(str(abs(self.x)))
        self.pointsUsed.setText(str(abs(self.y)))
            
    def movetolist2(self,item):
        if len(self.playerlist2)==11:
            self.errorWindow=QtWidgets.QDialog()
            self.errordialog=saveCard()
            self.errordialog.setupUi(self.errorWindow)
            self.errorWindow.show()
            self.errordialog.label.setText("can't select more than 11 players")
        else:    
            self.playerlist1.takeItem(self.playerlist1.row(item))
            if self.x>0:
                pcur.execute('select value from stats where player="{}";'.format(item.text()))
                self.minusPoints=pcur.fetchone()
                self.x=self.x-self.minusPoints[0]
                self.y=self.y+self.minusPoints[0]
                if self.x<0:
                    self.playerlist1.addItem(item.text())
                    self.errorWindow=QtWidgets.QDialog()
                    self.errordialog=saveCard()
                    self.errordialog.setupUi(self.errorWindow)
                    self.errorWindow.show()
                    self.errordialog.label.setText('No sufficent points to add this Player')
                    self.x=self.x+self.minusPoints[0]
                    self.y=self.y-self.minusPoints[0]
                else:
                    if self.wk.isChecked() and len(wicketkeepers)==1:
                            self.errorwk(item)
                    else:        
                        self.playerlist2.addItem(item.text())
                        if self.bat.isChecked():
                            batsmen.pop(item.text())
                        elif self.bow.isChecked():
                            bowlers.pop(item.text())
                        elif self.ar.isChecked():
                            allrounders.pop(item.text())
                        elif self.wk.isChecked():
                             wicketkeepers.pop(item.text())
                        self.playerNumberStats()
        
    def movetolist1(self,item):
        try:
            self.playerlist2.takeItem(self.playerlist2.row(item))
            pcur.execute('select value from stats where player="{}";'.format(item.text()))
            self.minusPoints=pcur.fetchone()
            self.x=self.x+self.minusPoints[0]
            self.y=self.y-self.minusPoints[0]
            if item.text() in batsmenL:
                self.bat.setCheckable(True)
                self.playerlist1.addItem(item.text())
                batsmen[item.text()]='bat'
            elif item.text() in bowlersL:
                self.bow.setCheckable(True)
                self.playerlist1.addItem(item.text())
                bowlers[item.text()]='bow'
            elif item.text() in allroundersL:
                self.ar.setCheckable(True)
                self.playerlist1.addItem(item.text())
                allrounders[item.text()]='ar'
            elif item.text() in wicketkeepersL:
                self.wk.setCheckable(True)
                self.playerlist1.addItem(item.text())
                wicketkeepers[item.text()]='wk'
            self.playerNumberStats()
        except Exception as e:
            print(e)
            
    def errorwk(self,item):
            self.errorWindow=QtWidgets.QDialog()
            self.errordialog=saveCard()
            self.errordialog.setupUi(self.errorWindow)
            self.errorWindow.show()
            self.errordialog.label.setText("can't select more than 1 wicket-Keeper")
            self.movetolist1(item)
    def getTname(self):
            self.teamNameShow.setText(self.dialog.lineEdit.text())
            self.teamName=self.teamNameShow.text()
            
    def openTname(self):
        self.openteamName=self.opendialog.lineEdit.text()
        self.teamNameShow.setText(self.opendialog.lineEdit.text())
        try:
            pcur.execute('select players from teams where name="{}";'.format(self.openteamName))
            pconn.commit()
            record=pcur.fetchall()
            olist=[]
            for i in record:
                for j in i:
                    olist.append(j)
            for i in olist:
                self.playerlist2.addItem(str(i))
            t=batsmenL+bowlersL+allroundersL+wicketkeepersL
            for k in t:
                if k not in olist:
                    if k in batsmenL:
                        self.bat.setCheckable(True)
                        self.playerlist1.addItem(k)
                    elif k in bowlersL:
                        self.bow.setCheckable(True)
                        self.playerlist1.addItem(k)
                    elif k in allroundersL:
                        self.ar.setCheckable(True)
                        self.playerlist1.addItem(k)
                    elif k in wicketkeepersL:
                        self.wk.setCheckable(True)
                        self.playerlist1.addItem(k)
            self.playerlist1.itemDoubleClicked.connect(self.movetolist2)
            self.playerlist2.itemDoubleClicked.connect(self.movetolist1)
        except Exception as e:
            print(e)

    def saveList(self,plist):
        for i in plist:
            pcur.execute("insert into teams(name,players) values(?,?);",(str(self.teamName),str(i)))
        pconn.commit()
        self.saveWindow=QtWidgets.QDialog()
        self.savedialog=saveCard()
        self.savedialog.setupUi(self.saveWindow)
        self.saveWindow.show()
        self.savedialog.label.setText('Saved Sucessfully')
        self.savedialog.okscore.clicked.connect(self.c)
        self.clearData()
    def clearData(self):
        self.batno.setText('0')
        self.bowno.setText('0')
        self.arno.setText('0')
        self.wkno.setText('0')
        self.pointsAvailable.setText('####')
        self.pointsUsed.setText('0')
        self.playerlist1.clear()
        self.playerlist2.clear()
        self.teamNameShow.setText('NA')
    def c(self):
        self.saveWindow.close()       
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
