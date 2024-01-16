# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'k_sez_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(109, 52)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 111, 53))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.k_sez = QLabel(self.widget)
        self.k_sez.setObjectName(u"k_sez")

        self.horizontalLayout.addWidget(self.k_sez)

        self.k_sez_edit = QLineEdit(self.widget)
        self.k_sez_edit.setObjectName(u"k_sez_edit")

        self.horizontalLayout.addWidget(self.k_sez_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.okey_button = QPushButton(self.widget)
        self.okey_button.setObjectName(u"okey_button")

        self.verticalLayout.addWidget(self.okey_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.k_sez.setText(QCoreApplication.translate("Form", u"\u041a\u0441\u0435\u0437 =", None))
        self.okey_button.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
    # retranslateUi

