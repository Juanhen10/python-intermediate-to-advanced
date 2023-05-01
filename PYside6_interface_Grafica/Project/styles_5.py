
# qt-material
# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import sys

import qdarktheme
from qt_material import apply_stylesheet
from variables_2 import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                         PRIMARY_COLOR)

color_list = ['dark_amber.xml',
              'dark_blue.xml',
              'dark_cyan.xml',
              'dark_lightgreen.xml',
              'dark_pink.xml',
              'dark_purple.xml',
              'dark_red.xml',
              'dark_teal.xml',
              'dark_yellow.xml',
              'light_amber.xml',
              'light_blue.xml',
              'light_cyan.xml',
              'light_cyan_500.xml',
              'light_lightgreen.xml',
              'light_pink.xml',
              'light_purple.xml',
              'light_red.xml',
              'light_teal.xml',
              'light_yellow.xml']


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def theme_1(app, style):
    th = apply_stylesheet(app, style)
    return th


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={"[dark]": {
            "primary": f"{PRIMARY_COLOR}",
        },
            "[light]": {
            "primary": f"{PRIMARY_COLOR}",
        }, },
        additional_qss=qss)
