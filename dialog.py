# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AFMNet(object):
    def setupUi(self, AFMNet):
        AFMNet.setObjectName("AFMNet")
        AFMNet.resize(727, 652)
        self.centralwidget = QtWidgets.QWidget(AFMNet)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(245, 30))
        self.splitter.setMaximumSize(QtCore.QSize(245, 30))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.uploadButton = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadButton.sizePolicy().hasHeightForWidth())
        self.uploadButton.setSizePolicy(sizePolicy)
        self.uploadButton.setMinimumSize(QtCore.QSize(120, 30))
        self.uploadButton.setMaximumSize(QtCore.QSize(120, 30))
        self.uploadButton.setObjectName("uploadButton")
        self.predictButton = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictButton.sizePolicy().hasHeightForWidth())
        self.predictButton.setSizePolicy(sizePolicy)
        self.predictButton.setMinimumSize(QtCore.QSize(120, 30))
        self.predictButton.setMaximumSize(QtCore.QSize(120, 30))
        self.predictButton.setObjectName("predictButton")
        self.gridLayout.addWidget(self.splitter, 2, 3, 1, 2)
        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textlabel.sizePolicy().hasHeightForWidth())
        self.textlabel.setSizePolicy(sizePolicy)
        self.textlabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textlabel.setFont(font)
        self.textlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel.setObjectName("textlabel")
        self.gridLayout.addWidget(self.textlabel, 1, 0, 1, 5)
        self.image = ImageLabel(self.centralwidget)
        self.image.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setTextFormat(QtCore.Qt.RichText)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(120, 30))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.modelButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelButton.sizePolicy().hasHeightForWidth())
        self.modelButton.setSizePolicy(sizePolicy)
        self.modelButton.setMinimumSize(QtCore.QSize(120, 20))
        self.modelButton.setMaximumSize(QtCore.QSize(120, 30))
        self.modelButton.setObjectName("modelButton")
        self.gridLayout.addWidget(self.modelButton, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(245, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setRowStretch(0, 20)
        AFMNet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AFMNet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        AFMNet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AFMNet)
        self.statusbar.setObjectName("statusbar")
        AFMNet.setStatusBar(self.statusbar)

        self.retranslateUi(AFMNet)
        QtCore.QMetaObject.connectSlotsByName(AFMNet)

    def retranslateUi(self, AFMNet):
        _translate = QtCore.QCoreApplication.translate
        AFMNet.setWindowTitle(_translate("AFMNet", "AFMNet"))
        self.uploadButton.setText(_translate("AFMNet", "Upload Image"))
        self.predictButton.setText(_translate("AFMNet", "Predict Image"))
        self.textlabel.setText(_translate("AFMNet", "Select a network architecture and load a pretrained model"))
        self.image.setText(_translate("AFMNet", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">No image uploaded</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("AFMNet", "Select Net..."))
        self.modelButton.setText(_translate("AFMNet", "Load a:"))

from application import ImageLabel

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AFMNet = QtWidgets.QMainWindow()
    ui = Ui_AFMNet()
    ui.setupUi(AFMNet)
    AFMNet.show()
    sys.exit(app.exec_())

