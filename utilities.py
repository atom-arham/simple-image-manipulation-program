import cv2 as cv
import numpy as np
from tkinter import filedialog
from PIL import Image
import customtkinter
import os
from tkinter import messagebox



class utilities:
    def __init__(self):
        self.original_image_path = None
        self.temp_image_path = None
        self.__temp_folder="temp"
        self.file_extension = None

    def importImage(self):
        if os.path.isdir(self.__temp_folder):
            print("Temp folder already exists. Don't worry")
        else:
            os.mkdir(self.__temp_folder)
    
        fileLocation = filedialog.askopenfilename(initialdir="C:*",
                                                  title="Select a File",
                                                  filetypes=(("All Files","*.*"),("PNG Files","*.png"),("JPG Files","*.jpg")))

        if not fileLocation:
            return "No Image Imported"        
        else:
            self.original_image_path = fileLocation
            self.temp_image_path = self.saveToTempFolder(self.original_image_path) #original_image_path = String
            print(f'Original Path: {self.original_image_path} <- Thats the original path')
            print(f'Temporary Path: {self.temp_image_path} <- Image has been saved here')            
            return self.ShowOnFrame(self.temp_image_path)
        

    
    def saveToTempFolder(self,image_path=None,image=None):
        output_folder = self.__temp_folder

        if image_path is not None:
            imread_path = cv.imread(image_path)
            self.file_extension = os.path.splitext(image_path)[1]
            output_filename = "temp_image" + self.file_extension
            constructed_path = os.path.join(output_folder,output_filename)
            cv.imwrite(constructed_path,imread_path)
            return constructed_path  
        
        elif image is not None and self.file_extension is not None:
            message = "processed_image"
            #self.file_extension = os.path.splitext(image_path)[1]
            output_filename = message + self.file_extension
            constructed_path = os.path.join(output_folder,output_filename)
            cv.imwrite(constructed_path,image)
            return constructed_path
        else:
            return "image not saved"

    def ShowOnFrame(self,image):
        image_path = Image.open(image)
        height,width,channel,ratio = self.imageAttribute(image)
        image_show = customtkinter.CTkImage(light_image=image_path,dark_image=image_path,size=(int(width),int(height)))
        return image_show

    def imageAttribute(self,image):
        img = cv.imread(image)
        height = img.shape[0]
        width = img.shape[1]
        channel = img.shape[2]
        ratio = 0.5
        return height*ratio,width*ratio,channel,ratio
    
    # Block Ends

    def grayScale(self):
        read = cv.imread(self.temp_image_path, 0)
        temp_folder = self.saveToTempFolder(image=read)
        show_path = self.ShowOnFrame(temp_folder)
        return show_path, temp_folder

    def invert(self):
        read = cv.imread(self.temp_image_path)
        inverted = cv.bitwise_not(read)
        temp_folder = self.saveToTempFolder(image=inverted)
        show_path = self.ShowOnFrame(temp_folder)
        return show_path,temp_folder
    
    def sobel(self):
        scale = 1
        delta= 0
        depth=cv.CV_16S
        read = cv.imread(self.temp_image_path)
        #sobel operations
        gradient_x = cv.Sobel(read, depth,1,0,ksize=3,scale=scale,delta=delta,borderType=cv.BORDER_DEFAULT)
        gradient_y = cv.Sobel(read, depth,0,1,ksize=3,scale=scale,delta=delta,borderType=cv.BORDER_DEFAULT)

        axis_x_sobel = cv.convertScaleAbs(gradient_x)
        axis_y_sobel = cv.convertScaleAbs(gradient_y)

        sobel = cv.addWeighted(axis_x_sobel,0.5,axis_y_sobel,0.5,0)
        #sobel operations
        temp_folder = self.saveToTempFolder(image=sobel)
        show_path = self.ShowOnFrame(temp_folder)

        return show_path,temp_folder
    
    def canny(self):
        read = cv.imread(self.temp_image_path)   
        canny = cv.Canny(read,100,200)
        temp_folder = self.saveToTempFolder(image=canny)
        show_path = self.ShowOnFrame(temp_folder)
        return show_path,temp_folder

    def sepia(self):
        read = cv.imread(self.temp_image_path) 
        
        cvtFloat = np.array(read,dtype=np.float64)

        transformed = cv.transform(cvtFloat,np.matrix([[0.272,0.534,0.131],
                                                     [0.349,0.686,0.168],
                                                     [0.393,0.769,0.189]]))
        transformed[np.where(transformed > 255)] = 255

        cvtUint8 = np.array(transformed, dtype=np.uint8)

        temp_folder = self.saveToTempFolder(image=cvtUint8)
        show_path = self.ShowOnFrame(temp_folder)     
        return show_path,temp_folder     

    def cartoon(self):
        read = cv.imread(self.temp_image_path)
        readG = cv.imread(self.temp_image_path,0)
        medianBlur = cv.medianBlur(read,5)
        adpativeThreshold = cv.adaptiveThreshold(readG,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,7)

        edges = cv.edgePreservingFilter(read,flags=2,sigma_s=150,sigma_r=0.75)
        
        construct = cv.bitwise_and(edges,edges,mask=adpativeThreshold)

        temp_folder = self.saveToTempFolder(image=construct)
        show_path = self.ShowOnFrame(temp_folder)     
        return show_path,temp_folder     

    def emboss(self):
        read = cv.imread(self.temp_image_path)
        readG = cv.imread(self.temp_image_path,0)

        height,width = readG.shape[:2]

        y = np.ones((height,width),np.uint8)*128
        empty_image = np.zeros((height,width),np.uint8)

        bottom_left = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
        bottom_right = np.array([[-1,0,1],[-1,0,1],[0,1,1]])

        emboss_bottom_left = cv.add(cv.filter2D(readG,-1,bottom_left),y)
        emboss_bottom_right = cv.add(cv.filter2D(readG,-1,bottom_right),y)

        for i in range(height):
            for j in range(width):
                empty_image[i,j] = max(emboss_bottom_left[i,j],emboss_bottom_right[i,j])
        
        temp_folder = self.saveToTempFolder(image=empty_image)
        show_path = self.ShowOnFrame(temp_folder)     
        return show_path,temp_folder  

    def pencilgray(self):
        read = cv.imread(self.temp_image_path)
        gray,colour = cv.pencilSketch(read,sigma_s=50,sigma_r=0.07,shade_factor=0.05)
        temp_folder = self.saveToTempFolder(image=gray)
        show_path = self.ShowOnFrame(temp_folder)     
        return show_path,temp_folder  

    def pencilcolor(self):
        read = cv.imread(self.temp_image_path)
        gray,colour = cv.pencilSketch(read,sigma_s=50,sigma_r=0.07,shade_factor=0.05)
        temp_folder = self.saveToTempFolder(image=colour)
        show_path = self.ShowOnFrame(temp_folder)     
        return show_path,temp_folder


    # def brightness(self, brightness_value):
    #     read = cv.imread(self.temp_image_path)
    #     if read is None:
    #         print("No Image Found")
    #         return None, None
    #     brightness_change = cv.convertScaleAbs(read,alpha=1.0,beta=float(brightness_value))
    #     rgb = cv.cvtColor(brightness_change, cv.COLOR_BGR2RGB)
    #     save = self.saveToTempFolder(image=rgb)
    #     show_path = self.ShowOnFrame(save)
    #     return show_path, save



            
ut = utilities()
