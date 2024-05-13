import cv2 as cv
import numpy as np
import json


class Barcode:
    def __init__(self, input_file:str) -> None:
        self.input_file = input_file
        
        

    def getInputFile(self):
        return self.input_file
    
    

    def avgPixelValues(self, skip_frames=1, store_list=False) -> list:
        
        avg_pixels = []
        total_frames = 0

        input_file = self.getInputFile()

        # create video capture object
        cap = cv.VideoCapture(input_file)

        if cap is None:
            print('Error loading the video')
            return
        
        while True:

            # Read video file frame by frame
            ret, frame = cap.read()

            # ret is True if a frame is read
            if not ret:
                print('No longer reading frames. EOF? Exiting...')
                break

            # increment frame counter
            total_frames += 1

            # If total_frames mod skip frames
            # equals 0, it is time to add
            # the average frame value
            # the default is to add all frames
            if total_frames % skip_frames ==0:
                avg_pixel = cv.mean(frame)[:3]
                avg_pixels.append(avg_pixel)
        
        # done with video loop
        # release capture object
        cap.release()

       
        self.avgPixels = avg_pixels

        if store_list:
            return True
        else:
            return False

        
    
    def getAvgPixels(self)-> list:
        try:
            return self.avgPixels
        except AttributeError:
            print('''Barcode object does not have a list of pixel averages yet. 
                  Call method avgPixelValues first with store_list=True''')
            return
    
    @staticmethod
    def toJson(avg_pixels: list, file_name:str) -> None:

       
        with open(file_name, 'w') as f:
            f.write(json.dumps(avg_pixels))

        return
    
    @staticmethod
    def fromJson(file_name:str) -> np.array:

        pixel_avgs = json.loads(open(file_name).read())

        pixel_avgs = np.array(pixel_avgs, dtype="uint8")

        return pixel_avgs
    
    def toBarcode(self, bar_width: int, bar_height:int, file_name:str, line_thickness=-1, pixel_vals=None) -> None:
        pixels = []
        if pixel_vals is None:

            pixels = self.getAvgPixels()
        else:
            pixels = pixel_vals



        barcode = np.zeros((bar_height, len(pixels) * bar_width, 3), dtype="uint8")

        for (i, avg) in enumerate(pixels):
            
            # OpenCV does not recognise numpy arrays
            # need to convert each pixel value to an integer
            b = int(avg[0])
            g = int(avg[1])
            r = int(avg[2])

            # write a rectangle to the current position
            cv.rectangle(barcode, (i * bar_width, 0), ((i+1) * bar_width, bar_height), color=(b, g, r), thickness=line_thickness)
        
        # save the file
        cv.imwrite(file_name, barcode)

        return
    
    








        
    






