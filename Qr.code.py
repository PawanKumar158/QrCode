# Qr Code Genrator Form URL

import qrcode as qr
from PIL import Image

img = qr.make("https://linktr.ee/pawankumar158")

img.save("MyLinkQr.png")
