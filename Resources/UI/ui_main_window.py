# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowBQNsuK.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 720)
        MainWindow.setMinimumSize(QSize(1120, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Central Widget */\n"
"QWidget#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"    border: none;               /* No border for a cleaner look */\n"
"    padding: 15px;              /* Padding inside the central widget */\n"
"}\n"
"\n"
"/* Scroll Area Styling (optional) */\n"
"QScrollArea {\n"
"    background-color: transparent; /* Transparent to match the central widget */\n"
"    border: none;                  /* No border */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #3c3f41;    /* Darker gray for scroll bar background */\n"
"    width: 12px;                  /* Scroll bar width */\n"
"    margin: 22px 0 22px 0;        /* Top and bottom margins */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5b5e60;    /* Slightly lighter gray for scroll handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;             /* Remove arrows */\n"
"}\n"
"\n"
"/* "
                        "QPushButton */\n"
"QPushButton {\n"
"    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"    padding: 6px 12px;          /* Padding for comfortable button size */\n"
"    font-size: 14px;            /* Button text size */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"    font-size: 14px;            /* Set font size */\n"
"    padding: 3px;              /* Padding inside the central widget */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-colo"
                        "r: #2e2e2e;  /* Dark gray for frames */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"    padding: 6px;               /* Padding for text input area */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text"
                        " input */\n"
"    font-size: 13px;            /* Slightly smaller font */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 14px;             /* Font size for readability */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;                 /* Size of the radio button */\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue "
                        "on hover */\n"
"    border-color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 6px 12px;            /* Padd"
                        "ing for comfortable button size */\n"
"    font-size: 14px;              /* Font size for text (if any) */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    /* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 9, -1, -1)
        self.gsc_code_input_area = QPlainTextEdit(self.frame_5)
        self.gsc_code_input_area.setObjectName(u"gsc_code_input_area")
        self.gsc_code_input_area.setFrameShape(QFrame.Shape.NoFrame)
        self.gsc_code_input_area.setTabStopDistance(8.000000000000000)

        self.horizontalLayout_4.addWidget(self.gsc_code_input_area)

        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.convert_gsc_to_py_btn = QPushButton(self.frame)
        self.convert_gsc_to_py_btn.setObjectName(u"convert_gsc_to_py_btn")
        icon = QIcon()
        icon.addFile(u":/888EAC-20px/ICONS/888EAC-20px/arrow-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convert_gsc_to_py_btn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.convert_gsc_to_py_btn)

        self.convert_py_to_gsc_btn = QPushButton(self.frame)
        self.convert_py_to_gsc_btn.setObjectName(u"convert_py_to_gsc_btn")
        icon1 = QIcon()
        icon1.addFile(u":/888EAC-20px/ICONS/888EAC-20px/arrow-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convert_py_to_gsc_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.convert_py_to_gsc_btn)


        self.horizontalLayout_4.addWidget(self.frame)

        self.python_code_input_area = QPlainTextEdit(self.frame_5)
        self.python_code_input_area.setObjectName(u"python_code_input_area")
        self.python_code_input_area.setFrameShape(QFrame.Shape.NoFrame)
        self.python_code_input_area.setTabStopDistance(8.000000000000000)

        self.horizontalLayout_4.addWidget(self.python_code_input_area)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phils-Hub - GSC > Py Bidirectional Converter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GSC", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.gsc_code_input_area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste gsc code here to convert to python", None))
#if QT_CONFIG(tooltip)
        self.convert_gsc_to_py_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Convert gsc to py", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.convert_py_to_gsc_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Convert py to gsc", None))
#endif // QT_CONFIG(tooltip)
        self.python_code_input_area.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste python code here to convert to gsc", None))
    # retranslateUi

