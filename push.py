import subprocess
import os
import platform
import time


# 支持的操作系统
SYSTEMS = ["Linux", "Darwin", "Windows"]

class PushStream():
    def __init__(self,push_url,file_path, cmd=None):
        pwd = os.path.dirname(__file__)
        system = platform.system()
        if system not in SYSTEMS:
            raise OSError("only support Linux , Darwin, Windows, now is %s" % system)
        self.ffmpeg = os.path.abspath(os.path.join(pwd, "../lib/bin", system, "ffmpeg"))

        # ffmpeg -re -i  file_path  -c copy -f flv  push_url
        if cmd == None:
            cmd = [self.ffmpeg, "-re", "--i", file_path, "-c", "copy", "-f", "flv", push_url]
            print(" ".join(cmd))
        print("start push stream")
        self.push_process = subprocess.Popen(cmd, encoding="utf-8",stdout = subprocess.PIPE,stdin = subprocess.PIPE, stderr = subprocess.PIPE)

    def stop(self):
        if self.push_process != None and self.push_process.poll() == None:
            print("stop push stream")
            self.push_process.kill()

    # 命令执行一秒，若结束，则返回错误； 若未结束，则让命令继续执行
    def status(self):
        try:
            out,err = self.push_process.communicate(timeout=1)
            print("push stream cmd error")
            return False, err
        except subprocess.TimeoutExpired:
            return True, None

    def __del__(self):
        if self.push_process != None and self.push_process.poll() == None:
            print("stop push stream")
            self.push_process.kill()

if __name__ == "__main__":
    push_url = "rtmp://startpush001.elementtest.org/live/test202109011900?txSecret=82863ad9c017c4fff575c811c210e065&txTime=6130AEAB"
    file_path = "/example/resources/video/1280_720_30f_1min.mp4"
    push_stream = PushStream(push_url, file_path)
    status, err = push_stream.status()
    print(status)
    print(err)
    for i in range(0,10):
        print(1)
        time.sleep(1)
    push_stream.stop()