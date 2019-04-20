# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:02:29 2019

@author: wl181
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
 
 
class Ui_wnd_main(QMainWindow):
    def __init__(self):
        # Setup main window
        super().__init__()
        self.resize(988, 505)
        self.centralWidget = QtWidgets.QWidget(self)
 
        # Table
        self.create_image_table()
        self.setup_image_table()
 
        # Buttons
        self.create_button_block()
        self.setup_button_block()
 
        # Setup Layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
 
        self.verticalLayout.addWidget(self.tbl_images)
        self.verticalLayout.addLayout(self.lay_button_block)
 
        self.setCentralWidget(self.centralWidget)
        self.retranslateUi(self)
 
    def create_image_table(self):
        self.tbl_images = QtWidgets.QTableWidget(self.centralWidget)
        self.tbl_images.setColumnCount(6)
        self.tbl_images.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_images.setHorizontalHeaderItem(5, item)
 
    def setup_image_table(self):
        pass
 
    def create_button_block(self):
        self.lay_button_block = QtWidgets.QGridLayout()
        self.btn_contrast_invert = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_contrast_invert, 3, 1, 1, 1)
        self.btn_display = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_display, 1, 0, 1, 1)
        self.btn_display_hist = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_display_hist, 2, 0, 1, 1)
        self.btn_display_color_hist = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(
            self.btn_display_color_hist, 3, 0, 1, 1)
        self.btn_compare = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_compare, 0, 0, 1, 1)
        self.btn_equalize_hist = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_equalize_hist, 0, 1, 1, 1)
        self.btn_contrast_stretch = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_contrast_stretch, 1, 1, 1, 1)
        self.btn_log_compress = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_log_compress, 2, 1, 1, 1)
        self.btn_dload_jpeg = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_dload_jpeg, 0, 2, 1, 1)
        self.btn_dload_tiff = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_dload_tiff, 1, 2, 1, 1)
        self.btn_dload_png = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_dload_png, 2, 2, 1, 1)
        self.btn_upload = QtWidgets.QPushButton(self.centralWidget)
        self.lay_button_block.addWidget(self.btn_upload, 3, 2, 1, 1)
 
    def setup_button_block(self):
        self.btn_upload.clicked.connect(self.callback)
        self.btn_compare.clicked.connect(self.img_compare)
 
    def retranslateUi(self, wnd_main):
        _translate = QtCore.QCoreApplication.translate
        wnd_main.setWindowTitle(_translate("wnd_main", "MainWindow"))
 
        item = self.tbl_images.horizontalHeaderItem(0)
        item.setText(_translate("wnd_main", "ID"))
        item = self.tbl_images.horizontalHeaderItem(1)
        item.setText(_translate("wnd_main", "Filename"))
        item = self.tbl_images.horizontalHeaderItem(2)
        item.setText(_translate("wnd_main", "Format"))
        item = self.tbl_images.horizontalHeaderItem(3)
        item.setText(_translate("wnd_main", "Size"))
        item = self.tbl_images.horizontalHeaderItem(4)
        item.setText(_translate("wnd_main", "Description"))
        item = self.tbl_images.horizontalHeaderItem(5)
        item.setText(_translate("wnd_main", "Timestamp"))
        self.btn_contrast_invert.setText(
            _translate("wnd_main", "Contrast Invert"))
        self.btn_display.setText(_translate("wnd_main", "Display"))
        self.btn_display_hist.setText(_translate("wnd_main", "Display HIST"))
        self.btn_display_color_hist.setText(
            _translate("wnd_main", "Display Color HIST"))
        self.btn_compare.setText(_translate("wnd_main", "Compare"))
        self.btn_equalize_hist.setText(
            _translate("wnd_main", "Equalize Histogram"))
        self.btn_contrast_stretch.setText(
            _translate("wnd_main", "Contrast Stretch"))
        self.btn_log_compress.setText(_translate("wnd_main", "Log Compress"))
        self.btn_dload_jpeg.setText(_translate("wnd_main", "Download JPEG"))
        self.btn_dload_tiff.setText(_translate("wnd_main", "Download TIFF"))
        self.btn_dload_png.setText(_translate("wnd_main", "Download PNG"))
        self.btn_upload.setText(_translate("wnd_main", "Upload"))
 
    def callback(self):
        indexes = self.tbl_images.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())
        # linked to database ID TBA
        
    def img_compare(self):
         print("compare_algorithm")
         self.next = img_show_wnd

class img_show_wnd(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'Show Image Processed'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 480
        self.next = None
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(204, 204, 255))
        self.setPalette(p)
        self.statusBar().showMessage('Step 3: Process Image!')