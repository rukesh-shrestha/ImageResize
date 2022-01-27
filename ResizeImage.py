import cv2

class ResizeImage:
    """
    This class is used to resize the image as per the passed input width and height.
    """

    
   
    def __init__(self,inputFilePath,width,height,outputFilePath):
        """
            This is the constructor of the class. It is invoked automatically when the object is created. 

            @param: inputFilePath (String) This is the image path to be resize.
            @param: width (Interger) This is the width of the image to be resize.
            @param: height (Interger) This is the height of the image to be resize.
            @param: outputFilePath (String) This is the image path to be save after resize.
        """
        self.inputFilePath = inputFilePath
        self.width = width
        self.height = height
        self.outputFilePath = outputFilePath


    
    def __resize(self):
        """
            This is the private method.It has use different opencv method to 
            resize the image according the width and height. 
            This method also show the output image after resize.
        
        """
        try:
            img =cv2.imread(self.inputFilePath)
            width=self.width
            height=self.height
            dimension=(width,height)
            resized=cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
            cv2.imshow('output',resized)
            cv2.imwrite(self.outputFilePath,resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as Exp:
            print("Enter path is not valid.")

    def run(self):
        """
            This method is use to call the private method. It also prints the instruction to quit the output image window.
        """
        print("Press the ESC key in keyboard to quit the program.")
        self.__resize()

if __name__ == '__main__':
    print()
    print("For eg:  inputPath: /home/rukeshshrestha/Pictures/Screenshot_16.png")
    inputFilePath = input("Please enter the file path.")
    print()
    print("For eg:  width: 300")
    width = int(input("Please enter the width of the image to be resize."))
    print()
    print("For eg:  height: 300")
    height = int(input("Please enter the height of the image to be resize."))
    print()
    print("For eg:  outputPath: /home/rukeshshrestha/Pictures/ResizeScreenshot_16.png")
    outputFilePath = input("Please enter the path to save the resize image.")
    
    resize = ResizeImage(inputFilePath, width,height,outputFilePath)
    resize.run()







    


    

