import qrcode

URL = "https://127.0.0.1:8000"
QRCODE_IMAGE_FILEPATH = "qr.png"

image = qrcode.make(URL)
image.save(QRCODE_IMAGE_FILEPATH)