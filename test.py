import qrcode
from PIL import Image

img = qrcode.make("https://example.com")
img.show()  # Should open a QR code image