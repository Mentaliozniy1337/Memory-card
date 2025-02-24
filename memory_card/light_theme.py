style = """
/* Основные стили для приложения */
QWidget {
    background-color: #E3F2FD; /* Светло-голубой фон */
    color: #0D47A1; /* Темно-синий текст */
    font-size: 16px;
}

/* Стили для кнопок */
QPushButton {
    background-color: #1976D2; /* Насыщенный синий */
    color: #FFFFFF; /* Белый текст */
    border: 2px solid #1565C0; /* Темно-синяя обводка */
    padding: 8px;
    border-radius: 5px;
    font-weight: bold;
}

/* Эффект свечения при наведении */
QPushButton:hover {
    background-color: #1565C0; /* Темнее при наведении */
    color: #E3F2FD; /* Светло-голубой */
    border: 2px solid #0D47A1;
}

/* Группы ответов */
QGroupBox {
    border: 2px solid #0D47A1;
    border-radius: 5px;
    margin-top: 10px;
    font-size: 18px;
    font-weight: bold;
    background-color: #BBDEFB; /* Светло-синий фон */
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 5px;
    color: #0D47A1;
}

/* Радио-кнопки */
QRadioButton {
    color: #0D47A1;
    font-size: 16px;
}

/* Поля ввода */
QLineEdit, QSpinBox {
    background-color: #FFFFFF; /* Белый фон */
    border: 2px solid #1976D2;
    border-radius: 5px;
    padding: 5px;
    color: #0D47A1;
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
    color: #0D47A1;
}
"""
