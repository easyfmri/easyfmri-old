# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMAGMDeepRSAGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMAGMDeepRSA(object):
    def setupUi(self, frmMAGMDeepRSA):
        frmMAGMDeepRSA.setObjectName("frmMAGMDeepRSA")
        frmMAGMDeepRSA.resize(857, 651)
        self.btnInFile = QtWidgets.QPushButton(frmMAGMDeepRSA)
        self.btnInFile.setGeometry(QtCore.QRect(790, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMAGMDeepRSA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.txtInFile = QtWidgets.QLineEdit(frmMAGMDeepRSA)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 601, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMAGMDeepRSA)
        self.btnConvert.setGeometry(QtCore.QRect(690, 600, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmMAGMDeepRSA)
        self.btnClose.setGeometry(QtCore.QRect(30, 600, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMAGMDeepRSA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 130, 801, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.label_3.setObjectName("label_3")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(180, 90, 181, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(180, 50, 181, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(180, 170, 181, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 111, 16))
        self.label_6.setObjectName("label_6")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(180, 210, 181, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 60, 16))
        self.label_7.setObjectName("label_7")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(180, 250, 181, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(260, 10, 51, 17))
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 290, 131, 16))
        self.label_9.setObjectName("label_9")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(180, 290, 181, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtDesign = QtWidgets.QComboBox(self.tab)
        self.txtDesign.setGeometry(QtCore.QRect(180, 130, 181, 26))
        self.txtDesign.setEditable(True)
        self.txtDesign.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDesign.setObjectName("txtDesign")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 30, 451, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFSubject = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFSubject.setGeometry(QtCore.QRect(10, 30, 130, 20))
        self.cbFSubject.setChecked(True)
        self.cbFSubject.setObjectName("cbFSubject")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.rbFRun = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbFRun.setGeometry(QtCore.QRect(220, 60, 221, 20))
        self.rbFRun.setObjectName("rbFRun")
        self.cbFTask = QtWidgets.QCheckBox(self.tab_3)
        self.cbFTask.setGeometry(QtCore.QRect(510, 60, 161, 20))
        self.cbFTask.setObjectName("cbFTask")
        self.cbFCounter = QtWidgets.QCheckBox(self.tab_3)
        self.cbFCounter.setGeometry(QtCore.QRect(510, 100, 161, 20))
        self.cbFCounter.setObjectName("cbFCounter")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(40, 160, 121, 16))
        self.label_11.setObjectName("label_11")
        self.txtUnit = QtWidgets.QSpinBox(self.tab_3)
        self.txtUnit.setGeometry(QtCore.QRect(160, 160, 181, 24))
        self.txtUnit.setMinimum(1)
        self.txtUnit.setMaximum(1000000000)
        self.txtUnit.setObjectName("txtUnit")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 761, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.rbScale = QtWidgets.QRadioButton(self.groupBox)
        self.rbScale.setGeometry(QtCore.QRect(190, 40, 161, 20))
        self.rbScale.setChecked(True)
        self.rbScale.setObjectName("rbScale")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 40, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 761, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rbAvg = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbAvg.setGeometry(QtCore.QRect(20, 30, 116, 22))
        self.rbAvg.setChecked(True)
        self.rbAvg.setObjectName("rbAvg")
        self.rbMax = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbMax.setGeometry(QtCore.QRect(170, 30, 116, 22))
        self.rbMax.setObjectName("rbMax")
        self.rbMin = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbMin.setGeometry(QtCore.QRect(330, 30, 116, 22))
        self.rbMin.setObjectName("rbMin")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(400, 220, 371, 16))
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(400, 340, 201, 16))
        self.label_19.setObjectName("label_19")
        self.txtLayers = QtWidgets.QLineEdit(self.tab_2)
        self.txtLayers.setGeometry(QtCore.QRect(220, 220, 160, 21))
        self.txtLayers.setObjectName("txtLayers")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 300, 201, 16))
        self.label_16.setObjectName("label_16")
        self.cbActivation = QtWidgets.QComboBox(self.tab_2)
        self.cbActivation.setGeometry(QtCore.QRect(220, 260, 161, 26))
        self.cbActivation.setObjectName("cbActivation")
        self.cbVerbose = QtWidgets.QCheckBox(self.tab_2)
        self.cbVerbose.setGeometry(QtCore.QRect(20, 380, 371, 20))
        self.cbVerbose.setChecked(True)
        self.cbVerbose.setObjectName("cbVerbose")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(20, 340, 201, 16))
        self.label_17.setObjectName("label_17")
        self.txtBatch = QtWidgets.QLineEdit(self.tab_2)
        self.txtBatch.setGeometry(QtCore.QRect(220, 340, 160, 21))
        self.txtBatch.setObjectName("txtBatch")
        self.cbLossNorm = QtWidgets.QComboBox(self.tab_2)
        self.cbLossNorm.setGeometry(QtCore.QRect(600, 260, 161, 26))
        self.cbLossNorm.setObjectName("cbLossNorm")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(400, 260, 201, 16))
        self.label_15.setObjectName("label_15")
        self.txtReportStep = QtWidgets.QLineEdit(self.tab_2)
        self.txtReportStep.setGeometry(QtCore.QRect(600, 300, 160, 21))
        self.txtReportStep.setObjectName("txtReportStep")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 260, 201, 16))
        self.label_14.setObjectName("label_14")
        self.txtRate = QtWidgets.QLineEdit(self.tab_2)
        self.txtRate.setGeometry(QtCore.QRect(600, 340, 160, 21))
        self.txtRate.setObjectName("txtRate")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(400, 300, 201, 16))
        self.label_18.setObjectName("label_18")
        self.txtIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtIter.setGeometry(QtCore.QRect(220, 300, 160, 21))
        self.txtIter.setObjectName("txtIter")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 220, 201, 16))
        self.label_13.setObjectName("label_13")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(400, 380, 201, 16))
        self.label_21.setObjectName("label_21")
        self.txtAlpha = QtWidgets.QLineEdit(self.tab_2)
        self.txtAlpha.setGeometry(QtCore.QRect(600, 380, 160, 21))
        self.txtAlpha.setObjectName("txtAlpha")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_4)
        self.txtFilter.setGeometry(QtCore.QRect(190, 30, 291, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 211, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.tab_4)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 91, 331))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbCov = QtWidgets.QCheckBox(self.tab_5)
        self.cbCov.setGeometry(QtCore.QRect(20, 30, 391, 20))
        self.cbCov.setChecked(True)
        self.cbCov.setObjectName("cbCov")
        self.cbCorr = QtWidgets.QCheckBox(self.tab_5)
        self.cbCorr.setGeometry(QtCore.QRect(20, 70, 391, 20))
        self.cbCorr.setChecked(True)
        self.cbCorr.setObjectName("cbCorr")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_35 = QtWidgets.QLabel(frmMAGMDeepRSA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMAGMDeepRSA)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 60, 601, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnOutFile = QtWidgets.QPushButton(frmMAGMDeepRSA)
        self.btnOutFile.setGeometry(QtCore.QRect(790, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.cbDiagram = QtWidgets.QCheckBox(frmMAGMDeepRSA)
        self.cbDiagram.setGeometry(QtCore.QRect(30, 90, 341, 22))
        self.cbDiagram.setChecked(True)
        self.cbDiagram.setObjectName("cbDiagram")
        self.cbBeta = QtWidgets.QCheckBox(frmMAGMDeepRSA)
        self.cbBeta.setGeometry(QtCore.QRect(180, 90, 341, 22))
        self.cbBeta.setChecked(True)
        self.cbBeta.setObjectName("cbBeta")
        self.btnRedraw = QtWidgets.QPushButton(frmMAGMDeepRSA)
        self.btnRedraw.setGeometry(QtCore.QRect(530, 600, 141, 32))
        self.btnRedraw.setObjectName("btnRedraw")
        self.label_22 = QtWidgets.QLabel(frmMAGMDeepRSA)
        self.label_22.setGeometry(QtCore.QRect(500, 90, 81, 16))
        self.label_22.setObjectName("label_22")
        self.cbDevice = QtWidgets.QComboBox(frmMAGMDeepRSA)
        self.cbDevice.setGeometry(QtCore.QRect(580, 90, 201, 26))
        self.cbDevice.setObjectName("cbDevice")

        self.retranslateUi(frmMAGMDeepRSA)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(frmMAGMDeepRSA)
        frmMAGMDeepRSA.setTabOrder(self.txtInFile, self.btnInFile)
        frmMAGMDeepRSA.setTabOrder(self.btnInFile, self.tabWidget)
        frmMAGMDeepRSA.setTabOrder(self.tabWidget, self.txtData)
        frmMAGMDeepRSA.setTabOrder(self.txtData, self.txtLabel)
        frmMAGMDeepRSA.setTabOrder(self.txtLabel, self.btnConvert)
        frmMAGMDeepRSA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMAGMDeepRSA):
        _translate = QtCore.QCoreApplication.translate
        frmMAGMDeepRSA.setWindowTitle(_translate("frmMAGMDeepRSA", "RAS"))
        self.btnInFile.setText(_translate("frmMAGMDeepRSA", "..."))
        self.label_33.setText(_translate("frmMAGMDeepRSA", "Input Data "))
        self.btnConvert.setText(_translate("frmMAGMDeepRSA", "Analyze"))
        self.btnClose.setText(_translate("frmMAGMDeepRSA", "Close"))
        self.label_2.setText(_translate("frmMAGMDeepRSA", "Data"))
        self.label_3.setText(_translate("frmMAGMDeepRSA", "Label"))
        self.label_6.setText(_translate("frmMAGMDeepRSA", "Subject"))
        self.label_7.setText(_translate("frmMAGMDeepRSA", "Run"))
        self.label_8.setText(_translate("frmMAGMDeepRSA", "Counter"))
        self.label.setText(_translate("frmMAGMDeepRSA", "ID"))
        self.label_9.setText(_translate("frmMAGMDeepRSA", "Task"))
        self.label_12.setText(_translate("frmMAGMDeepRSA", "Design"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMAGMDeepRSA", "Data"))
        self.groupBox_3.setTitle(_translate("frmMAGMDeepRSA", "<Subject Level>"))
        self.cbFSubject.setText(_translate("frmMAGMDeepRSA", "Subject"))
        self.radioButton.setText(_translate("frmMAGMDeepRSA", "Without Run"))
        self.rbFRun.setText(_translate("frmMAGMDeepRSA", "With Run"))
        self.cbFTask.setText(_translate("frmMAGMDeepRSA", "Task"))
        self.cbFCounter.setText(_translate("frmMAGMDeepRSA", "Counter"))
        self.label_11.setText(_translate("frmMAGMDeepRSA", "Unit number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMAGMDeepRSA", "Level"))
        self.groupBox.setTitle(_translate("frmMAGMDeepRSA", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMAGMDeepRSA", "Scale Data~N(0,1)"))
        self.rbScale.setText(_translate("frmMAGMDeepRSA", "Session Level"))
        self.radioButton_2.setText(_translate("frmMAGMDeepRSA", "Whole Data"))
        self.groupBox_2.setTitle(_translate("frmMAGMDeepRSA", "<Integration Metric>"))
        self.rbAvg.setText(_translate("frmMAGMDeepRSA", "Average"))
        self.rbMax.setText(_translate("frmMAGMDeepRSA", "Max"))
        self.rbMin.setText(_translate("frmMAGMDeepRSA", "Min"))
        self.label_20.setText(_translate("frmMAGMDeepRSA", "[Hidden Layer 1, HL2, HL3, ..., Out Layer]"))
        self.label_19.setText(_translate("frmMAGMDeepRSA", "Learning Rate"))
        self.txtLayers.setText(_translate("frmMAGMDeepRSA", "[1000, 700, 500]"))
        self.label_16.setText(_translate("frmMAGMDeepRSA", "Iteration"))
        self.cbVerbose.setText(_translate("frmMAGMDeepRSA", "Show Report"))
        self.label_17.setText(_translate("frmMAGMDeepRSA", "Batch Size"))
        self.txtBatch.setText(_translate("frmMAGMDeepRSA", "50"))
        self.label_15.setText(_translate("frmMAGMDeepRSA", "Loss Metric"))
        self.txtReportStep.setText(_translate("frmMAGMDeepRSA", "300"))
        self.label_14.setText(_translate("frmMAGMDeepRSA", "Activation"))
        self.txtRate.setText(_translate("frmMAGMDeepRSA", "0.001"))
        self.label_18.setText(_translate("frmMAGMDeepRSA", "Report Step every"))
        self.txtIter.setText(_translate("frmMAGMDeepRSA", "1000"))
        self.label_13.setText(_translate("frmMAGMDeepRSA", "Layers"))
        self.label_21.setText(_translate("frmMAGMDeepRSA", "Alpha > 0"))
        self.txtAlpha.setText(_translate("frmMAGMDeepRSA", "10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMAGMDeepRSA", "Parameters"))
        self.label_4.setText(_translate("frmMAGMDeepRSA", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMAGMDeepRSA", "0"))
        self.label_5.setText(_translate("frmMAGMDeepRSA", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMAGMDeepRSA", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMAGMDeepRSA", "Filter Class ID"))
        self.cbCov.setText(_translate("frmMAGMDeepRSA", "Covariance"))
        self.cbCorr.setText(_translate("frmMAGMDeepRSA", "Correlation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMAGMDeepRSA", "Metrics"))
        self.label_35.setText(_translate("frmMAGMDeepRSA", "Output Data"))
        self.btnOutFile.setText(_translate("frmMAGMDeepRSA", "..."))
        self.cbDiagram.setText(_translate("frmMAGMDeepRSA", "Show Diagrams"))
        self.cbBeta.setText(_translate("frmMAGMDeepRSA", "Save Beta, and Network Parameters"))
        self.btnRedraw.setText(_translate("frmMAGMDeepRSA", "Redraw"))
        self.label_22.setText(_translate("frmMAGMDeepRSA", "Device"))

