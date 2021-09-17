import unittest
from pyzbar import pyzbar
from ...avchest.push import PushStream
from ...avchest.ffprobe import FFprobe
from ...avchest.pyav import PullStream

PUSH_URL = "rtmp://startpush001.elementtest.org/live/test202109172004?txSecret=16be25a7b02f5d0272dfe225c821eec0&txTime=6145D5C2"
PULL_URL_RTMP = "rtmp://startplay001.elementtest.org/live/test202109172004"
# PULL_URL_FLV = ""
# PULL_URL_HLS = ""

PUSH_FILE = "./resources/video/1280_720_30f_1min.mp4"

# 用二维码解析视频画面，解析失败返回 -1
def process(img):
    img_info = pyzbar.decode(img)
    if len(img_info) > 0:
        return int(img_info[0].data.decode("utf-8")),True
    else:
        return -1, True

# 校验列表连续
# step 为允许空缺的帧数，当帧率改变时参考 ffmpeg 抽帧原理指定 step
def check_list(frame_list, step):
    if len(frame_list) <= 1 :
        return False
    prev = frame_list[0]
    error_count = 0
    for i in frame_list[1:]:
        # 连续超过 step 个解析失败
        if error_count >= step:
            return False
        if i != -1:
            if i - prev > 5:
                return False
            prev = i
            error_count = 0
        else:
            error_count += 1
    return True

class TestPushpull(unittest.TestCase):
    def test_pull_push(self):
        # 推流
        self.push_stream = PushStream(PUSH_URL, PUSH_FILE)
        status, err = self.push_stream.status()

        # 校验推流状态
        self.assertTrue(status,err)

        # 拉元信息
        metadata = FFprobe().pull_stream(PULL_URL_RTMP).get_info()
        # todo check metadata

        # 拉取并解析画面
        frame_list = PullStream(PULL_URL_RTMP, timeout=10, process=process).get_frame_list()
        self.assertTrue(check_list(frame_list, 5),"拉取到的视频帧不连续：%s"%frame_list)

    def tearDown(self):
        # 停止推流
        self.push_stream.stop()