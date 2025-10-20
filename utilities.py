
#utilities.py
# from PyQt6.QtWidgets import QFileDialog
import colorsys
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
        self.hsv_image = None;
        self.history = history()

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
        self.original_image = self.numpy_image.copy()
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
            medianBlur = cv.medianBlur(gray,7)
            adpativeThreshold = cv.adaptiveThreshold(medianBlur,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,9)
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

#Blur

    def simple_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        blur = cv.blur(image,(5,5))
        self.numpy_image = blur
        to_pixmap = self.numpy_to_qpixmap(blur)
        return to_pixmap

    def gaussian_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        gaussian = cv.GaussianBlur(image,(7,7),0)
        self.numpy_image = gaussian
        to_pixmap = self.numpy_to_qpixmap(gaussian)
        return to_pixmap

    def median_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        median = cv.medianBlur(image,7)
        self.numpy_image = median
        to_pixmap = self.numpy_to_qpixmap(median)
        return to_pixmap

    def bilateral_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        bilateral = cv.bilateralFilter(image,9,75,75)
        self.numpy_image = bilateral
        to_pixmap = self.numpy_to_qpixmap(bilateral)
        return to_pixmap
    
    def box_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        box = cv.boxFilter(image,-1,(7,7),normalize=True)
        self.numpy_image = box
        to_pixmap = self.numpy_to_qpixmap(box)
        return to_pixmap
        
    def motion_blur(self):
        self.history.push(self.numpy_image)
        image = self.numpy_image

        k_size = 15
        kernel = np.zeros((k_size,k_size))
        kernel[int((k_size-1)/2),:] = np.ones(k_size)
        kernel = kernel/k_size

        motion = cv.filter2D(image,-1,kernel)
        self.numpy_image = motion
        to_pixmap = self.numpy_to_qpixmap(motion)
        return to_pixmap

#TINT

    def delta_tint(self, blue=1.0, green=1.0,red=1.0):
        if self.numpy_image is None:
            return "There are no numpy image"
        
        image = self.numpy_image.copy()

        blue_channel, green_channel, red_channel = cv.split(image)

        blue_channel = cv.add(blue_channel, blue)
        green_channel = cv.add(green_channel, green)
        red_channel = cv.add(red_channel, red)

        blue_channel = np.clip(blue_channel, 0, 255).astype(np.uint8)
        green_channel = np.clip(green_channel, 0, 255).astype(np.uint8)
        red_channel = np.clip(red_channel, 0, 255).astype(np.uint8)

        self.adjusted_preview = cv.merge((blue_channel, green_channel, red_channel))
        return self.numpy_to_qpixmap(self.adjusted_preview)

    def apply_tint(self):
        self.numpy_image = self.adjusted_preview
        return self.numpy_to_qpixmap(self.adjusted_preview)


    def delta_brightness(self, brightness):

        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.copy()

        self.adjusted_preview = cv.convertScaleAbs(image, alpha=1.0, beta=brightness)
        
        return self.numpy_to_qpixmap(self.adjusted_preview)

    def apply_brightness(self):
        self.numpy_image = self.adjusted_preview
        return self.numpy_to_qpixmap(self.adjusted_preview)
    
    def delta_blacks(self, blacks):
        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.astype(np.float32)

        blacks_interp = np.interp(blacks,[0,200],[0,100])
        image = np.clip((image - blacks_interp),0,255)
        self.black_adjusted = image.astype(np.uint8)
        return self.numpy_to_qpixmap(self.black_adjusted)
        
    def apply_blacks(self):
        self.numpy_image = self.black_adjusted
        return self.numpy_to_qpixmap(self.numpy_image) 

    def delta_whites(self, whites):
        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.astype(np.float32)

        whites_interp = np.interp(whites,[0,200],[255,155])
        image = (image-0)*(255.0/whites_interp)
        image = np.clip(image,0,255)
        self.whites_adjusted = image.astype(np.uint8)
        return self.numpy_to_qpixmap(self.whites_adjusted)
        
    def apply_whites(self):
        self.numpy_image = self.whites_adjusted
        return self.numpy_to_qpixmap(self.numpy_image)

    def delta_noise(self, noise):
        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.astype(np.float32)
        #uniform
        noise_interp = np.interp(noise, [0,100],[0,50])
        noise = np.random.normal(0, noise_interp, image.shape)
        image = image + noise
        image = np.clip(image, 0, 255)
        self.noise_adjusted = image.astype(np.uint8)
        return self.numpy_to_qpixmap(self.noise_adjusted)
    
    def delta_noise_uniform(self, noise):
        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.astype(np.float32)
        #uniform
        noise_interp = np.interp(noise, [0,100],[0,50])
        noise = np.random.uniform(5, noise_interp, image.shape)
        image = image + noise
        image = np.clip(image, 0, 255)
        self.noise_adjusted = image.astype(np.uint8)
        return self.numpy_to_qpixmap(self.noise_adjusted)

    def delta_noise_saltpepper(self, noise):
        self.isNumpyImage(self.numpy_image)

        image = self.numpy_image.astype(np.float32)
        #uniform
        noise_interp = np.interp(noise, [0,100],[0,0.05])

        blacks = np.random.rand(*image.shape[:2]) < noise_interp/ 2
        whites = np.random.rand(*image.shape[:2]) < noise_interp/2

        if image.ndim == 3:
            image[blacks] = [255,255,255]
            image[whites] = [0,0,0]
        else:
            image[blacks] = 255
            image[whites] = 0
        
        image = image + noise
        image = np.clip(image, 0, 255)

        self.noise_adjusted = image.astype(np.uint8)

        return self.numpy_to_qpixmap(self.noise_adjusted)  
    def apply_noise(self):
        self.numpy_image = self.noise_adjusted
        return self.numpy_to_qpixmap(self.numpy_image) 

    def delta_hue(self, degree):
        self.isNumpyImage(self.numpy_image)
        image = self.numpy_image.astype(np.float32) / 255.0
        h, w, c = image.shape
        result = np.zeros_like(image)

        hue_shift = degree / 360.0 

        hsv = cv.cvtColor(self.numpy_image, cv.COLOR_RGB2HSV).astype(np.float32)
        hsv[..., 0] = (hsv[..., 0] + degree) % 180  # OpenCV hue range = [0,180)
        hsv = np.clip(hsv, 0, 255).astype(np.uint8)
        self.hue_adjusted = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)

        return self.numpy_to_qpixmap(self.hue_adjusted)
    
    def apply_hue(self):
        self.numpy_image = self.hue_adjusted
        return self.numpy_to_qpixmap(self.hue_adjusted)
    
    def delta_gaussian_falloff(self,strength):
        image = self.numpy_image
        rows, cols = image.shape[:2]
    
        kernel_x = cv.getGaussianKernel(cols, strength)
        kernel_y = cv.getGaussianKernel(rows, strength)
    
        mask = kernel_y * kernel_x.T
        mask = mask / np.max(mask)
    
        vignette = np.empty_like(image)
        for i in range(image.shape[2]):
            vignette[:, :, i] = image[:, :, i] * mask

        self.gaussian_falloff = vignette.astype(np.uint8)

        return self.numpy_to_qpixmap(self.gaussian_falloff)

    def apply_gaussian_falloff(self):
        self.numpy_image = self.gaussian_falloff 
        return self.numpy_to_qpixmap(self.numpy_image)       

    def delta_contrast(self,contrast):
        if self.numpy_image is None:
            return "There are no numpy image"
        
        image = (self.numpy_image.copy().astype(np.float32))/255.0
        con = contrast/100
        image = (image - 0.5) * con + 0.5
        image = np.clip(image,0,1)
        image = (image*255).astype(np.uint8)
        self.con_adjusted = image
        return self.numpy_to_qpixmap(image)      

    def apply_contrast(self):
        self.numpy_image = self.con_adjusted
        return self.numpy_to_qpixmap(self.con_adjusted)

    def isNumpyImage(self, image):
        if image is None:
            return "There are no numpy image"

        
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
    
    def is_hsv(self,image):
        if len(image.shape) == 3 and image.shape[2] == 3:
            hue_max = np.max(image[::0])
            if hue_max <= 179:
                return True
        return False
    
    def clarity(self,amount=1.0):
        sigma=1.0
        threshold=0
        image = self.numpy_image.copy()

        g_blur = cv.GaussianBlur(image,(5,5),sigma)
        sharp = float(amount+1)*image - float(amount)* g_blur

        sharp = np.maximum(sharp, np.zeros(sharp.shape))
        sharp = np.minimum(sharp, np.zeros(sharp.shape))
        sharp = sharp.round().astype(np.uint8)

        if threshold > 0:
            low_contrast = np.absolute(image - g_blur) < threshold
            np.copyto(sharp,image, where=low_contrast)

        self.clar_adjusted_preview = sharp
        return self.numpy_to_qpixmap(self.clar_adjusted_preview)

    def apply_clarity(self):
        self.numpy_image = self.clar_adjusted_preview
        return self.numpy_to_qpixmap(self.clar_adjusted_preview) 

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