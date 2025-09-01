
#utilities.py
# from PyQt6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
import cv2 as cv
import numpy as np

class importExport:
    def __init__(self):
        super().__init__()
        self.file = None
        self.numpy_image = None;
        self.history = history()
        self.base_brightness_image = None

        #brightness stuff
        self.previous_brightness = None;

    def save_file(self, path):
        if self.numpy_image is not None and path:
            cv.imwrite(path,self.numpy_image)
            return True
        return False

    def show_pixmap(self, pixmap, panel: QLabel):
        if isinstance(pixmap, QPixmap) and not pixmap.isNull():
            panel_size = panel.size()

            if int(panel_size.width()) or int(panel_size.height() <= 800):
                scaled_width = int(panel_size.width() * 1)
                scaled_height = int(panel_size.height() * 1)
            else:                
                scaled_width = int(panel_size.width() * 0.5)
                scaled_height = int(panel_size.height() * 0.5)
            
            scaled_pixmap = pixmap.scaled(scaled_width, scaled_height, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            panel.setPixmap(scaled_pixmap)
            panel.setScaledContents(False)
            panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            print("Pixmap Displayed")
        else:
            print("Cannot set pixmap.")
        
    def numpyImage(self, file_path):
        self.numpy_image = cv.imread(file_path)
        self.base_brightness_image = self.numpy_image.copy()


    def grayScale(self):
        self.history.push(self.numpy_image)

        if len(self.numpy_image.shape) == 3 and self.numpy_image.shape[2] == 3:  
            grayscale_conversion = cv.cvtColor(self.numpy_image, cv.COLOR_BGR2GRAY)
            self.numpy_image = grayscale_conversion
        else:
            grayscale_conversion = self.numpy_image
        self.numpy_image = grayscale_conversion
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(grayscale_conversion)

    def invert(self):
        self.history.push(self.numpy_image)
        invert_conversion = cv.bitwise_not(self.numpy_image)
        self.numpy_image = invert_conversion
        self.base_brightness_image = self.numpy_image.copy()
        invert_to_pixmap = self.numpy_to_qpixmap(invert_conversion)
        return invert_to_pixmap

    def sobel(self):
        self.history.push(self.numpy_image)      

        image = self.numpy_image  
        #np_image = np.array(image) 
        scale = 1
        delta= 0
        depth=cv.CV_16S
        #sobel operations
        gradient_x = cv.Sobel(image, depth,1,0,ksize=3,scale=scale,delta=delta,borderType=cv.BORDER_DEFAULT)
        gradient_y = cv.Sobel(image, depth,0,1,ksize=3,scale=scale,delta=delta,borderType=cv.BORDER_DEFAULT)

        axis_x_sobel = cv.convertScaleAbs(gradient_x)
        axis_y_sobel = cv.convertScaleAbs(gradient_y)

        sobel = cv.addWeighted(axis_x_sobel,0.5,axis_y_sobel,0.5,0)
        #sobel operations
        self.numpy_image = sobel
        self.base_brightness_image = self.numpy_image.copy()
        sobel_to_pixmap = self.numpy_to_qpixmap(sobel)
        return sobel_to_pixmap

    def canny(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image   
        canny = cv.Canny(image,100,200)
        self.numpy_image = canny
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(canny) # <- converts to Qpixmap and then retuns

    def sepia(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        if len(image.shape) == 2:
            cvtUint8 = image
        else:      
            cvtFloat = np.array(image,dtype=np.float64)

            transformed = cv.transform(cvtFloat,np.matrix([[0.272,0.534,0.131],
                                                        [0.349,0.686,0.168],
                                                        [0.393,0.769,0.189]]))
            transformed[np.where(transformed > 255)] = 255

            cvtUint8 = np.array(transformed, dtype=np.uint8)

        self.numpy_image = cvtUint8
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(cvtUint8)   
    
    def cartoon(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        if len(image.shape) == 2:
            construct = image
        else:
            gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
            medianBlur = cv.medianBlur(gray,5)
            adpativeThreshold = cv.adaptiveThreshold(medianBlur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,7)
            edges = cv.edgePreservingFilter(image,flags=2,sigma_s=150,sigma_r=0.75) 
            construct = cv.bitwise_and(edges,edges,mask=adpativeThreshold)
        self.numpy_image = construct
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(construct)   
    
    def emboss(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        if len(image.shape) == 2:
            empty_image = image
        else:
            gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

            height,width = gray.shape[:2]

            y = np.ones((height,width),np.uint8)*128
            empty_image = np.zeros((height,width),np.uint8)

            bottom_left = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
            bottom_right = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

            emboss_bottom_left = cv.add(cv.filter2D(gray,-1,bottom_left),y)
            emboss_bottom_right = cv.add(cv.filter2D(gray,-1,bottom_right),y)

            for i in range(height):
                for j in range(width):
                    empty_image[i,j] = max(emboss_bottom_left[i,j],emboss_bottom_right[i,j])
        
        self.numpy_image = empty_image  
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(empty_image)   


    def delta_brightness(self, brightness):

        if self.numpy_image is None:
            return "There are no numpy image"
        
        image = self.numpy_image.copy()

        self.adjusted_preview = cv.convertScaleAbs(image, alpha=1.0, beta=brightness)
        return self.numpy_to_qpixmap(self.adjusted_preview)
    


    def apply_brightness(self):
        self.numpy_image = self.adjusted_preview
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(self.adjusted_preview)
    
    
    def apply_effect(self):
        self.history.push(self.numpy_image)

    def delta_contrast(self,contrast):
        print("Applied")
        self.history.push(self.numpy_image)

        if self.numpy_image is None:
            return "There are no numpy image"
        
        image = self.numpy_image.copy()

        alpha = 1.0 + (contrast/100.0)
        self.con_adjusted = cv.convertScaleAbs(image, alpha=alpha, beta=0)
        return self.numpy_to_qpixmap(self.con_adjusted)      

    def apply_contrast(self):
        self.numpy_image = self.con_adjusted
        self.base_brightness_image = self.numpy_image.copy()
        return self.numpy_to_qpixmap(self.con_adjusted)


    def undo(self):
        self.numpy_image = self.history.undo(self.numpy_image)
        return self.numpy_to_qpixmap(self.numpy_image)

    def redo(self):
        self.numpy_image = self.history.redo(self.numpy_image)
        return self.numpy_to_qpixmap(self.numpy_image)

    def numpy_to_qpixmap(self, np_img):
        """Convert NumPy image to QPixmap (supports gray, RGB, BGR)."""
        if len(np_img.shape) == 2:  # grayscale
            h, w = np_img.shape
            bytes_per_line = w
            qimg = QImage(np_img.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
            return QPixmap.fromImage(qimg)

        if np_img.shape[2] == 3:  # BGR
            h, w, ch = np_img.shape
            bytes_per_line = ch * w
            rgb_image = cv.cvtColor(np_img, cv.COLOR_BGR2RGB)
            qimg = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            return QPixmap.fromImage(qimg)

        if np_img.shape[2] == 4:  # RGBA
            h, w, ch = np_img.shape
            bytes_per_line = ch * w
            qimg = QImage(np_img.data, w, h, bytes_per_line, QImage.Format_RGBA8888)
            return QPixmap.fromImage(qimg)

        raise ValueError("Unsupported image format")
    
class history:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def push(self, image):
        if image is not None:
            self.undo_stack.append(image.copy())
            self.redo_stack.clear()

    def undo(self, current):
        if self.undo_stack:
            self.redo_stack.append(current.copy())
            return self.undo_stack.pop()
        return current
    
    def redo(self, current):
        if self.redo_stack:
            self.undo_stack.append(current.copy())
            return self.redo_stack.pop()
        return current
    
        


ie = importExport()

