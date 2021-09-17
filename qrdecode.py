from pyzbar import pyzbar
from PIL import Image

# 将图片解析成二维码
def decode(img):
    pyzbar.decode(img)

if __name__ == "__main__":
    img_path = ""
    img = Image.open(img_path)
