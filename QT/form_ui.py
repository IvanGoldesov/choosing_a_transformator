# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(435, 197)
        Widget.setCursor(QCursor(Qt.ArrowCursor))
        Widget.setMouseTracking(True)
        Widget.setTabletTracking(True)
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 150, 181, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.compute_button = QPushButton(self.layoutWidget)
        self.compute_button.setObjectName(u"compute_button")

        self.horizontalLayout.addWidget(self.compute_button)

        self.cancel_button = QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)

        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 385, 102))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.Uvn = QLineEdit(self.widget)
        self.Uvn.setObjectName(u"Uvn")

        self.horizontalLayout_2.addWidget(self.Uvn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.temperature_winter = QLineEdit(self.widget)
        self.temperature_winter.setObjectName(u"temperature_winter")

        self.horizontalLayout_3.addWidget(self.temperature_winter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.temperature_summer = QLineEdit(self.widget)
        self.temperature_summer.setObjectName(u"temperature_summer")

        self.horizontalLayout_7.addWidget(self.temperature_summer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GN_winter = QLabel(self.widget)
        self.GN_winter.setObjectName(u"GN_winter")

        self.verticalLayout.addWidget(self.GN_winter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Choise_hour_graphics = QComboBox(self.widget)
        self.Choise_hour_graphics.addItem("")
        self.Choise_hour_graphics.addItem("")
        self.Choise_hour_graphics.addItem("")
        self.Choise_hour_graphics.setObjectName(u"Choise_hour_graphics")
        self.Choise_hour_graphics.setEditable(False)
        self.Choise_hour_graphics.setMaxVisibleItems(10)
        self.Choise_hour_graphics.setInsertPolicy(QComboBox.InsertAtBottom)
        self.Choise_hour_graphics.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.Choise_hour_graphics.setDuplicatesEnabled(False)
        self.Choise_hour_graphics.setFrame(True)
        self.Choise_hour_graphics.setModelColumn(0)

        self.horizontalLayout_4.addWidget(self.Choise_hour_graphics)

        self.take_hour_GN_winter = QPushButton(self.widget)
        self.take_hour_GN_winter.setObjectName(u"take_hour_GN_winter")

        self.horizontalLayout_4.addWidget(self.take_hour_GN_winter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Text_GN_summer = QLabel(self.widget)
        self.Text_GN_summer.setObjectName(u"Text_GN_summer")

        self.verticalLayout_3.addWidget(self.Text_GN_summer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Choise_hour_graphics_summer = QComboBox(self.widget)
        self.Choise_hour_graphics_summer.addItem("")
        self.Choise_hour_graphics_summer.addItem("")
        self.Choise_hour_graphics_summer.addItem("")
        self.Choise_hour_graphics_summer.addItem("")
        self.Choise_hour_graphics_summer.setObjectName(u"Choise_hour_graphics_summer")
        self.Choise_hour_graphics_summer.setEditable(False)
        self.Choise_hour_graphics_summer.setMaxVisibleItems(10)
        self.Choise_hour_graphics_summer.setInsertPolicy(QComboBox.InsertAtBottom)
        self.Choise_hour_graphics_summer.setDuplicatesEnabled(False)
        self.Choise_hour_graphics_summer.setFrame(True)
        self.Choise_hour_graphics_summer.setModelColumn(0)

        self.horizontalLayout_5.addWidget(self.Choise_hour_graphics_summer)

        self.take_hour_GN_summer = QPushButton(self.widget)
        self.take_hour_GN_summer.setObjectName(u"take_hour_GN_summer")

        self.horizontalLayout_5.addWidget(self.take_hour_GN_summer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.retranslateUi(Widget)

        self.Choise_hour_graphics.setCurrentIndex(-1)
        self.Choise_hour_graphics_summer.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.compute_button.setText(QCoreApplication.translate("Widget", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("Widget", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Widget", u"U_\u0432\u043d, \u043a\u0412", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"T_\u0437\u0438\u043c\u0430, \u00b0\u0421", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"T_\u043b\u0435\u0442\u0430, \u00b0\u0421", None))
        self.GN_winter.setText(QCoreApplication.translate("Widget", u"\u0413\u0440\u0430\u0444\u0438\u043a \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0432 \u0437\u0438\u043c\u043d\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.Choise_hour_graphics.setItemText(0, QCoreApplication.translate("Widget", u"1 \u0447.", None))
        self.Choise_hour_graphics.setItemText(1, QCoreApplication.translate("Widget", u"2 \u0447.", None))
        self.Choise_hour_graphics.setItemText(2, QCoreApplication.translate("Widget", u"4 \u0447.", None))

        self.take_hour_GN_winter.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.Text_GN_summer.setText(QCoreApplication.translate("Widget", u"\u0413\u0440\u0430\u0444\u0438\u043a \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0432 \u043b\u0435\u0442\u043d\u0439 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.Choise_hour_graphics_summer.setItemText(0, QCoreApplication.translate("Widget", u"\u041a\u0441\u0435\u0437", None))
        self.Choise_hour_graphics_summer.setItemText(1, QCoreApplication.translate("Widget", u"1 \u0447.", None))
        self.Choise_hour_graphics_summer.setItemText(2, QCoreApplication.translate("Widget", u"2 \u0447.", None))
        self.Choise_hour_graphics_summer.setItemText(3, QCoreApplication.translate("Widget", u"4 \u0447.", None))

        self.take_hour_GN_summer.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

