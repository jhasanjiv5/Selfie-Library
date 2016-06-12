# Selfie Library

The project has 3 main parts as face detection, recognition and barcode detection. For face detection we have used Haar cascade xml file where as for barcode detection it takes help of Zbar librariess. 
One of the major part of the project is face recognition, for which we have referred https://www.raspberrypi.org/forums/viewtopic.php?f=38&t=85755 post; here the post maily uses the sklearn library of python.

The program can be run by just calling "python selfie-lib.py" from raspberry pi terminal.

The project is using picamera with python 2.7 and opencv 3.0.0.

The Raspberry pi 2 model B used for the project is with os as Raspian jessie

The project returns the value of the identified barcode with matching database value. It goes further with detection and recognition of faces (update the folder and file refernces in the programs accordingly).
