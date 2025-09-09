import sys 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QScrollArea,QComboBox,
                               QMenuBar, QToolButton,QMenu, QFrame, QHBoxLayout, QFileDialog, QPushButton, QGridLayout, QSlider, QTabWidget)
from PySide6.QtCore import Qt, QSize   
from PySide6.QtGui import QAction, QIcon

from utilities import importExport,history
from themes_stylesheets import darkmode, lightmode

class MainWindow(QMainWindow):
    def __init__(self, ie):
        super().__init__()
        self.ie = ie
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 1280, 720)
        #self.ui()     
        self.setStyleSheet(darkmode())

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.main_layout = QVBoxLayout(self.central)


        self.menubar()
        self.ui()

    def menubar(self):
        menu_bar = QMenuBar(self)

        import_menu = QAction("Import", self)
        save_menu = QAction("Save", self)
        apprearance_menu = QMenu("Appearance", self)
        undo_menu = QAction("Undo", self)
        redo_menu = QAction("Redo", self)

        apprearance_menu.addAction("Dark Mode", self.darkmode_connect)
        apprearance_menu.addAction("Light Mode", self.lightmode_connect)

        import_menu.triggered.connect(self.import_file)
        save_menu.triggered.connect(self.save_file)

        menu_bar.addAction(import_menu)
        menu_bar.addAction(save_menu)  
        menu_bar.addMenu(apprearance_menu) 
        menu_bar.addAction(undo_menu)
        menu_bar.addAction(redo_menu)
        
        self.setMenuBar(menu_bar)

    def ui(self):

        #Frame
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.NoFrame)
        frame.setLineWidth(0)

        middle_layout = QHBoxLayout(frame)
        left_layout = QVBoxLayout()

        #Main Layout
        self.main_layout.addWidget(frame)

        #Main Panel --> display image 
        self.main_panel = QLabel()
        self.main_panel.setMinimumSize(640, 480)
        
        left_layout.addWidget(self.main_panel,7)

        #Filter Panel --> Filters are kept
        self.filter_panel = QFrame()
        self.filter_panel.setFixedHeight(200)
        

        self.filter_layout = QVBoxLayout(self.filter_panel)
        left_layout.addWidget(self.filter_panel,1)

        #Tab widget
        self.filter_tabs = QTabWidget()
        self.filter_tabs.addTab(self.filter_items(), "Filters")
        self.filter_tabs.addTab(self.blur_items(), "Blurs")

        self.filter_layout.addWidget(self.filter_tabs)
        #left_layout.addWidget(self.filter_tabs)

        #Right Panel --> Adjustments are kept
        self.right_panel = QWidget()
        self.right_panel.setFixedWidth(450)
        
        self.right_layout = QGridLayout(self.right_panel)
        #Right Panel End

        middle_layout.addLayout(left_layout,3)
        middle_layout.addWidget(self.right_panel,1)

        #Setting Object Names for Stylesheet
        self.main_panel.setObjectName("main_panel")
        self.filter_panel.setObjectName("filter_panel")
        self.right_panel.setObjectName("right_panel")

        self.main_layout.addLayout(middle_layout,1)
        self.right_panel_items()

    def filter_items(self):
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        container = QWidget()
        horizontal_layout = QHBoxLayout(container)         

        invert_button = QToolButton()
        invert_button.setIcon(QIcon(r"image-editor\filter_previews\invert.jpg"))
        invert_button.setIconSize(QSize(80, 80))
        invert_button.setText("Invert")
        invert_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        invert_button.setFixedSize(100, 105)
        invert_button.clicked.connect(self.invert)

        grayscale_button = QToolButton()
        grayscale_button.setIcon(QIcon(r"image-editor\filter_previews\grayscale.jpg"))
        grayscale_button.setIconSize(QSize(80, 80))
        grayscale_button.setText("Grayscale")
        grayscale_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        grayscale_button.setFixedSize(100, 105)
        grayscale_button.clicked.connect(self.grayscale)

        sobel_button = QToolButton()
        sobel_button.setIcon(QIcon(r"image-editor\filter_previews\sobel.jpg"))
        sobel_button.setIconSize(QSize(80, 80))
        sobel_button.setText("Sobel")
        sobel_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        sobel_button.setFixedSize(100,105)
        sobel_button.clicked.connect(self.sobel)

        sepia_button = QToolButton()
        sepia_button.setIcon(QIcon(r"image-editor\filter_previews\sepia.jpg"))
        sepia_button.setIconSize(QSize(80, 80))
        sepia_button.setText("Sepia")
        sepia_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        sepia_button.setFixedSize(100,105)
        sepia_button.clicked.connect(self.sepia)
        

        cartoon_button = QToolButton()
        cartoon_button.setIcon(QIcon(r"image-editor\filter_previews\cartoon.jpg"))
        cartoon_button.setIconSize(QSize(80, 80))
        cartoon_button.setText("Cartoon")
        cartoon_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        cartoon_button.setFixedSize(100,105)
        cartoon_button.clicked.connect(self.cartoon)
        

        emboss_button = QToolButton()
        emboss_button.setIcon(QIcon(r"image-editor\filter_previews\emboss.jpg"))
        emboss_button.setIconSize(QSize(80, 80))
        emboss_button.setText("Emboss")
        emboss_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        emboss_button.setFixedSize(100,105)
        emboss_button.clicked.connect(self.emboss)
        
        horizontal_layout.addWidget(invert_button)
        horizontal_layout.addWidget(grayscale_button)
        horizontal_layout.addWidget(sobel_button)
        horizontal_layout.addWidget(sepia_button)
        horizontal_layout.addWidget(cartoon_button)
        horizontal_layout.addWidget(emboss_button)


        scroll_area.setWidget(container)
        #self.filter_layout.addWidget(scroll_area)
        return scroll_area

    def blur_items(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        #scroll_area.setFixedHeight(200)
        #scroll_area.setAlignment(Qt.AlignmentFlag.AlignTop)

        container = QWidget()
        vertical_layout = QHBoxLayout(container)  
       
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

        vertical_layout.addWidget(simple_blur)
        vertical_layout.addWidget(gaussian_blur)
        vertical_layout.addWidget(median_blur)
        vertical_layout.addWidget(bilateral_blur)
        vertical_layout.addWidget(box_filer)
        vertical_layout.addWidget(motion_blur)

        scroll_area.setWidget(container)
        #self.right_layout.addWidget(scroll_area, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)
        return scroll_area

    def right_panel_items(self):
        self.right_layout.setContentsMargins(25,25,25,25)
        brightness_label, self.brightness_slider, self.brightness_apply = self.slider_function("Brightness",100,-100,0,self.update_brightness,0)

        self.right_layout.addWidget(brightness_label,0,0)
        self.right_layout.addWidget(self.brightness_slider ,0,1)
        self.right_layout.addWidget(self.brightness_apply ,0,2)

        #self.right_layout.addWidget(brightness_label)

        contrast_label, self.contrast_slider, self.contrast_apply = self.slider_function("Contrast",255,-255,0,self.update_contrast,1)
        self.right_layout.addWidget(contrast_label,1,0)
        self.right_layout.addWidget(self.contrast_slider ,1,1)
        self.right_layout.addWidget(self.contrast_apply ,1,2)

        hue_label, self.hue_slider, self.hue_apply = self.slider_function("Hue -> not implemented ",180,-180,0,self.update_hue,2)
        self.right_layout.addWidget(hue_label,2,0)
        self.right_layout.addWidget(self.hue_slider ,2,1)
        self.right_layout.addWidget(self.hue_apply ,2,2)

        gamma_label, self.gamma_slider, self.gamma_apply = self.slider_function("Gamma",180,-180,0,self.update_hue,2)
        self.right_layout.addWidget(gamma_label,3,0)
        self.right_layout.addWidget(self.gamma_slider ,3,1)
        self.right_layout.addWidget(self.gamma_apply ,3,2)

        clarity_label, self.clarity_slider, self.clarity_apply = self.slider_function("Clarity -> not impemented",180,-180,0,self.update_clarity,2)
        self.right_layout.addWidget(clarity_label,4,0)
        self.right_layout.addWidget(self.clarity_slider ,4,1)
        self.right_layout.addWidget(self.clarity_apply ,4,2)        
        # brightness_label = QLabel("Brightness")
        # self.brightness_slider = QSlider(Qt.Horizontal)
        # self.brightness_slider.setMinimum(-100)
        # self.brightness_slider.setMaximum(100)
        # self.brightness_slider.setValue(0)
        # self.brightness_slider.valueChanged.connect(self.update_brightness)

        # self.brightness_apply = QPushButton("Apply")
        # self.brightness_apply.setVisible(False)
        # self.brightness_apply.clicked.connect(self.ie.apply_brightness)
        # self.right_layout.addWidget(self.brightness_apply, 0,2)

        # self.right_layout.addWidget(brightness_label,0,0)
        # self.right_layout.addWidget(self.brightness_slider,0,1)

        # contrast_label = QLabel("Contrast")
        # self.contrast_slider = QSlider(Qt.Horizontal)
        # self.contrast_slider.setMinimum(-100)
        # self.contrast_slider.setMaximum(100)
        # self.contrast_slider.setValue(0)
        # self.contrast_slider.valueChanged.connect(self.update_contrast)

        # self.contrast_apply = QPushButton("Apply")
        # self.contrast_apply.setVisible(False)
        # self.contrast_apply.clicked.connect(self.ie.apply_contrast)
        # self.right_layout.addWidget(self.contrast_apply, 1,2)

        # self.right_layout.addWidget(contrast_label,1,0)
        # self.right_layout.addWidget(self.contrast_slider,1,1)

    def slider_function(self,label,max,min,default,connect_call,row):
        label = QLabel(label)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setValue(default)
        slider.valueChanged.connect(connect_call)

        slider_apply = QPushButton("Apply")
        slider_apply.setVisible(True)
        slider_apply.clicked.connect(connect_call)


        #label_add = self.right_layout.addWidget(label,row,0)
        #slider_add = self.right_layout.addWidget(slider,row,1)
        #apply_add = self.right_layout.addWidget(slider_apply,row,2)

        return label, slider, slider_apply

    def line(self):
        blur_frame_1 = QFrame()
        blur_frame_1.setFrameShape(QFrame.Shape.HLine)
        blur_frame_1.setLineWidth(1)
        blur_frame_1.setContentsMargins(0,0,0,0)

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

    def update_clarity(self):
        clar = self.clarity_slider
        self.clarity_apply.setVisible(True)
        if clar:
            value = clar.value()
            pixmap = self.ie.clarity(value)
            if pixmap:
                self.ie.show_pixmap(pixmap,self.main_panel)


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
