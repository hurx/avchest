import cv2

def match(image, templ):
    res = cv2.matchTemplate(image,templ, cv2.TM_CCOEFF)
    return cv2.minMaxLoc(res)
