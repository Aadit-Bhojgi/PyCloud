# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Auth2f.ui'
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


class Ui_Verify(object):
    def setupUi(self, Verify):
        Verify.setObjectName(_fromUtf8("Verify"))
        Verify.resize(438, 226)
        Verify.setMinimumSize(QtCore.QSize(438, 226))
        Verify.setMaximumSize(QtCore.QSize(438, 226))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Graphics/Icon/PyCloud-icon.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Verify.setWindowIcon(icon)
        Verify.setStyleSheet(_fromUtf8(""))
        self.label_9 = QtGui.QLabel(Verify)
        self.label_9.setGeometry(QtCore.QRect(50, 0, 341, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label = QtGui.QLabel(Verify)
        self.label.setGeometry(QtCore.QRect(-10, -10, 451, 241))
        self.label.setObjectName(_fromUtf8("label"))
        self.otp = QtGui.QLineEdit(Verify)
        self.otp.setGeometry(QtCore.QRect(40, 120, 301, 60))
        self.otp.setStyleSheet(_fromUtf8("font: 63 28pt \"Yu Gothic UI Semibold\";"))
        self.otp.setMaxLength(6)
        self.otp.setAlignment(QtCore.Qt.AlignCenter)
        self.otp.setObjectName(_fromUtf8("otp"))
        self.warning_send = QtGui.QLabel(Verify)
        self.warning_send.setGeometry(QtCore.QRect(90, 190, 251, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.warning_send.setFont(font)
        self.warning_send.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.warning_send.setObjectName(_fromUtf8("warning_send"))
        self.warning_verify = QtGui.QLabel(Verify)
        self.warning_verify.setGeometry(QtCore.QRect(90, 190, 251, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.warning_verify.setFont(font)
        self.warning_verify.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.warning_verify.setObjectName(_fromUtf8("warning_verify"))
        self.send_otp = QtGui.QCommandLinkButton(Verify)
        self.send_otp.setGeometry(QtCore.QRect(360, 130, 41, 41))
        self.send_otp.setText(_fromUtf8(""))
        self.send_otp.setObjectName(_fromUtf8("send_otp"))
        self.label_10 = QtGui.QLabel(Verify)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 291, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Verify)
        self.label_11.setGeometry(QtCore.QRect(20, 70, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.number_combo = QtGui.QComboBox(Verify)
        self.number_combo.setGeometry(QtCore.QRect(310, 60, 121, 22))
        self.number_combo.setStyleSheet(_fromUtf8("font: 63 9pt \"Yu Gothic UI Semibold\";"))
        self.number_combo.setObjectName(_fromUtf8("number_combo"))
        self.label.raise_()
        self.label_9.raise_()
        self.otp.raise_()
        self.warning_send.raise_()
        self.warning_verify.raise_()
        self.send_otp.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.number_combo.raise_()

        self.retranslateUi(Verify)
        QtCore.QMetaObject.connectSlotsByName(Verify)

    def retranslateUi(self, Verify):
        Verify.setWindowTitle(_translate("Verify", "Authentication", None))
        self.label_9.setText(_translate("Verify",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">Two-step authentication required</span></p></body></html>",
                                        None))
        self.label.setText(
            _translate("Verify", "<html><head/><body><p><img src=\":/Images/login_bg.png\"/></p></body></html>", None))
        self.warning_send.setText(_translate("Verify",
                                             "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; color:#ff0000;\">Failed to send verification code.</span></p></body></html>",
                                             None))
        self.warning_verify.setText(_translate("Verify",
                                               "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; color:#ff0000;\">Failed to verify verification code.</span></p></body></html>",
                                               None))
        self.label_10.setText(_translate("Verify",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:400; color:#f7f9fb;\">Choose from trusted Numbers :</span></p></body></html>",
                                         None))
        self.label_11.setText(_translate("Verify",
                                         "<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#f7f9fb;\">(Text Message will be sent to the selected)</span></p></body></html>",
                                         None))


import PyCloudResource

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Verify = QtGui.QWidget()
    ui = Ui_Verify()
    ui.setupUi(Verify)
    Verify.show()
    sys.exit(app.exec_())
