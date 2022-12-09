import pyqrcode     # pip install pyqrcode

# strings which represents the QR Code
str = "https://www.amazon.in/Kindle-eBooks/b?ie=UTF8&node=1634753031"

# generate QR code
code_url = pyqrcode.create(str)

# create and save the svg file (allows rendering qrcode in any desired size)
code_url.svg('myqrfile.svg', scale = 8)

# create and save the png file
code_url.png('myqrfile.png', scale = 6)

