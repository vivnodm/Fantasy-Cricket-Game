# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(281, 149)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.scorecard = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(10)
        self.scorecard.setFont(font)
        self.scorecard.setTextFormat(QtCore.Qt.PlainText)
        self.scorecard.setAlignment(QtCore.Qt.AlignCenter)
        self.scorecard.setObjectName("scorecard")
        self.horizontalLayout.addWidget(self.scorecard)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.okscore = QtWidgets.QPushButton(dialog)
        self.okscore.setObjectName("okscore")
        self.verticalLayout.addWidget(self.okscore)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
    
    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Score"))
        self.label.setText(_translate("dialog", "Your Score"))
        self.scorecard.setText(_translate("dialog", " "))
        self.okscore.setText(_translate("dialog", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
