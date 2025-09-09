import sys 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox,
                               QMenuBar, QMenu, QFrame, QHBoxLayout, QFileDialog, QPushButton, QGridLayout, QSlider)
from PySide6.QtCore import Qt   
from PySide6.QtGui import QAction

from utilities import importExport,history
from themes_stylesheets import darkmode, lightmode

class MainWindow(QMainWindow):
    def __init__(self, ie):
        super().__init__()
        self.ie = ie
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 1280, 720)
        self.ui()     
        self.setStyleSheet(darkmode())

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
        dark_appearance.triggered.connect(self.darkmode_connect)

        light_appearance = QAction("Light", mode_sub_menu)
        light_appearance.triggered.connect(self.lightmode_connect)

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
        self.right_side_panel.setFixedWidth(600)
        self.right_side_panel.setContentsMargins(2,2,2,2)
        #self.right_side_panel.setStyleSheet("background-color: rgba(163,102,255,45);border:none;")
        self.right_panel_items()

        #self.panel_layout.addWidget(self.tools_side_panel)
        self.panel_layout.addWidget(self.main_panel)
        self.panel_layout.addWidget(self.right_side_panel)

    def right_frames(self):
         
        frame = QFrame(self.right_side_panel)
        frame.setFrameShape(QFrame.Shape.NoFrame)
        frame.setStyleSheet("background-color: rgba(163,102,255,255);border:none;")
        self.layout = QVBoxLayout(frame)
        self.right_side_panel.addWidget(self.layout)
        

    def tool_side_panel_items(self):
        layout_left = QVBoxLayout(self.tools_side_panel)  
        layout_left.setContentsMargins(5,5,5,5)
        layout_left.setSpacing(0)

        tool_undo = QPushButton("Undo")
        tool_undo.clicked.connect(his.undo)

        tool_redo = QPushButton("Redo")
        tool_redo.clicked.connect(his.redo)
        tool_redo.setStyleSheet(tool_undo.styleSheet())
        
        self.right_panel_items.setSpacing(0)
        layout_left.addWidget(tool_undo)
        layout_left.addWidget(tool_redo)
        #tool_label.setStyleSheet("""""")

    def right_panel_items(self):
        self.layout = QGridLayout(self.right_side_panel)
        self.layout.setHorizontalSpacing(20)
        self.layout.setVerticalSpacing(20)
        #self.layout.setContentsMargins(100,100,100,100)
        self.layout.setContentsMargins(5,5,5,10)
        #GrayScale
        grayscale_button = QPushButton("Grayscale")
        grayscale_button.setFixedSize(180,35)
        grayscale_button.clicked.connect(self.grayscale)
        
        #Invert
        invert_button = QPushButton("Invert")
        invert_button.setFixedSize(180,35)
        invert_button.clicked.connect(self.invert)
        invert_button.setStyleSheet(grayscale_button.styleSheet())
        #Sobel
        sobel_button = QPushButton("Sobel")
        sobel_button.setFixedSize(180,35)
        sobel_button.clicked.connect(self.sobel)
        sobel_button.setStyleSheet(grayscale_button.styleSheet())
        #Canny
        canny_button = QPushButton("Canny")
        canny_button.setFixedSize(180,35)
        canny_button.clicked.connect(self.canny)
        canny_button.setStyleSheet(grayscale_button.styleSheet())

        sepia_button = QPushButton("Sepia")
        sepia_button.setFixedSize(180,35)
        sepia_button.clicked.connect(self.sepia)
        sepia_button.setStyleSheet(grayscale_button.styleSheet())

        cartoon_button = QPushButton("Cartoon")
        cartoon_button.setFixedSize(180,35)
        cartoon_button.clicked.connect(self.cartoon)
        cartoon_button.setStyleSheet(grayscale_button.styleSheet())

        emboss_button = QPushButton("Emboss")
        emboss_button.setFixedSize(180,35)
        emboss_button.clicked.connect(self.emboss)
        emboss_button.setStyleSheet(grayscale_button.styleSheet())

        blur_frame_1 = QFrame()
        blur_frame_1.setFrameShape(QFrame.Shape.HLine)
        blur_frame_1.setLineWidth(1)
        blur_frame_1.setContentsMargins(0,0,0,0)

        blur_frame_2 = QFrame()
        blur_frame_2.setFrameShape(QFrame.Shape.HLine)
        blur_frame_2.setLineWidth(1)
        blur_frame_2.setContentsMargins(0,0,0,0)

        blur_frame3 = QFrame()
        blur_frame3.setFrameShape(QFrame.Shape.HLine)
        blur_frame3.setLineWidth(1)   
        blur_frame3.setContentsMargins(0,0,0,0)

        blur_layout = QVBoxLayout(blur_frame_1)
        blur_layout.setContentsMargins(0,0,0,0)
        #blur_label = QLabel("Racial Blurs")
        #blur_label.setStyleSheet("font-weight: 600; font-size: 14px;margin:0px;padding:0px;")


        simple_blur = QPushButton("Simple")
        simple_blur.setFixedSize(150,35)
        simple_blur.clicked.connect(self.simple_blur)

        gaussian_blur = QPushButton("Gaussian")
        gaussian_blur.setFixedSize(150,35)
        gaussian_blur.clicked.connect(self.gaussian_blur)

        median_blur = QPushButton("Median")
        median_blur.setFixedSize(150,35)
        median_blur.clicked.connect(self.median_blur)

        bilateral_blur = QPushButton("Bilateral")
        bilateral_blur.setFixedSize(150,35)
        bilateral_blur.clicked.connect(self.bilateral_blur)

        box_filer = QPushButton("Box Filter")
        box_filer.setFixedSize(150,35)
        box_filer.clicked.connect(self.box_blur)

        motion_blur = QPushButton("Motion")
        motion_blur.setFixedSize(150,35)
        motion_blur.clicked.connect(self.motion_blur)


        #self.layout.addWidget(blur_label,5,0)

        self.layout.addWidget(blur_frame_1,4,0,1,3)
        self.layout.addWidget(blur_frame_2,8,0,1,3)
        self.layout.addWidget(blur_frame3,12,0,1,3)

        self.layout.addWidget(grayscale_button, 0,0)
        self.layout.addWidget(invert_button, 0,1)
        self.layout.addWidget(sobel_button,0,2)
        self.layout.addWidget(canny_button,1,0)
        self.layout.addWidget(sepia_button,1,1)
        self.layout.addWidget(cartoon_button,1,2)
        self.layout.addWidget(emboss_button,2,0)

        self.layout.addWidget(simple_blur,6,0)
        self.layout.addWidget(gaussian_blur,6,1)
        self.layout.addWidget(median_blur,6,2)
        self.layout.addWidget(bilateral_blur,7,0)
        self.layout.addWidget(box_filer,7,1)
        self.layout.addWidget(motion_blur,7,2)

        #brightness
        brightness_label = QLabel("Brightness")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setMinimum(-100)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.valueChanged.connect(self.update_brightness)
        
        self.brightness_apply = QPushButton("Apply")
        self.brightness_apply.setVisible(False)
        self.brightness_apply.setStyleSheet(grayscale_button.styleSheet())
        self.brightness_apply.clicked.connect(self.ie.apply_brightness)
        self.layout.addWidget(self.brightness_apply, 9,2)
        #brightness

        #contrast
        contrast_label = QLabel("Contrast")
        self.contrast_slider = QSlider(Qt.Horizontal)
        self.contrast_slider.setMinimum(-100)
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.update_contrast)      

        self.contrast_apply = QPushButton("Apply")
        self.contrast_apply.setVisible(False)
        self.contrast_apply.setStyleSheet(grayscale_button.styleSheet())
        self.contrast_apply.clicked.connect(self.ie.apply_contrast)
        self.layout.addWidget(self.contrast_apply, 10,2)
        #contrast

        #hue
        hue_label = QLabel("Hue")
        self.hue_slider = QSlider(Qt.Horizontal)
        self.hue_slider.setMinimum(0)
        self.hue_slider.setMaximum(255)
        self.hue_slider.setValue(0)
        self.hue_slider.valueChanged.connect(self.update_contrast)       

        
        self.hue_apply = QPushButton("Apply")
        self.hue_apply.setVisible(False)
        self.hue_apply.setStyleSheet(grayscale_button.styleSheet())
        self.hue_apply.clicked.connect(self.ie.apply_contrast)
        self.layout.addWidget(self.hue_apply, 11,2)
        #hue

#Red Green Blue Sliders
        red_label = QLabel("Red")
        self.red_slider = QSlider(Qt.Horizontal)
        self.red_slider.setMinimum(-100)
        self.red_slider.setMaximum(100)
        self.red_slider.setValue(0)
        self.red_slider.valueChanged.connect(self.tint_connect)
        self.red_slider.setContentsMargins(0,0,0,0)

        if self.red_slider.value != 0:
            self.red_apply = QPushButton("Apply")
            self.red_apply.setStyleSheet(grayscale_button.styleSheet())
            self.red_apply.clicked.connect(self.ie.apply_brightness)
            self.layout.addWidget(self.brightness_apply, 13,2)

        blue_label = QLabel("Blue")
        self.blue_slider = QSlider(Qt.Horizontal)
        self.blue_slider.setMinimum(-100)
        self.blue_slider.setMaximum(100)
        self.blue_slider.setValue(0)
        self.blue_slider.valueChanged.connect(self.tint_connect)      

        if self.blue_slider.value != 0:
            self.blue_apply = QPushButton("Apply")
            self.blue_apply.setStyleSheet(grayscale_button.styleSheet())
            self.blue_apply.clicked.connect(self.ie.apply_contrast)
            self.layout.addWidget(self.contrast_apply, 14,2)

        green_label = QLabel("Green")
        self.green_slider = QSlider(Qt.Horizontal)
        self.green_slider.setMinimum(0)
        self.green_slider.setMaximum(255)
        self.green_slider.setValue(0)
        self.green_slider.valueChanged.connect(self.tint_connect)       

        if self.green_slider.value != 0:
            self.green_apply = QPushButton("Apply")
            self.green_apply.setStyleSheet(grayscale_button.styleSheet())
            self.green_apply.clicked.connect(self.ie.apply_contrast)
            self.layout.addWidget(self.hue_apply, 15,2)

        self.layout.addWidget(brightness_label,9,0)
        self.layout.addWidget(self.brightness_slider,9,1)

        self.layout.addWidget(contrast_label,10,0)
        self.layout.addWidget(self.contrast_slider,10,1)

        self.layout.addWidget(hue_label,11,0)
        self.layout.addWidget(self.hue_slider,11,1)

        self.layout.addWidget(red_label,13,0)
        self.layout.addWidget(self.red_slider,13,1)

        self.layout.addWidget(blue_label,14,0)
        self.layout.addWidget(self.blue_slider,14,1)

        self.layout.addWidget(green_label,15,0)
        self.layout.addWidget(self.green_slider,15,1)

        self.layout.setRowMinimumHeight(0,0)
        self.layout.setVerticalSpacing(5)


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

    def simple_blur(self):
        simple = self.ie.simple_blur()
        if simple:
            self.ie.show_pixmap(simple,self.main_panel)
    
    def gaussian_blur(self):
        gaussian = self.ie.gaussian_blur()
        if gaussian:
            self.ie.show_pixmap(gaussian,self.main_panel)
        
    def median_blur(self):
        median = self.ie.median_blur()
        if median:
            self.ie.show_pixmap(median,self.main_panel)

    def bilateral_blur(self):
        bilateral = self.ie.bilateral_blur()
        if bilateral:
            self.ie.show_pixmap(bilateral,self.main_panel)

    def box_blur(self):
        box = self.ie.box_blur()
        if box:
            self.ie.show_pixmap(box,self.main_panel)

    def motion_blur(self):
        motion = self.ie.motion_blur()
        if motion:
            self.ie.show_pixmap(motion,self.main_panel)
            



    def update_brightness(self):
        brightness = self.brightness_slider
        self.brightness_apply.setVisible(True)
        if brightness:
            value = brightness.value()
            pixmap = self.ie.delta_brightness(value)
            if pixmap:
                self.ie.show_pixmap(pixmap,self.main_panel)

    def update_contrast(self):
        contrast = self.contrast_slider
        self.contrast_apply.setVisible(True)
        if contrast:
            value = contrast.value()
            pixmap = self.ie.delta_contrast(value)
            if pixmap:
                self.ie.show_pixmap(pixmap,self.main_panel)

    def update_hue(self):
        self.hue_apply.setVisible(True)
        pass

    def tint_connect(self):
        pass


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

    def darkmode_connect(self):
        self.setStyleSheet(darkmode())

    def lightmode_connect(self):
        self.setStyleSheet(lightmode())

    
if __name__ == "__main__":

    ie = importExport()
    his = history()
    app = QApplication(sys.argv)
    window = MainWindow(ie)
    window.show()
    sys.exit(app.exec())
