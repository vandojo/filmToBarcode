# filmToBarcode

A command line interface to create 'barcodes' from the frames of movies.

## Project Description

I was browsing Etsy when I noticed that people were selling barcodes generated from popular films. These barcodes consisted of reading the frames of a film, taking the mean pixel values, and generating rectangular bars out of those values. The resulting posters looked really neat: a form of modern art. This inspired me to try my hand at making such a poster of some of the films I like - the resulting images can be printed and spruce up any room they are hung in.

## Usage

#### dependencies

The project has the following dependencies:

- [NumPy](https://numpy.org/)
- [OpenCV](https://opencv.org/)

#### How to run the project

Once these dependencies are installed, you can begin by cloning the project:

```shell
git clone https://github.com/vandojo/filmToBarcode.git
cd filmToBarcode
```

An input file is required, this is the film you want to convert. An output file is also required, this is the image file that is created. This is done by prefacing the paths to these files with an -i and -o respectively. In the example below the width of each of the bars is set to 2 pixels by typing -W 2, and the height is set to 250 pixels with -H 250.
A film can be converted into a barcode by starting the project like so:

```shell
python3 filmToBarcode.py -i <path_to_film> -o <path_to_output> -H 250 -W 2
```

For more information on other parameters and options type:

```shell
python3 filmToBarcode.py -h
```

This provides you with some help and information about how to run the project.

This file currently can generate basic barcodes based on the width and height of the input dimensions. An input and output file need to be specified. The barcode.py file contains the class information. You can import this class if you want to run your own projects.

The current iteration of the project takes the mean pixel value of a frame, and uses this to create the bars. Further extensions and improvements can definitely be made.

// vandojo 2024
