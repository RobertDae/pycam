"""
The Pycam module contains various helper functions and classes
used in Computer Vision.

The pycam.VideoCapturePlayer class creates a simple object for 
creating a program with a capture->processs->display cycle.

pycam.filters contains a few different implementations of 
gaussian filters, median filters.

The pycam.camera is a wrapper for an OpenCV camera to be used with Pygame.

"""
# Turn pycam into a python module...
from VideoCapturePlayer import VideoCapturePlayer
from camera import Camera
from conversionUtils import surf2CV, cv2SurfArray, numpyFromSurf, numpyFromOpenCV
from adaptors import Ipl2NumPy, NumPy2Ipl
import objectDetect
from objectDetect import ObjectDetector
import filters




