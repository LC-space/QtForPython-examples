
#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

# PySide6 tutorial 7


import sys

from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber,
                               QPushButton, QSlider, QVBoxLayout, QWidget)


class LCDRange(QWidget):

    # 定义值改变信号
    value_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建两位数码管
        lcd = QLCDNumber(2)

        # 创建滑块
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        # 滑动滑块发出信号，改变数码管显示、发出值改变信号
        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.value_changed)

        # 创建垂直布局，放入数码管、滑块
        layout = QVBoxLayout(self)
        layout.addWidget(lcd)
        layout.addWidget(self.slider)

    def value(self):
        """取滑块的值"""
        return self.slider.value()

    @Slot(int)
    def set_value(self, value):
        """设置滑块的值"""
        self.slider.setValue(value)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建退出按钮
        quit = QPushButton("Quit")
        quit.setFont(QFont("Times", 18, QFont.Bold))
        quit.clicked.connect(qApp.quit)

        # 创建一个空对象，用于存放已经存在的数码管＋滑块控件
        previous_range = None

        # 创建垂直布局，放入退出按钮、网格布局
        layout = QVBoxLayout(self)
        layout.addWidget(quit)
        grid = QGridLayout()
        layout.addLayout(grid)

        # 在网格布局中放入数码管＋滑块控件
        for row in range(3):
            for column in range(3):
                lcd_range = LCDRange()
                grid.addWidget(lcd_range, row, column)

                # 如果该控件之前有控件，则在改变该控件值的同时也改变之前控件的值
                if previous_range:
                    lcd_range.value_changed.connect(previous_range.set_value)

                # 将生成的数码管＋滑块控件加入已存在控件对象
                previous_range = lcd_range


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
