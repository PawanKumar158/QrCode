# Qr Code Genrator Form URL

import qrcode as qr
from PIL import Image

img = qr.make("https://www.google.com")

img.save("GoogleQr.png")
