import av
import time

class PullStream():
    # process 是每一帧的处理函数，输入为 PIL.Image 类型，输出为一个对象和一个信号（控制是否继续读帧，True 继续，False 暂停）
    def __init__(self, file_url, timeout, process=None, save_img_num = 10):
        self.frame_list = []
        time_start = int(time.time())
        while True:
            if int(time.time()) - time_start > timeout:
                break
            try:
                container = av.open(file_url, timeout=2)
                for frame in container.decode(video=0):
                    if int(time.time()) - time_start > timeout:
                        break
                    img = frame.to_image()
                    if process != None:
                        img_info , f = process(img)
                        self.frame_list.append(img_info)
                        if not f :
                            return
                    else:
                        if len(self.frame_list) > save_img_num:
                            return
                        self.frame_list.append(img)
            except EOFError:
                print("EOF!!!!")
                time.sleep(1)  # 避免大量循环，隔一秒再啦
            except Exception as e:
                print("other ERROR!!! %s", e)
                time.sleep(1)  # 避免大量循环，隔一秒再啦

    def get_frame_list(self):
        return self.frame_list
