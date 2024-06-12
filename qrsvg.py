import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("https://www.youtube.com",image_factory = factory)
svg_img.save("KuKuQR")