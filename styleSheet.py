"""
    /* ===== Global Base ===== */
    QMainWindow, QWidget {
        background-color: #240200;   /* deep espresso base */
        color: #fce8d1;              /* cream text */
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-size: 14px;
    }

    /* ===== Menubar ===== */
    QMenuBar {
        background-color: #610c01;   /* rich coffee brown */
        color: #fce8d1;
        padding: 6px;
    }
    QMenuBar::item {
        background-color: transparent;
        padding: 6px 12px;
    }
    QMenuBar::item:selected {
        background-color: #912309;   /* warm burnt red */
        color: #ffffff;
        border-radius: 4px;
    }

    /* ===== Menus ===== */
    QMenu {
        background-color: #240200;
        border: 1px solid #610c01;
    }
    QMenu::item {
        padding: 6px 20px;
        color: #fce8d1;
    }
    QMenu::item:selected {
        background-color: #df7534;   /* terracotta */
        color: #ffffff;
        border-radius: 4px;
    }

    /* ===== Buttons ===== */
    QPushButton {
        background-color: #912309;   /* accent red-brown */
        color: #fce8d1;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
    }
    QPushButton:hover {
        background-color: #df7534;   /* terracotta highlight */
        color: #ffffff;
    }
    QPushButton:pressed {
        background-color: #f2b276;   /* caramel pressed */
        color: #240200;
    }
    QPushButton:disabled {
        background-color: #3a1a10;
        color: #777777;
    }

    /* ===== Tool Buttons ===== */
    QToolButton {
        background-color: #912309;
        color: #fce8d1;
        border-radius: 6px;
        padding: 6px;
    }
    QToolButton:hover {
        background-color: #df7534;
        color: #ffffff;
    }

    /* ===== Labels ===== */
    QLabel {
        color: #fce8d1;
        font-size: 13px;
    }

    /* ===== Sliders ===== */
    QSlider::groove:horizontal {
        background: #610c01;
        height: 6px;
        border-radius: 3px;
    }
    QSlider::handle:horizontal {
        background: #f2b276;   /* caramel handle */
        border-radius: 8px;
        width: 14px;
        margin: -4px 0;
    }
    QSlider::sub-page:horizontal {
        background: #df7534;
        border-radius: 3px;
    }

    /* ===== Viewport (Image Panel) ===== */
    QGraphicsView, QLabel#imageViewport {
        background-color: #2a0a04;   /* espresso canvas bg */
        border: 2px solid #912309;
        border-radius: 10px;
    }

    /* ===== Status Bar ===== */
    QStatusBar {
        background-color: #610c01;
        color: #fce8d1;
    }
"""