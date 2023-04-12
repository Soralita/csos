import pyaudio as pa
import wave

pre_path = "../static/audio/"
p = pa.PyAudio()

# 语音播报
def play_audio(text):
    filePath = pre_path + text + ".wav"
    wf = wave.open(filePath, 'rb')
    wf_data = wf.readframes(wf.getnframes())
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    stream.write(wf_data)
    stream.stop_stream()
    stream.close()
    wf.close()
    p.terminate()