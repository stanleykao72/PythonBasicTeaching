# -*- coding: utf-8 -*-
import json
import sys
import os
import time
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from datetime import datetime

from MarkQtUI_Radio_end import Ui_MainWindow


class Mark(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        # 繼承Ui_MainWindow 也就是 mark_tool 內的 class
        super(Mark, self).__init__(parent)

        # 建立ui介面
        self.setupUi(self)
        # 這功能主要是點擊了這個按鈕要執行什麼？
        # self.clickTestButton 這個 function 在 MarkQtUI.Ui_MainWindow內
        # 因為已經繼承了Ui_MainWindow，因此執行 self.Test_Button
        # 點擊了時候會套用下方的function test_button_clicked，會將值輸出
        # 如果沒有這行，點擊按鈕不會有任何的動作
        self.clickTestButton.clicked.connect(self.test_button_clicked)

        # 下面兩個是我們新增的按鈕，因此我們給他指定的function，當使用者點擊了之後會跑去對應的function做操作
        self.clickDateButton.clicked.connect(self.date_button_clicked)
        self.clickTimeButton.clicked.connect(self.time_button_clicked)

        # 下面三個是我們新增的三個 Radio 按鈕，因此我們給他指定的function，當使用者點擊了之後會跑去對應的function做操作
        self.clickWaterRadioButton.clicked.connect(self.water_radio_button_clicked)
        self.clickJuiceRadioButton.clicked.connect(self.juice_radio_button_clicked)
        self.clickColaRadioButton.clicked.connect(self.cola_radio_button_clicked)

        # 當你想對你所選擇到的 Radio做其他操作可以多設定一個參數值給他
        self.selectRadioStr = ''
        self.drink_dict = Mark.getJsonToDictData(self)

        self.selectRadioButton.clicked.connect(self.select_radio_button_clicked)

    def logv2(self, title, msg):
        """
        :param title: log 的 開頭
        :param msg: 你想顯示的訊息
        :return: [2020/02/28 14:35:29][test] Hi
        """
        timeStr = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        log_message = '[' + str(timeStr) + '][' + title + '] ' + str(msg)
        # print(log_message)  # 如果你把註解拿掉，你的終端機就會顯示 Log
        return log_message

    def test_button_clicked(self):
        """
        當我們每點擊一次 self.clickTestButton 按鈕的時候，就會執行這裡
        每點擊一次就會顯示在我們剛建立起來的 self.displayListWidget (List Widget)
        類似：[2020/02/28 14:40:38][PyQt5教學] 有問題可以問我喔！
        """
        self.displayListWidget.addItem(self.logv2('PyQt5教學', '有問題可以問我喔！'))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的

    def date_button_clicked(self):
        """
        當我們每點擊一次 self.clickDateButton 按鈕的時候，就會執行這裡
        類似：[2020/03/07 23:42:17][現在日期] 2020-03-07
        """
        now_data = datetime.now().strftime("%Y-%m-%d")
        self.displayListWidget.addItem(self.logv2('現在日期', now_data))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的

    def time_button_clicked(self):
        """
        當我們每點擊一次 self.clickTimeButton 按鈕的時候，就會執行這裡
        類似：[2020/03/07 23:42:19][現在時間] 23:42:19
        """
        now_time = datetime.now().strftime("%H:%M:%S")
        self.displayListWidget.addItem(self.logv2('現在時間', now_time))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的

    def water_radio_button_clicked(self):
        """
        當我們每點擊一次 self.clickWaterRadioButton 按鈕的時候，就會執行這裡
        類似：[2020/03/07 23:42:19][現在時間] 23:42:19
        """
        self.displayListWidget.addItem(self.logv2('你選擇的是', self.drink_dict['drink']['water']))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的
        self.selectRadioStr = self.drink_dict['drink']['water']

    def juice_radio_button_clicked(self):
        """
        當我們每點擊一次 self.clickTimeButton 按鈕的時候，就會執行這裡
        類似：[2020/03/07 23:42:19][現在時間] 23:42:19
        """
        self.displayListWidget.addItem(self.logv2('你選擇的是', self.drink_dict['drink']['juice']))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的
        self.selectRadioStr = self.drink_dict['drink']['juice']

    def cola_radio_button_clicked(self):
        """
        當我們每點擊一次 self.clickTimeButton 按鈕的時候，就會執行這裡
        類似：[2020/03/07 23:42:19][現在時間] 23:42:19
        """
        self.displayListWidget.addItem(self.logv2('你選擇的是', self.drink_dict['drink']['cola']))  # 顯示在我們剛建立的 List Widget內
        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的
        self.selectRadioStr = self.drink_dict['drink']['cola']

    def select_radio_button_clicked(self):
        if self.selectRadioStr == '':
            self.displayListWidget.addItem(self.logv2('你的選擇是', '請你點選下方任一個飲料'))  # 顯示在我們剛建立的 List Widget內
        else:
            self.displayListWidget.addItem(self.logv2('你最後選擇的是', self.selectRadioStr))  # 顯示在我們剛建立的 List Widget內

        self.displayListWidget.scrollToBottom()  # 這行很重要，如果你沒加這行，你的如果超過self.displayListWidget範圍的話，他是不會往下執行的

    def PATH(self, p):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), p))

    def json_parser(self, raw_data):
        # json -> dict of python
        json_data = json.loads(raw_data)
        return json_data

    def getJsonToDictData(self):

        # 取得 json
        read_drink_data = open(str(self.PATH('./drink.json')), "r")
        raw_data = read_drink_data.read()
        read_drink_data.close()

        # 將 json to dict
        drink_dict = self.json_parser(raw_data)

        return drink_dict


if __name__ == "__main__":
    
    # 第一行必備，系統呼叫
    app = QApplication(sys.argv)

    # 指定 Mark Class 會先執行__init__
    window = Mark()

    # 將GUI介面顯示出來
    window.show()

    # 關閉系統
    sys.exit(app.exec_())
