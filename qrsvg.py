import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make(input("Fill a text or a link >>"),image_factory = factory)
svg_img.save("KuKuQR")