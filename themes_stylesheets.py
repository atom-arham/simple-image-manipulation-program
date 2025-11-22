import sys 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QCheckBox,
                               QMenuBar, QMenu, QFrame, QHBoxLayout, QFileDialog, QPushButton, QGridLayout, QSlider)
from PySide6.QtCore import Qt   
from PySide6.QtGui import QAction 


    
def darkmode():
        return ("""
    /* ===== Global Base ===== */
    QMainWindow, QWidget {
        background-color: #1E1E24;    /* dark base */
        color: #f5f5f5;               /* light text */
        font-family: "Fira Code", "JetBrains Mono", "Cascadia Code", monospace;
        font-size: 14px;
    }

    /* ===== Menubar ===== */
    QMenuBar {
        background-color: #1E1E24;
        color: #f5f5f5;
        border-bottom: 1px solid #2a2a2a;
    }
    QMenuBar::item {
        padding: 6px 12px;
        background: transparent;
    }
    QMenuBar::item:selected {
        background: #2a2a2a;
        border-radius: 4px;
    }

    /* ===== Menus ===== */
    QMenu {
        background-color: #1e1e1e;
        border: 1px solid #333;
        color: #f5f5f5;
    }
    QMenu::item {
        padding: 6px 20px;
    }
    QMenu::item:selected {
        background-color: #3a3a3a;
        border-radius: 4px;
    }

    /* ===== Buttons ===== */
    QPushButton {
        background-color: #2A2A32;
        color: #f5f5f5;
        border: 1px solid #5C5470;
        border-radius: 6px;
        padding: 6px 12px;
    }
    QPushButton:hover {
        background-color: #3c3c3c;
    }
    QPushButton:pressed {
        background-color: #505050;
    }
    QPushButton:disabled {
        background-color: #2a2a2a;
        color: #777;
        border: 1px solid #2a2a2a;
    }

    /* ===== Tool Buttons ===== */
    QToolButton {
        background-color: #2A2A32;
        padding: 6px 6px;
        border: 1px solid transparent;
        border-radius: 6px;
    }
    QToolButton:hover{
        background-color: #3c3c3c;
        border: 1px solid #5C5470;
    }
    QToolButton:pressed{
        background-color: #505050;
    }      
    
    /* ===== Group Boxes (New for Adjustments Panel) ===== */
    QGroupBox {
        border: 1px solid #444;
        border-radius: 6px;
        margin-top: 20px; /* Leave space for the title */
        font-weight: bold;
        padding-top: 10px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        subcontrol-position: top left;
        left: 10px;
        padding: 0 5px;
        background-color: #1E1E24; /* Matches window bg to hide border behind text */
        color: #aaa;
    }

    /* ===== Labels ===== */
    QLabel {
        color: #f5f5f5;
        font-size: 13px;
    }

    /* ===== Scroll Areas ===== */
    QScrollArea {
        background-color: #1E1E24;
        border: none;
    }
    
    /* Specific styling for buttons inside Scroll Areas (Blur menu) */
    QScrollArea QPushButton {
        text-align: left;
        background-color: transparent;
        border: none;
        padding: 8px 15px;
    }
    QScrollArea QPushButton:hover {
        background-color: #2A2A32;
        border-radius: 4px;
    }

    /* ===== Tabs ===== */
    QTabWidget::pane {
        border: 1px solid #2a2a2a;
        background: #2C2C36;
        border-radius: 4px;
        margin-top: -1px; 
    }
    QTabBar::tab {
        background-color: #1e1e1e;   
        color: #888;
        padding: 8px 20px;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        margin-right: 4px;
        border: 1px solid #2a2a2a;
        border-bottom: none;
    }
    QTabBar::tab:selected {
        background: #2C2C36;
        color: #fff;
        font-weight: bold;
        border-bottom: 1px solid #2C2C36; /* Blend with pane */
    }
    QTabBar::tab:hover {
        background: #252525;
        color: #ccc;
    }

    /* ===== Sliders ===== */
    QSlider::groove:horizontal {
        height: 6px;
        background: #2a2a2a;
        border-radius: 3px;
    }
    QSlider::handle:horizontal {
        background: #5a5a5a;
        border: 1px solid #777;
        width: 14px;
        margin: -5px 0;
        border-radius: 7px;
    }
    QSlider::handle:horizontal:hover {
        background: #777;
    }

    /* ===== ComboBox ===== */
    QComboBox {
        background-color: #2b2b2b;
        border: 1px solid #3a3a3a;
        border-radius: 6px;
        padding: 4px 8px;
        color: #f5f5f5;
    }
    QComboBox QAbstractItemView {
        background-color: #1e1e1e;
        border: 1px solid #3a3a3a;
        selection-background-color: #3c3c3c;
        selection-color: #ffffff;
    }

    /* ===== Frames ===== */
    QFrame {
        border: none;
        background-color: transparent;
    }

    /* ===== Scrollbars ===== */
    QScrollBar:vertical {
        background: #1a1a1a;
        width: 10px;
        margin: 0;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #444;
        border-radius: 5px;
        min-height: 20px;
    }
    QScrollBar::handle:vertical:hover {
        background: #555;
    }
    QScrollBar:horizontal {
        background: #1a1a1a;
        height: 10px;
        border-radius: 5px;
    }
    QScrollBar::handle:horizontal {
        background: #444;
        border-radius: 5px;
        min-width: 20px;
    }
    QScrollBar::handle:horizontal:hover {
        background: #555;
    }
        /* Panels */
    #main_panel {
        background-color: #2A2A32;  
        border: 1px solid #5C5470;
        }

    #filter_panel {
        background-color: #32323C;   
        border: 1px solid #5C5470;
        }

    #right_panel {
        background-color: #2C2C36;   
        border: 1px solid #5C5470;
        }

    QIcon {
        corner-radius: 8px;
        }       
    """)

def lightmode():        
        return ("""
            /* ===== Global Base ===== */
            QMainWindow, QWidget {
                background-color: #faf9fd;   /* near white lilac */
                color: #2a173b;              /* deep violet text */
                font-family: "Fira Code", "JetBrains Mono", "Cascadia Code", monospace;
                font-size: 14px;
            }

            /* ===== Menubar ===== */
            QMenuBar {
                background-color: #e8e4f9;
                color: #2a173b;
                border-bottom: 1px solid #2a2a2a;
                
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 6px 12px;
            }
            QMenuBar::item:selected {
                background: #d1c7f3;
                border-radius: 4px;
                background-color: #d1c7f3;   /* soft violet highlight */
            }

            /* ===== Menus ===== */
            QMenu {
                background-color: #ffffff;
                border: 1px solid #d1c7f3;
            }
            QMenu::item {
                padding: 6px 20px;
                color: #2a173b;
            }
            QMenu::item:selected {
                background-color: #d1c7f3;
                color: #000000;
                border-radius: 4px;
            }

            /* ===== Buttons ===== */
            QPushButton {
                background-color: #e8e4f9;   /* pale lavender button */
                color: #2a173b;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #d1c7f3;   /* brighter violet */
                color: #000000;
            }
            QPushButton:pressed {
                background-color: #b8a8eb;   /* medium lilac pressed */
                color: #ffffff;
            }
            QPushButton:disabled {
                background-color: #f0edf9;
                color: #9a90b8;
            }

            /* ===== Tool Buttons ===== */
            QToolButton {
                background-color: #e8e4f9;
                color: #2a173b;
                border-radius: 6px;
                padding: 6px;
            }
            QToolButton:hover {
                background-color: #d1c7f3;
                color: #000000;
            }

            /* ===== Group Boxes (New) ===== */
            QGroupBox {
                border: 1px solid #d1c7f3;
                border-radius: 6px;
                margin-top: 20px;
                font-weight: bold;
                color: #3f2c5f;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 10px;
                padding: 0 5px;
                background-color: #faf9fd;
            }

            /* ===== Labels ===== */
            QLabel {
                color: #3f2c5f;   /* indigo text */
                font-size: 13px;
            }

            /* ===== Scroll Areas ===== */
            QScrollArea {
                background-color: #faf9fd;
                border: none;
            }
            
            /* Specific styling for buttons inside Scroll Areas (Blur menu) */
            QScrollArea QPushButton {
                text-align: left;
                background-color: transparent;
                border: none;
                padding: 8px 15px;
            }
            QScrollArea QPushButton:hover {
                background-color: #e8e4f9;
                border-radius: 4px;
            }

            /* ===== Tabs ===== */
            QTabWidget::pane {
                border: 1px solid #d1c7f3;
                background: #ffffff;
                border-radius: 4px;
                margin-top: -1px;
            }
            QTabBar::tab {
                background-color: #e8e4f9;
                color: #555;
                padding: 8px 20px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                margin-right: 4px;
            }
            QTabBar::tab:selected {
                background: #ffffff;
                color: #3f2c5f;
                font-weight: bold;
                border: 1px solid #d1c7f3;
                border-bottom: none;
            }
            QTabBar::tab:hover {
                background: #f0edf9;
            }

            /* ===== Sliders ===== */
            QSlider::groove:horizontal {
                background: #e8e4f9;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #b8a8eb;   /* lilac handle */
                border-radius: 8px;
                width: 14px;
                margin: -4px 0;
            }
            QSlider::sub-page:horizontal {
                background: #d1c7f3;
                border-radius: 3px;
            }

            /* ===== Viewport (Image Panel) ===== */
            QGraphicsView, QLabel#imageViewport {
                background-color: #ffffff;   /* bright canvas bg */
                border: 2px solid #e8e4f9;
                border-radius: 10px;
            }

            /* ===== Status Bar ===== */
            QStatusBar {
                background-color: #e8e4f9;
                color: #2a173b;
            }

            /* Custom Panels */
        #main_panel {
            background-color: #faf9fd;  
            border: 2px solid #3f2c5f;
            }

        #filter_panel {
            background-color: #faf9fd;   /* deep purple */
            border: 2px solid #3f2c5f;
            
            
            }

        #right_panel {
            background-color: #faf9fd;   /* teal tint */
            border: 2px solid #3f2c5f;
            }
            """)