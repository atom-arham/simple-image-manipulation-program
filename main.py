import sys 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QCheckBox,
                               QMenuBar, QMenu, QFrame, QHBoxLayout, QFileDialog, QPushButton, QGridLayout, QSlider)
from PySide6.QtCore import Qt   
from PySide6.QtGui import QAction

from utilities import importExport,history

class MainWindow(QMainWindow):
    def __init__(self, ie):
        super().__init__()
        self.ie = ie
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)
        self.ui()
        self.darkmode()
    def darkmode(self):
        self.setStyleSheet("""
    /* ===== Global Base ===== */
    QMainWindow, QWidget {
        background-color: #2a173b;   /* deep violet base */
        color: #f0eafc;              /* soft off-white text */
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-size: 14px;
    }

    /* ===== Menubar ===== */
    QMenuBar {
        background-color: #3f2c5f;   /* muted indigo */
        color: #f0eafc;
        padding: 6px;
    }
    QMenuBar::item {
        background-color: transparent;
        padding: 6px 12px;
    }
    QMenuBar::item:selected {
        background-color: #443f7b;   /* violet highlight */
        color: #ffffff;
        border-radius: 4px;
    }

    /* ===== Menus ===== */
    QMenu {
        background-color: #2a173b;
        border: 1px solid #3f2c5f;
    }
    QMenu::item {
        padding: 6px 20px;
        color: #f0eafc;
    }
    QMenu::item:selected {
        background-color: #443f7b;
        color: #ffffff;
        border-radius: 4px;
    }

    /* ===== Buttons ===== */
    QPushButton {
        background-color: #3f2c5f;   /* indigo button */

        color: #f0eafc;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
    }
    QPushButton:hover {
        background-color: #443f7b;   /* brighter violet */
        color: #ffffff;
    }
    QPushButton:pressed {
        background-color: #6a5dad;   /* lilac pressed */
        color: #2a173b;
    }
    QPushButton:disabled {
        background-color: #22132e;
        color: #6e6685;
    }

    /* ===== Tool Buttons ===== */
    QToolButton {
        background-color: #3f2c5f;
        color: #f0eafc;
        border-radius: 6px;
        padding: 6px;
    }
    QToolButton:hover {
        background-color: #443f7b;
        color: #ffffff;
    }

    /* ===== Labels ===== */
    QLabel {
        color: #e2daf9;
        font-size: 13px;
    }

    /* ===== Sliders ===== */
    QSlider::groove:horizontal {
        background: #3f2c5f;
        height: 6px;
        border-radius: 3px;
    }
    QSlider::handle:horizontal {
        background: #6a5dad;   /* lavender handle */
        border-radius: 8px;
        width: 14px;
        margin: -4px 0;
    }
    QSlider::sub-page:horizontal {
        background: #443f7b;
        border-radius: 3px;
    }

    /* ===== Viewport (Image Panel) ===== */
    QGraphicsView, QLabel#imageViewport {
        background-color: #1f122c;   /* darker canvas bg */
        border: 2px solid #3f2c5f;
        border-radius: 10px;
    }

    /* ===== Status Bar ===== */
    QStatusBar {
        background-color: #3f2c5f;
        color: #f0eafc;
    }
""")
        
    def lightmode(self):        
        self.setStyleSheet("""/* ===== Global Base ===== */
QMainWindow, QWidget {
    background-color: #fdf6f0;   /* soft cream base */
    color: #240200;              /* deep espresso text */
    font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
    font-size: 14px;
}

/* ===== Menubar ===== */
QMenuBar {
    background-color: #f2b276;   /* warm caramel */
    color: #240200;
    padding: 6px;
}
QMenuBar::item {
    background-color: transparent;
    padding: 6px 12px;
}
QMenuBar::item:selected {
    background-color: #df7534;   /* burnt orange highlight */
    color: #ffffff;
    border-radius: 4px;
}

/* ===== Menus ===== */
QMenu {
    background-color: #fdf6f0;
    border: 1px solid #f2b276;
}
QMenu::item {
    padding: 6px 20px;
    color: #240200;
}
QMenu::item:selected {
    background-color: #f2b276;   /* caramel highlight */
    color: #ffffff;
    border-radius: 4px;
}

/* ===== Buttons ===== */
QPushButton {
    background-color: #df7534;   /* terracotta accent */
    color: #fdf6f0;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #f2b276;   /* caramel highlight */
    color: #240200;
}
QPushButton:pressed {
    background-color: #fce8d1;   /* light cream pressed */
    color: #240200;
}
QPushButton:disabled {
    background-color: #f4d8c0;
    color: #a09088;
}

/* ===== Tool Buttons ===== */
QToolButton {
    background-color: #df7534;
    color: #fdf6f0;
    border-radius: 6px;
    padding: 6px;
}
QToolButton:hover {
    background-color: #f2b276;
    color: #240200;
}

/* ===== Labels ===== */
QLabel {
    color: #240200;
    font-size: 13px;
}

/* ===== Sliders ===== */
QSlider::groove:horizontal {
    background: #f2b276;
    height: 6px;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #df7534;   /* terracotta handle */
    border-radius: 8px;
    width: 14px;
    margin: -4px 0;
}
QSlider::sub-page:horizontal {
    background: #fce8d1;
    border-radius: 3px;
}

/* ===== Viewport (Image Panel) ===== */
QGraphicsView, QLabel#imageViewport {
    background-color: #fff1e0;   /* soft canvas */
    border: 2px solid #df7534;
    border-radius: 10px;
}

/* ===== Status Bar ===== */
QStatusBar {
    background-color: #f2b276;
    color: #240200;
}""")

    def ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        menu_bar = QMenuBar(self)
        #menu_bar.setFixedHeight(25)
        #menu_bar.setStyleSheet("background-color: rgba(163,102,255,25);border:none;")

        file_menu = QMenu("File", self)

        options_menu = QMenu("Options", self)
        mode_sub_menu = QMenu("Appearance", options_menu)
        dark_appearance = QAction("Dark", mode_sub_menu)
        dark_appearance.triggered.connect(self.darkmode)

        light_appearance = QAction("Light", mode_sub_menu)
        light_appearance.triggered.connect(self.lightmode)



        tool_undo = QAction("Undo", self)
        tool_redo = QAction("Redo", self)

        
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        
        import_action = QAction("Import", self)
        import_action.triggered.connect(self.import_file)

        file_menu.addAction(save_action)
        file_menu.addAction(import_action)

        menu_bar.addMenu(file_menu)
        mode_sub_menu.addAction(light_appearance)  
        mode_sub_menu.addAction(dark_appearance)
        options_menu.addMenu(mode_sub_menu)
        menu_bar.addMenu(options_menu)
        menu_bar.addAction(tool_undo)
        menu_bar.addAction(tool_redo)

        self.setMenuBar(menu_bar)

        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.NoFrame)
        frame.setLineWidth(0)
        main_layout.addWidget(frame)

        self.panel_layout = QHBoxLayout(frame)
        self.panel_layout.setContentsMargins(0, 0, 0, 0)
        self.panel_layout.setSpacing(0)

        # self.tools_side_panel = QWidget()
        # self.tools_side_panel.setFixedWidth(50)
        # self.tools_side_panel.setStyleSheet("background-color: rgba(163,102,255,65);border:none;")
        # self.tool_side_panel_items()

        self.main_panel = QLabel()
        #self.main_panel.setStyleSheet("background-color: rgba(163,102,255,25);border:none;")
        self.main_panel.setAlignment(Qt.AlignCenter)
        self.main_panel.setScaledContents(True)
        
        self.right_side_panel = QWidget()
        self.right_side_panel.setFixedWidth(400)
        self.right_side_panel.setContentsMargins(2,2,2,2)
        #self.right_side_panel.setStyleSheet("background-color: rgba(163,102,255,45);border:none;")
        self.right_panel_items()

        #self.panel_layout.addWidget(self.tools_side_panel)
        self.panel_layout.addWidget(self.main_panel)
        self.panel_layout.addWidget(self.right_side_panel)

    def tool_side_panel_items(self):
        layout_left = QVBoxLayout(self.tools_side_panel)  
        layout_left.setContentsMargins(5,5,5,5)
        layout_left.setSpacing(0)

        tool_undo = QPushButton("Undo")
        tool_undo.clicked.connect(his.undo)
        # tool_undo.setStyleSheet("""QPushButton{
        #                                background-color: rgba(163,102,255,200);
        #                                border:none;
        #                                padding: 8px 8px;
                                    
        #                                }
        #                                QPushButton:hover {
        #                                background-color: rgba(163,102,255,255);
        #                                }
        #                                QPushButton:pressed{
        #                                background-color: rgba(120,60,200,100);
        #                                }""")
        
        tool_redo = QPushButton("Redo")
        tool_redo.clicked.connect(his.redo)
        tool_redo.setStyleSheet(tool_undo.styleSheet())
        
        self.right_panel_items.setSpacing(0)
        layout_left.addWidget(tool_undo)
        layout_left.addWidget(tool_redo)
        #tool_label.setStyleSheet("""""")

    def right_panel_items(self):
        layout = QGridLayout(self.right_side_panel)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)
        #layout.setContentsMargins(100,100,100,100)
        layout.setContentsMargins(10,10,10,10)
        #GrayScale
        grayscale_button = QPushButton("Grayscale")
        grayscale_button.clicked.connect(self.grayscale)
        
        #Invert
        invert_button = QPushButton("Invert")
        invert_button.clicked.connect(self.invert)
        invert_button.setStyleSheet(grayscale_button.styleSheet())
        #Sobel
        sobel_button = QPushButton("Sobel")
        sobel_button.clicked.connect(self.sobel)
        sobel_button.setStyleSheet(grayscale_button.styleSheet())
        #Canny
        canny_button = QPushButton("Canny")
        canny_button.clicked.connect(self.canny)
        canny_button.setStyleSheet(grayscale_button.styleSheet())

        sepia_button = QPushButton("Sepia")
        sepia_button.clicked.connect(self.sepia)
        sepia_button.setStyleSheet(grayscale_button.styleSheet())

        cartoon_button = QPushButton("Cartoon")
        cartoon_button.clicked.connect(self.cartoon)
        cartoon_button.setStyleSheet(grayscale_button.styleSheet())

        emboss_button = QPushButton("Emboss")
        emboss_button.clicked.connect(self.emboss)
        emboss_button.setStyleSheet(grayscale_button.styleSheet())


        layout.addWidget(grayscale_button, 0,0)
        layout.addWidget(invert_button, 0,1)
        layout.addWidget(sobel_button,0,2)
        layout.addWidget(canny_button,1,0)
        layout.addWidget(sepia_button,1,1)
        layout.addWidget(cartoon_button,1,2)
        layout.addWidget(emboss_button,2,0)

        #SLIDERS
        brightness_label = QLabel("Brightness")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.valueChanged.connect(self.update_brightness)
        self.brightness_slider.setContentsMargins(10,10,10,10)

        if self.brightness_slider.value != 0:
            self.brightness_apply = QPushButton("Apply")
            self.brightness_apply.setStyleSheet(grayscale_button.styleSheet())
            self.brightness_apply.clicked.connect(self.ie.apply_brightness)
            layout.addWidget(self.brightness_apply, 7,2)


        contrast_label = QLabel("Contrast")
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setMinimum(-100)
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.update_contrast)      

        if self.contrast_slider.value != 0:
            self.contrast_apply = QPushButton("Apply")
            self.contrast_apply.setStyleSheet(grayscale_button.styleSheet())
            self.contrast_apply.clicked.connect(self.ie.apply_contrast)
            layout.addWidget(self.contrast_apply, 8,2)

        

        layout.addWidget(brightness_label,7,0)
        layout.addWidget(self.brightness_slider,7,1)
        layout.addWidget(contrast_label,8,0)
        layout.addWidget(self.contrast_slider,8,1)


        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(self.ie.apply_effect)
        layout.addWidget(apply_button, 14,0)

    def invert(self):
        invert = self.ie.invert()
        if invert:
            self.ie.show_pixmap(invert,self.main_panel) 

    def grayscale(self):
        gray = self.ie.grayScale()
        if gray:
            self.ie.show_pixmap(gray, self.main_panel)
        print("action works")

    def sobel(self):
        sobel = self.ie.sobel()
        if sobel:
            self.ie.show_pixmap(sobel, self.main_panel)

    def canny(self):
        canny = self.ie.canny()
        if canny:
            self.ie.show_pixmap(canny, self.main_panel)

    def sepia(self):
        sepia = self.ie.sepia()
        if sepia:
            self.ie.show_pixmap(sepia, self.main_panel)

    def cartoon(self):
        cartoon = self.ie.cartoon()
        if cartoon:
            self.ie.show_pixmap(cartoon,self.main_panel)

    def emboss(self):
        emboss = self.ie.emboss()
        if emboss:
            self.ie.show_pixmap(emboss,self.main_panel)


    def update_brightness(self):
        brightness = self.brightness_slider
        if brightness:
            value = brightness.value()
            pixmap = self.ie.delta_brightness(value)
            if pixmap:
                self.ie.show_pixmap(pixmap,self.main_panel)

    def update_contrast(self):
        contrast = self.contrast_slider
        if contrast:
            value = contrast.value()
            pixmap = self.ie.delta_contrast(value)
            if pixmap:
                self.ie.show_pixmap(pixmap,self.main_panel)



    def tools_panel_items(self):
        print("Tools Panel Items")

    def save_file(self):
        file_name,_ = QFileDialog.getSaveFileName(self,"Save Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            success = self.ie.save_file(file_name)
            if success:
                print("File Saved", file_name)
            else:
                print("Save failed, kill yourself")

    def import_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")  
        self.ie.numpyImage(file_name)
        if file_name and self.ie.numpy_image is not None:
            pixmap = self.ie.numpy_to_qpixmap(self.ie.numpy_image)
            self.ie.show_pixmap(pixmap, self.main_panel)



    
if __name__ == "__main__":
    ie = importExport()
    his = history()
    app = QApplication(sys.argv)
    window = MainWindow(ie)
    window.show()
    sys.exit(app.exec())
