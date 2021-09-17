from PIL import  Image

# 按参数将图片进行分割
def crop(*args):
    """
    :param args:
    :return:
    """
    img = Image.open("newresource/imgs/1.png")
    img_list = []
    for i in args:
        croped_img = img.crop(i)
        img_list.append(croped_img)
    return img_list