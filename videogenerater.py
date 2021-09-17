import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# 生成指定宽、高的二维码图片
def create_qrcode_imgs_in_size(width, height, start_num, end_num, prefix=None, version=3):
    """
    :param width:
    :param height:
    :param start_num:
    :param end_num:
    :param prefix:
    :param version:
    :return:
    """
    # 纯色背景
    back_ground = Image.new("RGBA", (width, height), "White")
    # 生成二维码
    qr = qrcode.QRCode(
        version=version,
    )
    for i in range(start_num, end_num):
        qr.clear()
        if prefix != None:
            data = prefix + str(i)
        else:
            data = str(i)
        qr.add_data(data)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        offset_width = int((back_ground.size[0] - qr_img.size[0])/2)
        offset_hight = int((back_ground.size[1] - qr_img.size[1]) / 2)
        back_ground.paste(qr_img, box=(offset_width, offset_hight))
        file_name = 'example/resources/imgs/' + data + '.png'
        with open(file_name, 'wb') as f:
            back_ground.save(f)

if __name__ == "__main__":
    create_qrcode_imgs_in_size(1280, 720,1,2)
    # result = decode(Image.open('resource/imgs/1.png'))
    # print(result)
