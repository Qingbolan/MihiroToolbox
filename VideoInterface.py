# coding:utf-8

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QFileDialog
from functools import partial
import os

from UI.Ui_video import Ui_Video


class VideoInterface(QWidget, Ui_Video):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 编码选项
        self.EncoderType.addItem('x264')
        self.EncoderType.addItem('x265')

        self.DepthChoice.addItem('8bit')
        self.DepthChoice.addItem('10bit')

        # 文件选项
        self.InputButton.clicked.connect(
            partial(self.FileSelect, self.InputLine, self.OutputLine))
        self.Outputbutton.clicked.connect(
            partial(self.FileSelect, self.OutputLine, 0))
        self.Outputbutton_2.clicked.connect(
            partial(self.FileSelect, self.TextLine, 0))
        
        # 分辨率选项
        self.WidthNum.setDisabled(1)
        self.HeightNum.setDisabled(1)
        self.IfEnableSwitch.checkedChanged.connect(self.ResolutionChange)
        
    # 文件选择函数
    def FileSelect(self, TargetLine, AutoFill):
        dir = QFileDialog()
        dir.setDirectory(os.getcwd())
        if dir.exec_():      # 判断是否选择了文件
            FilePath = dir.selectedFiles()
            TargetLine.setText(FilePath[0])

            if AutoFill != 0:
                FileExt = os.path.splitext(FilePath[0])[1]
                FilePath = os.path.splitext(FilePath[0])[0]
                NewFilePath = FilePath + '_output' + FileExt
                AutoFill.setText(NewFilePath)
    
    # 自定义分辨率控制            
    def ResolutionChange(self):
        if (self.IfEnableSwitch.checked):
            self.WidthNum.setDisabled(0)
            self.HeightNum.setDisabled(0)
        else:
            self.WidthNum.setDisabled(1)
            self.HeightNum.setDisabled(1)
