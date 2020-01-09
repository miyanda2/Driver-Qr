import qrcode
sr = qrcode.make("Hello world")
sr.save("myQr.png")