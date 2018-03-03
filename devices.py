# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devices.ui'
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


class Ui_get_device(object):
    def setupUi(self, get_device):
        get_device.setObjectName(_fromUtf8("get_device"))
        get_device.resize(495, 76)
        get_device.setMinimumSize(QtCore.QSize(495, 76))
        get_device.setMaximumSize(QtCore.QSize(495, 76))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Graphics/Icon/PyCloud-icon.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        get_device.setWindowIcon(icon)
        self.label = QtGui.QLabel(get_device)
        self.label.setGeometry(QtCore.QRect(0, -110, 511, 251))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_9 = QtGui.QLabel(get_device)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox = QtGui.QComboBox(get_device)
        self.comboBox.setGeometry(QtCore.QRect(290, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("font: 63 9pt \"Yu Gothic UI Semibold\";"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(get_device)
        QtCore.QMetaObject.connectSlotsByName(get_device)

    def retranslateUi(self, get_device):
        get_device.setWindowTitle(_translate("get_device", "Devices", None))
        self.label.setText(
            _translate("get_device", "<html><head/><body><p><img src=\":/Images/bg.png\"/>TextLabel</p></body></html>",
                       None))
        self.label_9.setText(_translate("get_device",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">Choose from your devices :</span></p></body></html>",
                                        None))


import PyCloudResource

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    get_device = QtGui.QWidget()
    ui = Ui_get_device()
    ui.setupUi(get_device)
    get_device.show()
    sys.exit(app.exec_())
