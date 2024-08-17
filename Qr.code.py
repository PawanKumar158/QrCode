# Qr Code Genrator Form URL

import qrcode as qr
from PIL import Image

# importing gui for take input by user
import GuiQRCode

img = qr.make(input_field)

img.save("MyLinkQr.png")
