import qrcode
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=5)

qr.add_data(input("Put a link or text >>"))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("myqr.png")