#TODO 使用Python实现，对着电脑哄一声，自动打开浏览器，打开百度。

import pyaudio
import wave
from tqdm import tqdm
import speech_recognition as sr
import webbrowser


def get_wav(output_path, RECORD_SECONDS):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = output_path

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in tqdm(range(0, int(RATE / CHUNK * RECORD_SECONDS)), "开始录音:"):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_txt(wav_path):
    # 文件路径
    print(f"打开音频路径：{wav_path}")
    harvard = sr.AudioFile(wav_path)
    r = sr.Recognizer()
    with harvard as source:
        audio = r.record(source)
    print(type(audio))
    text = r.recognize_google(audio, language="zh-CN")

    temp = text.split()
    txt = "".join(temp)
    print(txt)
    with open("./output/wav.txt", "w", encoding="utf-8") as f:
        f.write(txt)


def open_url():
    with open("./output/wav.txt", "r", encoding="utf-8") as f:
        word = f.read()
        if word == "打开百度":
            print("True")
            webbrowser.open("www.baidu.com", new=0, autoraise=True)


def run(output_path: str, record_seconds: int):
    get_wav(output_path=output_path, RECORD_SECONDS=3)
    get_txt(wav_path=output_path)
    open_url()


if __name__ == '__main__':
    # get_wav(output_path="output/wav/output.wav", RECORD_SECONDS=3)
    # get_txt(wav_path="../show_me_code/output/wav/test3.wav")
    open_url()
