# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkbox_IR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_IR.setObjectName("checkbox_IR")
        self.gridLayout_3.addWidget(self.checkbox_IR, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gain_label = QtWidgets.QLabel(self.centralwidget)
        self.gain_label.setObjectName("gain_label")
        self.horizontalLayout_4.addWidget(self.gain_label)
        self.combobox_gain = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_gain.setObjectName("combobox_gain")
        self.horizontalLayout_4.addWidget(self.combobox_gain)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.step_label = QtWidgets.QLabel(self.centralwidget)
        self.step_label.setObjectName("step_label")
        self.horizontalLayout_5.addWidget(self.step_label)
        self.combobox_step = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_step.setObjectName("combobox_step")
        self.horizontalLayout_5.addWidget(self.combobox_step)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.checkbox_x = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_x.setObjectName("checkbox_x")
        self.gridLayout_3.addWidget(self.checkbox_x, 0, 0, 1, 1)
        self.checkbox_y = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_y.setObjectName("checkbox_y")
        self.gridLayout_3.addWidget(self.checkbox_y, 1, 0, 1, 1)
        self.checkbox_z = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_z.setObjectName("checkbox_z")
        self.gridLayout_3.addWidget(self.checkbox_z, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exp_label = QtWidgets.QLabel(self.centralwidget)
        self.exp_label.setObjectName("exp_label")
        self.horizontalLayout_3.addWidget(self.exp_label)
        self.combobox_exp = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_exp.setObjectName("combobox_exp")
        self.horizontalLayout_3.addWidget(self.combobox_exp)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.checkbox_HDR = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_HDR.setObjectName("checkbox_HDR")
        self.gridLayout_3.addWidget(self.checkbox_HDR, 4, 0, 1, 1)
        self.checkbox_IR_an_normal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_IR_an_normal.setObjectName("checkbox_IR_an_normal")
        self.gridLayout_3.addWidget(self.checkbox_IR_an_normal, 3, 1, 1, 1)
        self.pushbutton_find_endstops = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_find_endstops.setObjectName("pushbutton_find_endstops")
        self.gridLayout_3.addWidget(self.pushbutton_find_endstops, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_dslr = QtWidgets.QPushButton(self.centralwidget)
        self.button_dslr.setObjectName("button_dslr")
        self.horizontalLayout.addWidget(self.button_dslr)
        self.button_auto = QtWidgets.QPushButton(self.centralwidget)
        self.button_auto.setObjectName("button_auto")
        self.horizontalLayout.addWidget(self.button_auto)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushbutton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_exit.setObjectName("pushbutton_exit")
        self.gridLayout_2.addWidget(self.pushbutton_exit, 4, 0, 1, 1)
        self.activate_gamepad = QtWidgets.QPushButton(self.centralwidget)
        self.activate_gamepad.setObjectName("activate_gamepad")
        self.gridLayout_2.addWidget(self.activate_gamepad, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Auto Imaging Parameters"))
        self.checkbox_IR.setText(_translate("MainWindow", "IR"))
        self.gain_label.setText(_translate("MainWindow", "Analogue Gain"))
        self.step_label.setText(_translate("MainWindow", "Step Size"))
        self.checkbox_x.setText(_translate("MainWindow", "X-motor"))
        self.checkbox_y.setText(_translate("MainWindow", "Y-motor"))
        self.checkbox_z.setText(_translate("MainWindow", "Z-motor"))
        self.exp_label.setText(_translate("MainWindow", "Exposure"))
        self.checkbox_HDR.setText(_translate("MainWindow", "HDR"))
        self.checkbox_IR_an_normal.setText(_translate("MainWindow", "IR and normal"))
        self.pushbutton_find_endstops.setText(_translate("MainWindow", "Find Endstops"))
        self.button_dslr.setText(_translate("MainWindow", "Start Graphical"))
        self.button_auto.setText(_translate("MainWindow", "Start Automatic"))
        self.pushbutton_exit.setText(_translate("MainWindow", "Exit"))
        self.activate_gamepad.setText(_translate("MainWindow", "Activate Gamepad"))
