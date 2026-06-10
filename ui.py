from PySide6.QtWidgets import QMainWindow, QHBoxLayout , QWidget , QVBoxLayout , QLineEdit, QPushButton , QLabel, QGridLayout
from PySide6.QtCore import Qt
from weather_api import get_weather_by_city
import datetime

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,500)
        #the main center widget.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet('background-color: #1e1e1e;')
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
        self.search_bar.setPlaceholderText('🔎  Search By cities.')
        self.search_bar.setStyleSheet('color:white;')
        self.sec_left_layout.addWidget(self.search_bar)
        self.sec_left_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.left_layout.addLayout(self.sec_left_layout)

        #now the fetch button.
        self.fetch_btn = QPushButton('Fetch')
        self.fetch_btn.setStyleSheet('color:white;')
        self.sec_left_layout.addWidget(self.fetch_btn)

        #running the imported function when fetch is clicked.
        self.fetch_btn.clicked.connect(self.fetch_weather)

        #now setting the elements,
        self.city_label =QLabel()
        self.left_layout.addWidget(self.city_label)
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.city_label.setStyleSheet('font-size:40px; font-weight:bold; color:white;')
        #country and date.
        self.country_date = QLabel()
        self.left_layout.addWidget(self.country_date)
        self.country_date.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.country_date.setStyleSheet('color:white; font-size:15px;')
        #temp
        self.temp_label = QLabel()
        self.left_layout.addWidget(self.temp_label)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.temp_label.setStyleSheet('color:white; font-size:45px; font-weight:bold;')
        #sky status.
        self.sky_status = QLabel()
        self.left_layout.addWidget(self.sky_status)
        #self.left_layout.addStretch()
        self.sky_status.setStyleSheet('color:white; font-size:15px')
        #2x2 box
        self.box_layout = QGridLayout()
        self.left_layout.addLayout(self.box_layout)
        self.left_layout.addStretch()

        self.humidity_box, self.humidity_value = self.create_box('💧 HUMIDITY')
        self.box_layout.addWidget(self.humidity_box, 0, 0)

        self.wind_box, self.wind_value = self.create_box('💨 WIND SPEED')
        self.box_layout.addWidget(self.wind_box, 0, 1)

        self.visibility_box, self.visibility_value = self.create_box('👁 VISIBILITY')
        self.box_layout.addWidget(self.visibility_box, 1, 0)

        self.feels_box, self.feels_value = self.create_box('🌡 FEELS LIKE')
        self.box_layout.addWidget(self.feels_box, 1, 1)

        # right side widget.
        self.right_widget = QWidget()
        self.main_layout.addWidget(self.right_widget)
        self.right_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)
        self.fetch_weather()

    def fetch_weather(self):
        search_input = self.search_bar.text().lower()
        weather = get_weather_by_city(search_input)

        City_name = weather['name']
        country = weather['sys']['country']
        date = datetime.datetime.today().strftime('%A, %B %d')
        temp = weather['main']['temp']
        sky_sts = weather['weather'][0]['description']

        #now for the box design
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        visibility = weather['visibility']
        feels_like = weather['main']['feels_like']

        self.city_label.setText(str(City_name))
        self.country_date.setText(str(f'{country}  {date}'))
        self.temp_label.setText(f'{temp}<span style="font-size:20px;">°C</span>')
        self.sky_status.setText(str(sky_sts))

        self.humidity_value.setText(f'{humidity} %')
        self.wind_value.setText(f'{wind_speed} km/h')
        self.visibility_value.setText(f'{(visibility)/1000} km')
        self.feels_value.setText(f'{feels_like} °C')

    def create_box(self, title_text):
        box = QWidget()
        box.setObjectName('weatherBox')
        box.setStyleSheet('#weatherBox {border: 1px solid #555; border-radius: 15px;}')
        box_layout = QVBoxLayout()
        box.setLayout(box_layout)
        title = QLabel(title_text)  # ← parameter, not hardcoded
        title.setStyleSheet('color:white; font-weight:bold;')
        value = QLabel()
        value.setStyleSheet('color:white; font-size:15px;')
        box_layout.addWidget(title)
        box_layout.addWidget(value)
        box_layout.addStretch()
        return box, value  # ← hand back both











