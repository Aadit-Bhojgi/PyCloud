# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Instruction.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(870, 793)
        Dialog.setMinimumSize(QtCore.QSize(870, 793))
        Dialog.setMaximumSize(QtCore.QSize(870, 793))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/Graphics/Icon/PyCloud-icon.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 871, 801))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 550, 791))
        self.label_2.setMinimumSize(QtCore.QSize(550, 791))
        self.label_2.setMaximumSize(QtCore.QSize(550, 791))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 231, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 421, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 401, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 451, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 560, 421, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 640, 281, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 720, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(230, 720, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(20, 310, 461, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PyCloud - Instructions", None))
        self.label.setText(
            _translate("Dialog", "<html><head/><body><p><img src=\":/Images/bg.png\"/></p></body></html>", None))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p><img src=\":/Images/Graphics/GUI Images/screen.png\"/></p></body></html>",
                                        None))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#f7f9fb;font-size:18pt; font-weight:600;\">Before you begin</span></p></body></html>",
                                        None))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#f7f9fb;font-size:13pt; font-weight:600;\">1. Update your iPhone, iPad, or iPod touch <br>to the latest iOS</span></p></body></html>",
                                        None))
        self.label_6.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" color:#f7f9fb;font-size:18pt; font-weight:600;\">Turn on iCloud Photo Library</span></p></body></html>",
                                        None))
        self.label_7.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">2. Set up iCloud on all of your devices.</span></p></body></html>",
                                        None))
        self.label_8.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:13pt; color:#f7f9fb;\">3. Make sure that you’re signed in to iCloud <br/>with the same </span><span style=\" font-size:13pt; font-style:italic; color:#f7f9fb;\">Apple ID </span><span style=\" font-size:13pt; color:#f7f9fb;\">on all of your devices <br/>that you want to use with </span><span style=\" font-size:13pt; font-style:italic; color:#f7f9fb;\">iCloud Photo<br/>Library</span><span style=\" font-size:13pt; color:#f7f9fb;\">.</span></p></body></html>",
                                        None))
        self.label_9.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">On your iPhone, iPad, or iPod touch with<br/></span><span style=\" font-size:13pt; font-weight:400; font-style:italic; color:#f7f9fb;\">iOS 10</span><span style=\" font-size:13pt; font-style:italic; color:#f7f9fb;\">.3 </span><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">or later, go to<br/></span></p></body></html>",
                                        None))
        self.label_10.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; text-decoration: underline; color:#f7f9fb;\">Settings &gt; [your name] &gt; iCloud &gt; Photos</span><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\"><br/>then turn on </span><span style=\" font-size:13pt; font-weight:400; font-style:italic; color:#f7f9fb;\">iCloud Photo Library.</span></p></body></html>",
                                         None))
        self.label_11.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">In </span><span style=\" font-size:13pt; font-weight:400; font-style:italic; color:#f7f9fb;\">iOS 10.2</span><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\"> or earlier, go to <br/></span><span style=\" font-size:13pt; font-weight:400; text-decoration: underline; color:#f7f9fb;\">Settings &gt; iCloud &gt; Photos</span><span style=\" font-size:13pt; font-weight:400; color:#f7f9fb;\">.</span></p></body></html>",
                                         None))
        self.label_12.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:14pt; color:#f7f9fb;\">For more info go to</span></p></body></html>",
                                         None))
        self.label_13.setText(_translate("Dialog",
                                         "<html><head/><body><p><a href=\"https://support.apple.com/en-in/HT204264\"><span style=\" font-size:15pt; font-style:italic; text-decoration: underline; color:#dcdcdc;\">iCloud Photo Library</span></a></p></body></html>",
                                         None))
        self.label_14.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-size:13pt; color:#f7f9fb;\">4. Make sure that you have a stable Internet<br> Connection on your system and on your<br> device too(to use some features of<b> PyCloud<b>)</span></p></body></html>",
                                         None))


import PyCloudResource

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
