# filmToBarcode

## project description

I was browsing Etsy when I noticed that people were selling barcodes generated from popular films. These barcodes consisted of reading the frames of a film, taking the mean pixel values, and generating rectangular bars out of those values. The resulting posters looked really neat: a form of modern art. This inspired me to try my hand at making such a poster of some of the films I like - the resulting images can be printed and spruce up any room they are hung in.

This project contains two main files:

- filmToBarcode.py
- barcode.py

The external dependencies are:

- NumPy
- OpenCV

You can run the project by typing:
python3 filmToBarcode.py --h

This provides you with some help and information about how to run the project. This file currently can generate basic barcodes based on the width and height of the input dimensions. An input and output file need to be specified. The barcode.py file contains the class information. You can import this class if you want to run your own projects.

The current iteration of the project takes the mean pixel value of a frame, and uses this to create the bars. Further extensions and improvements can definetly be made. This is only a first draft.

// vandojo 2024
