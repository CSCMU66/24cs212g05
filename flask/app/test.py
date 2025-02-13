import qrcode
img = qrcode.make('google.com')
type(img)  # qrcode.image.pil.PilImage
img.save("static/qrcode/test.png")