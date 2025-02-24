from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import light_theme as light_theme
import dark_theme as dark_theme


windows = []

# Определяем глобальную переменную is_dark
is_dark = False

# Глобальная переменная для кнопки озвучки
speech_button = None

def toggle_theme():
    """Переключает тему для всех окон"""
    global is_dark
    for window in windows:
        if is_dark:
            window.setStyleSheet(light_theme.style)
        else:
            window.setStyleSheet(dark_theme.style)
    is_dark = not is_dark

def show_speech_button():
    """Показывает кнопку озвучки"""
    global speech_button
    if speech_button:
        speech_button.show()

def hide_speech_button():
    """Скрывает кнопку озвучки"""
    global speech_button
    if speech_button:
        speech_button.hide()

def show_menu():
    global menu_window  # Чтобы окно не закрывалось сразу
    menu_window = QWidget()
    menu_window.setWindowTitle("setting")
    menu_window.resize(500, 300)

    # Добавляем окно в глобальный список
    windows.append(menu_window)

    layout = QVBoxLayout()
    btn_close = QPushButton("Закрыть")
    btn_close.clicked.connect(menu_window.close)

    # Добавление кнопок в layout
    btn_youtube = QPushButton("Поддержка")
    btn_youtube.clicked.connect(open_youtube)
    
    btn_theme = QPushButton("Сменить тему")
    btn_theme.clicked.connect(toggle_theme)

    # Кнопка для включения озвучки
    global speech_button
    speech_button = QPushButton("Включить озвучку")
    speech_button.clicked.connect(show_speech_button)  # Когда нажмут на неё, она появится

    layout.addWidget(btn_close)
    layout.addWidget(btn_youtube)
    layout.addWidget(btn_theme)
    layout.addWidget(speech_button)  # Добавляем кнопку озвучки

    menu_window.setLayout(layout)
    
    # Показываем окно
    menu_window.show()


# Обработчик для открытия YouTube
def open_youtube():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    QDesktopServices.openUrl(QUrl(url))
