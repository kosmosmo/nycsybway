from PySide.QtGui import *
from PySide.QtCore import *

import sys

class subwayUi(QTabWidget):
    def __init__(self):
        super(subwayUi,self).__init__()

        self.setWindowTitle("NYC Subway")
        self.resize(500,700)

        #Widgets

        start_label = QLabel("Start")
        self.start_search_line_edit = QLineEdit()
        goal_label = QLabel("Goal ")
        self.goal_search_line_edit = QLineEdit()
        self.info_text_edit = QPlainTextEdit()
        self.start_list_widget = QListWidget()
        self.goal_list_widget = QListWidget()
        self.find_button = QPushButton('Find')
        self.close_button = QPushButton('Close')


        #Layout
        main_layout = QVBoxLayout()

        start_layout = QHBoxLayout()
        start_layout.addWidget(start_label)
        start_layout.addWidget(self.start_search_line_edit)


        goal_layout = QHBoxLayout()
        goal_layout.addWidget(goal_label)
        goal_layout.addWidget(self.goal_search_line_edit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.find_button)
        button_layout.addWidget(self.close_button)


        main_layout.addLayout(start_layout)
        main_layout.addWidget(self.start_list_widget)
        main_layout.addLayout(goal_layout)
        main_layout.addWidget(self.goal_list_widget)
        main_layout.addWidget(self.info_text_edit)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)






