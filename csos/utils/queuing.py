import concurrent.futures
import sys
import pyaudio as pa
import wave

MAX_WORKERS = 1  # 最大并发线程数

# 语音播报
def play_audio(text):
    import csos.settings
    pre_path = csos.settings.STATIC_AUDIO_FILE
    p = pa.PyAudio()
    filePath = pre_path + "\\" + text + ".wav"
    print(filePath)
    wf = wave.open(filePath, 'rb')
    wf_data = wf.readframes(wf.getnframes())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    def play():
        stream.write(wf_data)
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()

    play()

def play_audio_cmd(filepath):
    p = pa.PyAudio()
    wf = wave.open(filepath, 'rb')
    wf_data = wf.readframes(wf.getnframes())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    def play():
        stream.write(wf_data)
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()

    play()


def device_list():
    import pyaudio
    p = pyaudio.PyAudio()
    # print(p)
    device_index = 0

    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info.get('name', '').find('i2s') != -1:
            print(device_info)
            device_index = device_info.get('index')

    print('Selected device index: {}'.format(device_index))


if __name__ == "__main__":
    # print(sys.argv)
    play_audio_cmd(sys.argv[1])

