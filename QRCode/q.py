# Basic Usage
import qrcode as qr
img = qr.make("https://www.hackerrank.com/")
img.save("Hackerrank.jpg")

# Advanced Usage
# from ensurepip import version
# from tkinter import constants
# import qrcode as qr
# qr = qr.QRCode(
#     version= 1,
#     error_correction=qr.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data("https://youtube.com/")
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("Youtube.jpg")