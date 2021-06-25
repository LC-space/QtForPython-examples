
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

# PySide6 tutorial 5


import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QLCDNumber, QPushButton,
                               QSlider, QVBoxLayout, QWidget)


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建退出按钮
        quit = QPushButton("Quit")
        quit.setFont(QFont("Times", 18, QFont.Bold))

        # 创建两位数数码管
        lcd = QLCDNumber(2)

        # 创建水平滑块，范围0~99，初始值为0
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)

        # 按钮发出信号后退出、滑块发出信号后数码管显示
        quit.clicked.connect(qApp.quit)
        slider.valueChanged.connect(lcd.display)

        # 设置纵向布局，依次放入按钮、数码管、滑块
        layout = QVBoxLayout(self)
        layout.addWidget(quit)
        layout.addWidget(lcd)
        layout.addWidget(slider)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
