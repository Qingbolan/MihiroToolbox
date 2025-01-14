# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Jason Shen\Documents\MihiroToolbox\UI\QtDesigner\audio.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Audio(object):
    def setupUi(self, Audio):
        Audio.setObjectName("Audio")
        Audio.resize(748, 808)
        self.gridLayout_6 = QtWidgets.QGridLayout(Audio)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.AudioBox = QtWidgets.QGridLayout()
        self.AudioBox.setContentsMargins(26, 45, 26, 26)
        self.AudioBox.setSpacing(16)
        self.AudioBox.setObjectName("AudioBox")
        self.AudioTitile = LargeTitleLabel(Audio)
        self.AudioTitile.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.AudioTitile.setFont(font)
        self.AudioTitile.setObjectName("AudioTitile")
        self.AudioBox.addWidget(self.AudioTitile, 0, 0, 1, 1)
        self.InnerAudioBox = QtWidgets.QVBoxLayout()
        self.InnerAudioBox.setObjectName("InnerAudioBox")
        self.FileTitle = SubtitleLabel(Audio)
        self.FileTitle.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.FileTitle.setFont(font)
        self.FileTitle.setObjectName("FileTitle")
        self.InnerAudioBox.addWidget(self.FileTitle)
        self.FileBox = SimpleCardWidget(Audio)
        self.FileBox.setObjectName("FileBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.FileBox)
        self.gridLayout_4.setContentsMargins(16, 16, 16, 16)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.OutputBox = QtWidgets.QGridLayout()
        self.OutputBox.setObjectName("OutputBox")
        self.OutputLabel = BodyLabel(self.FileBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setObjectName("OutputLabel")
        self.OutputBox.addWidget(self.OutputLabel, 0, 0, 1, 1)
        self.OutputLine = LineEdit(self.FileBox)
        self.OutputLine.setEnabled(True)
        self.OutputLine.setObjectName("OutputLine")
        self.OutputBox.addWidget(self.OutputLine, 1, 0, 1, 1)
        self.Outputbutton = PushButton(self.FileBox)
        self.Outputbutton.setObjectName("Outputbutton")
        self.OutputBox.addWidget(self.Outputbutton, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.OutputBox, 1, 0, 1, 1)
        self.InputBox = QtWidgets.QGridLayout()
        self.InputBox.setObjectName("InputBox")
        self.inputLabel = BodyLabel(self.FileBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.inputLabel.setFont(font)
        self.inputLabel.setObjectName("inputLabel")
        self.InputBox.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.InputLine = LineEdit(self.FileBox)
        self.InputLine.setEnabled(True)
        self.InputLine.setObjectName("InputLine")
        self.InputBox.addWidget(self.InputLine, 1, 0, 1, 1)
        self.InputButton = PushButton(self.FileBox)
        self.InputButton.setObjectName("InputButton")
        self.InputBox.addWidget(self.InputButton, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.InputBox, 0, 0, 1, 1)
        self.InnerAudioBox.addWidget(self.FileBox)
        self.AudioBox.addLayout(self.InnerAudioBox, 1, 0, 1, 1)
        self.ProcessBox = QtWidgets.QVBoxLayout()
        self.ProcessBox.setObjectName("ProcessBox")
        self.ProcessTitle = SubtitleLabel(Audio)
        self.ProcessTitle.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessTitle.setFont(font)
        self.ProcessTitle.setObjectName("ProcessTitle")
        self.ProcessBox.addWidget(self.ProcessTitle)
        self.OptionBox = SimpleCardWidget(Audio)
        self.OptionBox.setObjectName("OptionBox")
        self.gridLayout = QtWidgets.QGridLayout(self.OptionBox)
        self.gridLayout.setObjectName("gridLayout")
        self.EncoderLabel = BodyLabel(self.OptionBox)
        self.EncoderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EncoderLabel.setObjectName("EncoderLabel")
        self.gridLayout.addWidget(self.EncoderLabel, 0, 0, 1, 1)
        self.EncoderChioce = ComboBox(self.OptionBox)
        self.EncoderChioce.setMinimumSize(QtCore.QSize(200, 33))
        self.EncoderChioce.setText("")
        self.EncoderChioce.setObjectName("EncoderChioce")
        self.gridLayout.addWidget(self.EncoderChioce, 0, 1, 1, 1)
        self.BitrateLabel = BodyLabel(self.OptionBox)
        self.BitrateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BitrateLabel.setObjectName("BitrateLabel")
        self.gridLayout.addWidget(self.BitrateLabel, 1, 0, 1, 1)
        self.BitrateNum = CompactSpinBox(self.OptionBox)
        self.BitrateNum.setMinimumSize(QtCore.QSize(200, 33))
        self.BitrateNum.setMaximum(999999)
        self.BitrateNum.setObjectName("BitrateNum")
        self.gridLayout.addWidget(self.BitrateNum, 1, 1, 1, 1)
        self.ProcessButton = PrimaryPushButton(self.OptionBox)
        self.ProcessButton.setObjectName("ProcessButton")
        self.gridLayout.addWidget(self.ProcessButton, 2, 0, 1, 2)
        self.ProgressBar = IndeterminateProgressBar(self.OptionBox)
        self.ProgressBar.setObjectName("ProgressBar")
        self.gridLayout.addWidget(self.ProgressBar, 3, 0, 1, 2)
        self.ProcessBox.addWidget(self.OptionBox)
        self.AudioBox.addLayout(self.ProcessBox, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.AudioBox, 0, 0, 1, 1)

        self.retranslateUi(Audio)
        QtCore.QMetaObject.connectSlotsByName(Audio)

    def retranslateUi(self, Audio):
        _translate = QtCore.QCoreApplication.translate
        Audio.setWindowTitle(_translate("Audio", "Form"))
        self.AudioTitile.setText(_translate("Audio", "音频"))
        self.FileTitle.setText(_translate("Audio", "文件"))
        self.OutputLabel.setText(_translate("Audio", "音频输出"))
        self.Outputbutton.setText(_translate("Audio", "浏览"))
        self.inputLabel.setText(_translate("Audio", "音频输入"))
        self.InputButton.setText(_translate("Audio", "浏览"))
        self.ProcessTitle.setText(_translate("Audio", "压制"))
        self.EncoderLabel.setText(_translate("Audio", "编码器"))
        self.BitrateLabel.setText(_translate("Audio", "码率(Kbps)"))
        self.BitrateNum.setToolTip(_translate("Audio", "<html><head/><body><p>只有ACC和MP3编码器支持自定义码率</p></body></html>"))
        self.ProcessButton.setText(_translate("Audio", "压制"))
from qfluentwidgets import BodyLabel, ComboBox, CompactSpinBox, IndeterminateProgressBar, LargeTitleLabel, LineEdit, PrimaryPushButton, PushButton, SimpleCardWidget, SubtitleLabel
