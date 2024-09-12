# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(932, 806)
        self.verticalLayout_9 = QVBoxLayout(Form)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:red;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:red;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.line_choose_file = QLineEdit(self.groupBox)
        self.line_choose_file.setObjectName(u"line_choose_file")
        self.line_choose_file.setStyleSheet(u"background-color:pink;")

        self.horizontalLayout_3.addWidget(self.line_choose_file)

        self.btn_choose_file_txt = QPushButton(self.groupBox)
        self.btn_choose_file_txt.setObjectName(u"btn_choose_file_txt")
        self.btn_choose_file_txt.setStyleSheet(u"color:blue")

        self.horizontalLayout_3.addWidget(self.btn_choose_file_txt)

        self.btn_choose_file_excel = QPushButton(self.groupBox)
        self.btn_choose_file_excel.setObjectName(u"btn_choose_file_excel")
        self.btn_choose_file_excel.setStyleSheet(u"color:green;")

        self.horizontalLayout_3.addWidget(self.btn_choose_file_excel)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:red;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.box_threat_level = QCheckBox(self.groupBox)
        self.box_threat_level.setObjectName(u"box_threat_level")
        self.box_threat_level.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_threat_level)

        self.box_malware_type = QCheckBox(self.groupBox)
        self.box_malware_type.setObjectName(u"box_malware_type")
        self.box_malware_type.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_malware_type)

        self.box_malware_family = QCheckBox(self.groupBox)
        self.box_malware_family.setObjectName(u"box_malware_family")
        self.box_malware_family.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_malware_family)

        self.box_file_name = QCheckBox(self.groupBox)
        self.box_file_name.setObjectName(u"box_file_name")
        self.box_file_name.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_file_name)

        self.box_file_type = QCheckBox(self.groupBox)
        self.box_file_type.setObjectName(u"box_file_type")
        self.box_file_type.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_file_type)

        self.box_tag = QCheckBox(self.groupBox)
        self.box_tag.setObjectName(u"box_tag")
        self.box_tag.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_tag)

        self.box_threat_score = QCheckBox(self.groupBox)
        self.box_threat_score.setObjectName(u"box_threat_score")
        self.box_threat_score.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_threat_score)

        self.box_multi_engines = QCheckBox(self.groupBox)
        self.box_multi_engines.setObjectName(u"box_multi_engines")
        self.box_multi_engines.setStyleSheet(u"color:blue;")

        self.horizontalLayout_2.addWidget(self.box_multi_engines)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.table = QTableWidget(self.groupBox_2)
        self.table.setObjectName(u"table")

        self.verticalLayout_5.addWidget(self.table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)

        self.lcd_key_count = QLCDNumber(self.groupBox_2)
        self.lcd_key_count.setObjectName(u"lcd_key_count")
        self.lcd_key_count.setFont(font1)
        self.lcd_key_count.setAutoFillBackground(False)
        self.lcd_key_count.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lcd_key_count.setProperty("value", 3.000000000000000)

        self.horizontalLayout.addWidget(self.lcd_key_count)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout.addWidget(self.label_6)

        self.lcd_key_id = QLCDNumber(self.groupBox_2)
        self.lcd_key_id.setObjectName(u"lcd_key_id")
        self.lcd_key_id.setStyleSheet(u"color:red;")
        self.lcd_key_id.setSmallDecimalPoint(False)
        self.lcd_key_id.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.lcd_key_id.setProperty("value", 4.000000000000000)

        self.horizontalLayout.addWidget(self.lcd_key_id)

        self.label_ = QLabel(self.groupBox_2)
        self.label_.setObjectName(u"label_")
        self.label_.setFont(font1)

        self.horizontalLayout.addWidget(self.label_)

        self.lcd_md5_id = QLCDNumber(self.groupBox_2)
        self.lcd_md5_id.setObjectName(u"lcd_md5_id")

        self.horizontalLayout.addWidget(self.lcd_md5_id)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout.addWidget(self.label_10)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setUnderline(False)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: red;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(7, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.label_callback = QLineEdit(self.groupBox_2)
        self.label_callback.setObjectName(u"label_callback")
        self.label_callback.setFont(font2)
        self.label_callback.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.label_callback.setStyleSheet(u" background: pink;  \n"
" color:red;")
        self.label_callback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_callback)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"color:blue;\n"
"background-color:pink;")
        self.progressBar.setValue(0)

        self.verticalLayout_7.addWidget(self.progressBar)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_start = QPushButton(self.groupBox_4)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setStyleSheet(u"color:blue;")

        self.horizontalLayout_4.addWidget(self.btn_start)

        self.btn_callback_file = QPushButton(self.groupBox_4)
        self.btn_callback_file.setObjectName(u"btn_callback_file")
        self.btn_callback_file.setStyleSheet(u"color:blue;")

        self.horizontalLayout_4.addWidget(self.btn_callback_file)

        self.btn_ret = QPushButton(self.groupBox_4)
        self.btn_ret.setObjectName(u"btn_ret")
        self.btn_ret.setStyleSheet(u"color:blue;")

        self.horizontalLayout_4.addWidget(self.btn_ret)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)


        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.label.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.groupBox_4.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"微步工具", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5fae\u6b65API\u8c03\u7528GUI\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\uff1a", None))
        self.btn_choose_file_txt.setText(QCoreApplication.translate("Form", u"\u9009\u62e9txt\u6587\u4ef6", None))
        self.btn_choose_file_excel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9excel\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u5185\u5bb9\uff1a", None))
        self.box_threat_level.setText(QCoreApplication.translate("Form", u"\u5a01\u80c1\u7b49\u7ea7", None))
        self.box_malware_type.setText(QCoreApplication.translate("Form", u"\u5a01\u80c1\u5206\u7c7b", None))
        self.box_malware_family.setText(QCoreApplication.translate("Form", u"\u75c5\u6bd2\u5bb6\u65cf", None))
        self.box_file_name.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\u79f0", None))
        self.box_file_type.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7c7b\u578b", None))
        self.box_tag.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e", None))
        self.box_threat_score.setText(QCoreApplication.translate("Form", u"\u5a01\u80c1\u8bc4\u5206\u503c", None))
        self.box_multi_engines.setText(QCoreApplication.translate("Form", u"\u68c0\u51fa\u7387", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u5185\u5bb9\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"key\u603b\u6570\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5f53\u524dkey_id\uff1a", None))
        self.label_.setText(QCoreApplication.translate("Form", u"\u5f53\u524dmd5_id\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u65e5\u5fd7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u2193\u2193\u2193\u2193\u2193\u2193\u2193\u2193", None))
        self.label_callback.setText(QCoreApplication.translate("Form", u"\u8bf7\u5148\u5bfc\u5165\u6570\u636e\uff0c\u7136\u540e\u518d\u5f00\u59cb\u8fd0\u884c\u7a0b\u5e8f\uff0c\u7a0b\u5e8f\u8fd0\u884c\u7ed3\u675f\u4e4b\u540e\u53ef\u4ee5\u5bfc\u51fa\u6570\u636e\u751f\u6210excel\u6587\u4ef6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u8fdb\u5ea6\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u83dc\u5355", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.btn_callback_file.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8868\u683c", None))
        self.btn_ret.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u7a0b\u5e8f", None))
    # retranslateUi

