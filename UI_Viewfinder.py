# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Viewfinder_mod.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Viewfinder(object):
    def setupUi(self, Viewfinder):
        Viewfinder.setObjectName("Viewfinder")
        Viewfinder.resize(900, 674)
        Viewfinder.setMaximumSize(QtCore.QSize(900, 674))
        self.centralwidget = QtWidgets.QWidget(Viewfinder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 901, 661))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Preview = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Preview.setContentsMargins(0, 0, 0, 0)
        self.Preview.setObjectName("Preview")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 0, 111, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Button_row = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Button_row.setContentsMargins(0, 0, 0, 0)
        self.Button_row.setObjectName("Button_row")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Button_row.addItem(spacerItem)
        self.Capture_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Capture_button.setObjectName("Capture_button")
        self.Button_row.addWidget(self.Capture_button)
        self.exposure_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.exposure_label.setObjectName("exposure_label")
        self.Button_row.addWidget(self.exposure_label)
        self.exposure_choice = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.exposure_choice.setObjectName("exposure_choice")
        self.Button_row.addWidget(self.exposure_choice)
        self.ISO_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ISO_label.setObjectName("ISO_label")
        self.Button_row.addWidget(self.ISO_label)
        self.ISO_choice = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.ISO_choice.setObjectName("ISO_choice")
        self.Button_row.addWidget(self.ISO_choice)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Button_row.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.Button_row.addWidget(self.label)
        self.IR_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.IR_button.setObjectName("IR_button")
        self.Button_row.addWidget(self.IR_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Button_row.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.Button_row.addWidget(self.label_2)
        self.Zoom_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Zoom_button.setObjectName("Zoom_button")
        self.Button_row.addWidget(self.Zoom_button)
        self.ZoomLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ZoomLabel.setObjectName("ZoomLabel")
        self.Button_row.addWidget(self.ZoomLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Button_row.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Button_row.addItem(spacerItem3)
        self.Exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Exit.setObjectName("Exit")
        self.Button_row.addWidget(self.Exit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Button_row.addItem(spacerItem4)
        Viewfinder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Viewfinder)
        self.statusbar.setObjectName("statusbar")
        Viewfinder.setStatusBar(self.statusbar)

        self.retranslateUi(Viewfinder)
        QtCore.QMetaObject.connectSlotsByName(Viewfinder)

    def retranslateUi(self, Viewfinder):
        _translate = QtCore.QCoreApplication.translate
        Viewfinder.setWindowTitle(_translate("Viewfinder", "MainWindow"))
        self.Capture_button.setText(_translate("Viewfinder", "Capture"))
        self.exposure_label.setText(_translate("Viewfinder", "Exposure (e-6s)"))
        self.ISO_label.setText(_translate("Viewfinder", "ISO"))
        self.label.setText(_translate("Viewfinder", "IR"))
        self.IR_button.setText(_translate("Viewfinder", "IR"))
        self.label_2.setText(_translate("Viewfinder", "Zoom"))
        self.Zoom_button.setText(_translate("Viewfinder", "Zoom"))
        self.ZoomLabel.setText(_translate("Viewfinder", "TextLabel"))
        self.Exit.setText(_translate("Viewfinder", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Viewfinder = QtWidgets.QMainWindow()
    ui = Ui_Viewfinder()
    ui.setupUi(Viewfinder)
    Viewfinder.show()
    sys.exit(app.exec_())
