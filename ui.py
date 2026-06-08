from PySide6.QtWidgets import QMainWindow, QHBoxLayout , QWidget , QVBoxLayout , QLineEdit, QPushButton
from PySide6.QtCore import Qt


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,600)
        #the main center widget.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #this is the main root layout.
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)


        #left side widget
        self.left_widget = QWidget()
        self.main_layout.addWidget(self.left_widget)
        self.left_layout = QVBoxLayout()
        self.left_widget.setLayout(self.left_layout)

        #now for the search button and Fetch button.
        self.sec_left_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Search By cities.')
        self.sec_left_layout.addWidget(self.search_bar)
        self.sec_left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.left_layout.addLayout(self.sec_left_layout)

        #now the fetch button.
        self.fetch_btn = QPushButton('Fetch')
        self.sec_left_layout.addWidget(self.fetch_btn)
        self.left_layout.addLayout(self.sec_left_layout)

        # right side widget.
        self.right_widget = QWidget()
        self.main_layout.addWidget(self.right_widget)
        self.right_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)








