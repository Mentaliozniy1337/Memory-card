style = """

/* Основные стили для приложения */
QWidget {
    background-color: #0A0F25; /* Темно-синий цвет фона */
    color: #E0E0E0; /* Светло-серый текст */
    font-size: 16px;
}

/* Стили для кнопок */
QPushButton {
    background-color: #1C2541;
    color: #FFD700; /* Золотой цвет текста */
    border: 2px solid #FFD700; /* Полупрозрачная золотая обводка */
    padding: 8px;
    border-radius: 5px;
    font-weight: bold;
}

/* Эффект свечения при наведении */
QPushButton:hover {
    background-color: #FFD700;
    color: #1C2541;
    border: 2px solid #FFD700;
}

/* Группы ответов */
QGroupBox {
    border: 2px solid #FFD700;
    border-radius: 5px;
    margin-top: 10px;
    font-size: 18px;
    font-weight: bold;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 5px;
    color: #FFD700;
}

/* Радио-кнопки */
QRadioButton {
    color: #E0E0E0;
    font-size: 16px;
}

/* Поля ввода */
QLineEdit, QSpinBox {
    background-color: #132238;
    border: 2px solid #FFD700;
    border-radius: 5px;
    padding: 5px;
    color: #FFD700;
}

/* Метки (Labels) */
QLabel {
    font-size: 16px;
    font-weight: bold;
}

/* Статистика */
#lb_header_stat {
    font-size: 20px;
    font-weight: bold;
    color: #FFD700;
}

"""
