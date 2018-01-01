# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Pycloud(object):
    def setupUi(self, Pycloud):
        Pycloud.setObjectName(_fromUtf8("Pycloud"))
        Pycloud.resize(863, 560)
        Pycloud.setMinimumSize(QtCore.QSize(863, 560))
        Pycloud.setMaximumSize(QtCore.QSize(863, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Graphics/Icon/PyCloud-icon.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Pycloud.setWindowIcon(icon)
        self.label = QtGui.QLabel(Pycloud)
        self.label.setGeometry(QtCore.QRect(-10, 0, 881, 571))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Pycloud)
        self.commandLinkButton.setGeometry(QtCore.QRect(770, 300, 51, 51))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.commandLinkButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/log-in-button-with-arrow.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.username = QtGui.QLineEdit(Pycloud)
        self.username.setGeometry(QtCore.QRect(490, 250, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setMouseTracking(False)
        self.username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.username.setStyleSheet(_fromUtf8("color: #b9b9b9;"))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(Pycloud)
        self.password.setGeometry(QtCore.QRect(490, 300, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet(_fromUtf8("color: #b9b9b9;"))
        self.password.setObjectName(_fromUtf8("password"))
        self.label_6 = QtGui.QLabel(Pycloud)
        self.label_6.setGeometry(QtCore.QRect(540, 160, 171, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(Pycloud)
        self.label_4.setGeometry(QtCore.QRect(90, 380, 281, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semilight"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(Pycloud)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(120, 480, 211, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.commandLinkButton_2.setToolTip(_fromUtf8(""))
        self.commandLinkButton_2.setStyleSheet(_fromUtf8("color: #ececec;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/instruction-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon2)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.label_2 = QtGui.QLabel(Pycloud)
        self.label_2.setGeometry(QtCore.QRect(-40, -40, 431, 441))
        self.label_2.setStyleSheet(_fromUtf8("image: url(:/logo/AppleLogo.png);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Pycloud)
        QtCore.QMetaObject.connectSlotsByName(Pycloud)
        Pycloud.setTabOrder(self.username, self.password)

    def retranslateUi(self, Pycloud):
        Pycloud.setWindowTitle(_translate("Pycloud", "PyCloud", None))
        self.label.setText(
            _translate("Pycloud", "<html><head/><body><p><img src=\":/Images/bg.png\"/></p></body></html>", None))
        self.commandLinkButton.setToolTip(_translate("Pycloud", "Log In", None))
        self.username.setToolTip(_translate("Pycloud", "<html><head/><body><p>Username</p></body></html>", None))
        self.username.setText(_translate("Pycloud", "Username", None))
        self.password.setToolTip(_translate("Pycloud", "Password", None))
        self.password.setText(_translate("Pycloud", "Password", None))
        self.label_6.setText(_translate("Pycloud",
                                        "<html><head/><body><p><span style=\" color:#f7f9fb;font-size:30pt; font-weight:600;\">Sign In</span></p></body></html>",
                                        None))
        self.label_4.setText(_translate("Pycloud",
                                        "<html><head/><body><p><span style=\" font-size:45pt; color:#f7f9fb;\">PyCloud</span></p></body></html>",
                                        None))
        self.commandLinkButton_2.setText(_translate("Pycloud", "Instructions", None))
        self.label_2.setText(_translate("Pycloud",
                                        "<html><head/><body><p><img src=\":/Images/Graphics/Icon/PyCloud.png\"/></p></body></html>",
                                        None))


import PyCloudResource

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Pycloud = QtGui.QWidget()
    ui = Ui_Pycloud()
    ui.setupUi(Pycloud)
    Pycloud.show()
    sys.exit(app.exec_())
