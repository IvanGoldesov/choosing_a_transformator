import sys
import GN_winter_ui_four_hour
import GN_winter_ui_two_hour
import GN_winter_ui_one_hour

import GN_winter_ui_four_hour_summer
import GN_winter_ui_two_hour_summer
import GN_winter_ui_one_hour_summer

import k_sez_ui

from typing import Optional
from PySide6.QtCore import Qt

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from result_ui import Ui_Form
from form_ui import Ui_Widget


class ExpenceTracker(QMainWindow):
    def __init__(self) -> None:
        super(ExpenceTracker, self).__init__()
        #Определяем основное окно
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
       

        #Окно ГН 1 час зима
        self.new_window_one_hour_winter = QtWidgets.QDialog()
        self.ui_window_one_hour_winter = GN_winter_ui_one_hour.Ui_Form()
        self.ui_window_one_hour_winter.setupUi(self.new_window_one_hour_winter)

        #Окно ГН 1 час лето
        self.new_window_one_hour_summer = QtWidgets.QDialog()
        self.ui_window_one_hour_summer = GN_winter_ui_one_hour_summer.Ui_Form()
        self.ui_window_one_hour_summer.setupUi(self.new_window_one_hour_summer)

        #Окно ГН 2 часа зима

        self.new_window_two_hour_winter = QtWidgets.QDialog()
        self.ui_window_two_hour_winter = GN_winter_ui_two_hour.Ui_Form()
        self.ui_window_two_hour_winter.setupUi(self.new_window_two_hour_winter)

        #Окно ГН 2 часа лето

        self.new_window_two_hour_summer = QtWidgets.QDialog()
        self.ui_window_two_hour_summer = GN_winter_ui_two_hour_summer.Ui_Form()
        self.ui_window_two_hour_summer.setupUi(self.new_window_two_hour_summer)

        #Окно ГН 4 часа зима

        self.new_window_four_hour_winter = QtWidgets.QDialog()
        self.ui_window_four_hour_winter = GN_winter_ui_four_hour.Ui_Form()
        self.ui_window_four_hour_winter.setupUi(self.new_window_four_hour_winter)

        #Окно ГН 4 часа лето

        self.new_window_four_hour_summer = QtWidgets.QDialog()
        self.ui_window_four_hour_summer = GN_winter_ui_four_hour_summer.Ui_Form()
        self.ui_window_four_hour_summer.setupUi(self.new_window_four_hour_summer)

        #Окно Ксез
        self.new_window_k_sez = QtWidgets.QDialog()
        self.ui_window_k_sez = k_sez_ui.Ui_Form()
        self.ui_window_k_sez.setupUi(self.new_window_k_sez)      

        #Для обращения к нужной функции и получения данных из таблицы
        self.dict_gn_winter = {
            '1' : (self.ui_window_one_hour_winter, self.new_window_one_hour_winter),
            '2' : (self.ui_window_two_hour_winter, self.new_window_two_hour_winter),
            '4' : (self.ui_window_four_hour_winter, self.new_window_four_hour_winter)
        }

        self.dict_gn_summer = {
            '1' : (self.ui_window_one_hour_summer, self.new_window_one_hour_summer),
            '2' : (self.ui_window_two_hour_summer, self.new_window_two_hour_summer),
            '4' : (self.ui_window_four_hour_summer, self.new_window_four_hour_summer)
        }


        #Обработка нажатия кнопок
        self.ui.compute_button.clicked.connect(self.result)

        #Обрабатываем нажатие кнопки для записи данных мощностей графиков нагрузки
        self.ui.take_hour_GN_winter.clicked.connect(self.compute_result_winter)
        self.ui.take_hour_GN_summer.clicked.connect(self.compute_result_summer)
        
        #Нажатие кнопок для обработки введенных данных в таблицу ГН
        self.ui_window_one_hour_winter.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_one_hour_summer.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_two_hour_winter.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_two_hour_summer.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_four_hour_winter.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_four_hour_summer.one_hour_button_okey.clicked.connect(self.get_data)
        self.ui_window_k_sez.okey_button.clicked.connect(self.calculate)



    def compute_result_winter(self):
        self.num_graph_winter = self.ui.Choise_hour_graphics.currentText()

        if self.num_graph_winter: 
            if self.num_graph_winter[0] == '1':
                self.one_hour_winter()
            elif self.num_graph_winter[0] == '2':
                self.two_hour_winter()
            else:
                self.four_hour_winter()
        else:
            error = QMessageBox()
            error.setWindowTitle('Внимание!')
            error.setText('Выберите количество часов в зимнем графике нагрузки и заполните его')
            
            error.exec()

    def compute_result_summer(self):
        self.num_graph_summer = self.ui.Choise_hour_graphics_summer.currentText()

        if self.num_graph_summer:
            if self.num_graph_summer[0] == '1':
                self.one_hour_summer()
            elif self.num_graph_summer[0] == '2':
                self.two_hour_summer()
            elif self.num_graph_summer[0] == '4':
                self.four_hour_summer()
            else:
                try:
                    if self.widgetItem_winter:
                        self.kef_sez()
                    else:
                        error = QMessageBox()
                        error.setWindowTitle('Внимание!')
                        error.setText('Выберите количество часов в зимнем графике нагрузки и заполните его')
                
                        error.exec()
                except:
                    error = QMessageBox()
                    error.setWindowTitle('Внимание!')
                    error.setText('Выберите количество часов в зимнем графике нагрузки и заполните его')
                
                    error.exec()


    def one_hour_winter(self):
        self.new_window_one_hour_winter.show()

    def one_hour_summer(self):
        self.new_window_one_hour_summer.show()


    def two_hour_winter(self):
        
        self.new_window_two_hour_winter.show()

    def two_hour_summer(self):
        
        self.new_window_two_hour_summer.show()

    def four_hour_winter(self):
       
        self.new_window_four_hour_winter.show()

    def four_hour_summer(self):
        
        self.new_window_four_hour_summer.show()

    def kef_sez(self):
        self.new_window_k_sez.show()
        

    def calculate(self):
        k_sez = float(self.ui_window_k_sez.k_sez_edit.text())
        self.widgetItem_summer = list(map(lambda x: int(x)*k_sez, self.widgetItem_winter))
        print(self.widgetItem_summer)
        
        self.new_window_k_sez.close()
        


    def get_data(self):
        
        sender = self.sender()

        if sender.text() == 'Принять ГН для зимы':
            info = self.dict_gn_winter[self.num_graph_winter[0]] 
            self.widgetItem_winter = []
        else:
            info = self.dict_gn_summer[self.num_graph_summer[0]] 
            self.widgetItem_summer = []
        
        rowCount = info[0].tableWidget.rowCount()
        columnCount = info[0].tableWidget.columnCount()

        if sender.text() == 'Принять ГН для зимы':
            for row in range(rowCount):
                for column in range(columnCount):
                    self.widgetItem_winter.append(info[0].tableWidget.item(row, column).text())
        else:
            for row in range(rowCount):
                for column in range(columnCount):
                    self.widgetItem_summer.append(info[0].tableWidget.item(row, column).text())

        info[1].close()


    def result(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Form()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

        u_vn = self.ui.Uvn.text()

        if self.ui.temperature_winter.text():
            temperature_winter = round(int(self.ui.temperature_winter.text()), -1)
        if self.ui.temperature_summer.text():
            temperature_summer = round(int(self.ui.temperature_summer.text()), -1)

        S_winter = list(map(float, self.widgetItem_winter))
        
        S_summer = list(map(float, self.widgetItem_summer))


        """a = self.compute_result()
        self.ui_window.textBrowser.setText(str())"""
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenceTracker()
    window.show()

    sys.exit(app.exec())