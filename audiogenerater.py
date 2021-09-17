import pyttsx3
import matplotlib.pyplot as plt
import librosa.display
import librosa

# 生成读数音频
def audio_generater(audio_content, rate=120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.save_to_file(audio_content, 'dushu.wav')
    engine.runAndWait()

# 生成音频波形图
def audio_wave(audio_file):
    x, sr = librosa.load(audio_file)
    plt.figure(figsize=(16, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.show()


if __name__ == "__main__":
    list = [str(i) for i in range(0, 120)]
    audio_content = ' '.join(list)
    audio_generater(audio_content)

    audioFile = 'renshengdushu.wav'
    audio_wave(audioFile)
