import argparse
import json
import numpy as np
import cv2 as cv
from pathlib import Path
from barcode import Barcode


parser = argparse.ArgumentParser(prog="filmToBarcode", 
                                 description="CLI that creates a vector image from a film file",
                                 epilog="Thank you for using filmToBarcode! <3",
                                 )


parser.add_argument("-v","--version", action="version", version="filmToBarcode 0.1.0",
                    help="Display the version number of the program")


# Required arguments: path to input file, temp file name, path to output file
parser.add_argument("-i", "--input", required=True, help="Path to the video input file. This is a required argument.")
parser.add_argument("-t", '--temp', help="Name of temporary JSON file in which film data is stored.", type=str)
parser.add_argument("-o", "--output", required=True, help="Name of the output file. If you do not include this file, remember to call the Barcode class appropriately.", type=str)


# Optional arguments: 
# height of the output image
parser.add_argument("-H", "--height", help="Integer value, that determines the height of the output image.", type=int, default=300)

# width of the output image
parser.add_argument("-W", "--width", help="Integer value, that determines the width of the bars in the output image.", type=int, default=1)

# number of frames to skip, this can be used to reduce image widt/reduce no of pixels
parser.add_argument("-S", "--skip", help="This specifies the number of frames to skip. This can also reduce the width of the image file.", type=int, default=0)

# Represents whether to wrap the rectangles around or not
parser.add_argument("--wrap", help="Normally one bar is created. Specify this argument to wrap the rectangles around and create one bar comprised of multiple smaller ones.", action="store_true")








def main(args):

    bc = Barcode(input_file=args['input'])

    bc.avgPixelValues(store_list=True)
    bc.toBarcode(bar_width=1, bar_height=250, file_name=args['output'])
    

    return


if __name__ == "__main__":
    
    args = vars(parser.parse_args())

    if not Path(args['input']).exists():
        parser.exit(1, message="The target input file doesn't exist. Please check your input variables.")
    else:       
        print(args)
        #main(args)

        
    




