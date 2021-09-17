import subprocess
import os
import platform
import json

# 支持的操作系统
SYSTEMS = ["Linux", "Darwin", "Windows"]

class FFprobe():

    def pull_stream(self, file_path):
        pwd = os.path.dirname(__file__)
        system = platform.system()
        if system not in SYSTEMS:
            raise OSError("only support Linux , Darwin, Windows, now is %s" % system)
        self.ffprobe = os.path.abspath(os.path.join(pwd, "../lib/bin", system, "ffprobe"))
        cmd = [self.ffprobe, "-print_format","json", "-show_format", "-show_streams", file_path]
        pull_process = subprocess.Popen(cmd,  encoding="utf-8",stdout = subprocess.PIPE,stdin = subprocess.PIPE, stderr = subprocess.PIPE)
        try:
            out,err  = pull_process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            # todo
            raise

        if bytes(out,encoding="utf-8") == b'{\n\n}\n':
            err_info = err.split('\n')[-2]
            # todo
            print(err_info)
            return

        self.info = json.loads(out)

    def get_info(self):
        return self.info


if __name__ == "__main__":
    file_path = "example/resources/video/1280_720_30f_1min.mp4"
    FFprobe().pull_stream(file_path)