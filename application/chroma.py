from essentia.streaming import VectorInput, FrameCutter, Chromagram
from essentia import Pool, run

def chroma(filename, fs=44100, frame_size=32768):
    audio = MonoLoader(filename=filename)()
    hop_size = frame_size // 2
    vectorinput = VectorInput(audio)
    framecutter = FrameCutter(frameSize=frame_size, hopSize=hop_size)
    chromagram = Chromagram(sampleRate=fs)
    pool = Pool()
    vectorinput.data >> framecutter.signal
    framecutter.frame >> chromagram.frame
    chromagram.chromagram >> (pool, 'chromagram')
    run(vectorinput)
    return pool['chromagram']