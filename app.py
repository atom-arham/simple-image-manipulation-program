import customtkinter
import tkinter
import os
import shutil
from utilities import ut

class editorClass(customtkinter.CTk):
    window_width = 1280
    window_height = 720
    def __init__(self):
        super().__init__()
        self.geometry(str(self.window_width) +"x"+ str(self.window_height))
        self.title("Ver1.0")
        self.configure(bg_color="#3A0519")
        self.image_label_main_panel = None;
        self.is_imported = False;
        
        self.sidebar = customtkinter.CTkFrame(self,fg_color="#2a202a",
                                              border_color="#483d48",
                                              border_width=1,
                                              corner_radius=15,
                                              width=self.window_width/4)
        self.sidebar.pack(side="bottom",
                          fill="both",
                          padx=5,pady=2.5)

        self.mainPanel = customtkinter.CTkFrame(self,fg_color="#2a202a",
                                                border_color="#483d48",
                                                border_width=1,
                                                corner_radius=15,height=400)
        self.mainPanel.pack(expand=True,side="top",
                            fill="both",
                            padx=5,
                            )
        #oncloseoperation
        
    #def uiPanels(self):
class elements(editorClass):
    def __init__(self):
        super().__init__()
        
    def importButton(self):
        self.importButton = customtkinter.CTkButton(self.sidebar,text="Import",command=self.importedButtonShow,fg_color="#8a2e3f",hover_color="#b1263f",corner_radius=15)
        self.importButton.grid(padx=5,pady=5)    

    def importedButtonShow(self):
        self.imported_image = ut.importImage()
        if self.imported_image:
            self.mainPanelShow(self.imported_image)

    def mainPanelShow(self, image):
        if self.is_imported == True:
            self.image_label_main_panel.destroy()
        self.image_label_main_panel = customtkinter.CTkLabel(self.mainPanel,text="",image=image,compound="center",anchor="center")
        self.image_label_main_panel.pack(padx=10,pady=10,expand=True)
        self.is_imported = True


#Needs Optimisation
    def grayScaleConnect(self):
        show_path, temp_folder=ut.grayScale()
        self.mainPanelShow(show_path)

    def invertConnect(self):
        show_path, temp_folder=ut.invert()
        self.mainPanelShow(show_path)    

    def sobelConnect(self):
        show_path,temp_folder = ut.sobel()
        self.mainPanelShow(show_path)

    def cannyConnect(self):
        show_path,temp_folder = ut.canny()
        self.mainPanelShow(show_path)

    def sepiaConnect(self):
        show_path,temp_folder = ut.sepia()
        self.mainPanelShow(show_path)

    def cartoonConnect(self):
        show_path,temp_folder = ut.cartoon()
        self.mainPanelShow(show_path)

    def pencilgrayConnect(self):
        show_path,temp_folder = ut.pencilgray()
        self.mainPanelShow(show_path)

    def pencilcolorConnect(self):
        show_path,temp_folder = ut.pencilcolor()
        self.mainPanelShow(show_path)

    def embossConnect(self):
        show_path,temp_folder = ut.emboss()
        self.mainPanelShow(show_path)

    def splashConnect(self):
        show_path,temp_folder = ut.emboss()
        self.mainPanelShow(show_path)    

    def duotoneConnect(self):
        show_path,temp_folder = ut.emboss()
        self.mainPanelShow(show_path)

    def features(self):

        #Grayscale Button
        self.grayScaleButton = customtkinter.CTkButton(self.sidebar,text="Grayscale",command=self.grayScaleConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.grayScaleButton.grid(row=0, column=2,padx=5,pady=10)
        #Grayscale Button

        #invert
        self.invertButton = customtkinter.CTkButton(self.sidebar,text="Invert",command=self.invertConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.invertButton.grid(row=0, column=3,pady=10,padx=5)
        #invert

        #sobel
        self.sobelButton = customtkinter.CTkButton(self.sidebar,text="Sobel",command=self.sobelConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.sobelButton.grid(row=0, column=4,pady=10,padx=5)
        #sobel

        #canny
        self.cannyButton = customtkinter.CTkButton(self.sidebar,text="Canny",command=self.cannyConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.cannyButton.grid(row=0, column=5,pady=10,padx=5)
        #canny        

        #sepia
        self.sepiaButton = customtkinter.CTkButton(self.sidebar,text="Sepia",command=self.sepiaConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.sepiaButton.grid(row=0, column=6,pady=10,padx=5)
        #sepia  

        #cartoon
        self.cartoonButton = customtkinter.CTkButton(self.sidebar,text="Cartoon",command=self.cartoonConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.cartoonButton.grid(row=0, column=7,pady=10,padx=5)
        #cartoon  

        #emboss
        self.embossButton = customtkinter.CTkButton(self.sidebar,text="Emboss",command=self.embossConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.embossButton.grid(row=0, column=8,pady=10,padx=5)
        #emboss  

        #pencil
        self.pencilcolorButton = customtkinter.CTkButton(self.sidebar,text="Colour Pencil",command=self.pencilcolorConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.pencilcolorButton.grid(row=0, column=9,pady=10,padx=5)
        #pencil 

        #pencil
        self.pencilsketchButton = customtkinter.CTkButton(self.sidebar,text="Pencil Sketch",command=self.pencilgrayConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.pencilsketchButton.grid(row=0, column=10,pady=10,padx=5)
        #pencil 

        #splash
        self.splashButton = customtkinter.CTkButton(self.sidebar,text="Splash",command=self.splashConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.splashButton.grid(row=0, column=11,pady=10,padx=5)
        #splash
         
        #duo tone
        self.duotoneButton = customtkinter.CTkButton(self.sidebar,text="Duo Tone",command=self.duotoneConnect,fg_color="#3e2730",hover_color="#6e2541",corner_radius=15)
        self.duotoneButton.grid(row=0, column=12,pady=10,padx=5)
        #duo tone
     
temp_folder="temp"
def onCloseOperation():
    if not os.path.exists(temp_folder):
        print("No tempfolder exists")
        elements.destroy()
    else:
        shutil.rmtree(temp_folder)
        elements.destroy()
                        


#editor = editorClass()
elements = elements()

#editor.uiPanels()
elements.importButton()
elements.features()
#editor.mainloop()
elements.protocol("WM_DELETE_WINDOW", onCloseOperation)
elements.mainloop()

# def uiButtons(self):

        

#         def importedImageConnect():
#             imported_image = ut.importImage()
#             if imported_image:
#                mainPanelShowCall(imported_image)
#                self.isImported = True;
    
#         self.importButton = customtkinter.CTkButton(self.sidebar,
#                                                     text="Import",
#                                                     command=importedImageConnect)
#         self.importButton.pack(padx=20,
#                                pady=10)

#         def grayScaleFunctionCall():
#             grayImage, temp_folder_path = ut.grayScale()
#             if grayImage:
#                 mainPanelShowCall(grayImage)
        
#         self.GrayscaleButton = customtkinter.CTkButton(self.sidebar,
#                                                        text="Grayscale",
#                                                        command=grayScaleFunctionCall)
#         self.GrayscaleButton.pack(padx=20,
#                                   pady=10)

#         def mainPanelShowCall(image_Imp):
#             if self.isImported == True:
#                self.image_label_main_panel.destroy()
#             self.image_label_main_panel = customtkinter.CTkLabel(self.mainPanel,text="",image=image_Imp)
#             self.image_label_main_panel.pack(padx=10,pady=10)
#             self.isImported = True;

    
            

#         #Brightness

#         self.BrightnessFrame = customtkinter.CTkFrame(self.sidebar)
#         self.BrightnessText = customtkinter.CTkLabel(self.BrightnessFrame,text="Brightness")
#         self.BrightnessSlider = customtkinter.CTkSlider(self.BrightnessFrame,from_=0,to=100)
#         self.BrightnessSlider.set(50)
#         self.BrightnessFrame.pack(padx=20,pady=10)
#         self.BrightnessText.pack(padx=20,pady=3)
#         self.BrightnessSlider.pack(padx=20,pady=10)

#         if self.BrightnessSlider != 50:
#              self.Apply = customtkinter.CTkButton(self.sidebar,
#                                                     text="Apply",
#                                                     command=brightnessCall)
             
#         def brightnessCall():    
#             brightness = ut.brightness(self.BrightnessSlider.get())
#             mainPanelShowCall(brightness)


#         #Contrast
#         self.ContrastFrame = customtkinter.CTkFrame(self.sidebar)
#         self.ContrastText = customtkinter.CTkLabel(self.ContrastFrame,text="Contrast")
#         self.ContrastSlider = customtkinter.CTkSlider(self.ContrastFrame,from_=0,to=100)
#         self.ContrastFrame.pack(padx=20,pady=10)
#         self.ContrastText.pack(padx=20,pady=3)
#         self.ContrastSlider.pack(padx=20,pady=10)