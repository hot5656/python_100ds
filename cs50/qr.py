import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran")
img.save("qr.png", "PNG")
# windows not support
# os.system("open qr.png")