import  unittest
from pyzbar import pyzbar
from pyav import PullStream

def process(img):
    return pyzbar.decode(img),True

def process2(img):
    img_info = pyzbar.decode(img)
    num = int(img_info[0].data.decode("utf-8"))
    if num < 10010:
        return num , True
    return num , False

class TestPyav(unittest.TestCase):
    @unittest.skip
    def test_local_file(self):
        file_url = "resources/video/1280_720_30f_1min.mp4"
        time_out = 1
        pull_stream = PullStream(file_url, time_out, process)
        frame_list = pull_stream.get_frame_list()
        for i in frame_list:
            print(i)
            break

    def test_local_file2(self):
        file_url = "resources/video/1280_720_30f_1min.mp4"
        time_out = 1
        pull_stream = PullStream(file_url, time_out, process2)
        frame_list = pull_stream.get_frame_list()
        print(frame_list)

if __name__ == "__main__":
    unittest.main()