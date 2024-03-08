#QR code (Quick Response code)  is a type of the matrix barcode invented in 1994 by the Japanese automotive company
# Denso Wave. A barcode is a machine-readable optical label that can contain information about the item to which
# it is attached.
#Using Python packages like qrcode, pyqrcode modules we can generate and read the QR codes. In this project, we
# will see how we can generate the QR Codes using python.
#In this project, we will take the link from the user and the basic requirements like name, box size, etc, and
# generate a QRcode with the given information.
#You can generate the QR code and save it in png format.
import os
import platform
import sys


def windows_remove_files():
    filepath = 'C:/Users/bruno/Downloads'
    print(filepath)
    print(os.listdir(filepath))



print("""Python version: %s

system: %s

""" % (
sys.version.split('\n'),
platform.system(),

))

def main():
    if platform.system() == 'Windows':
        windows_remove_files()
