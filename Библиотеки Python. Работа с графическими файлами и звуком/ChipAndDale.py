import wave
import struct


def chip_and_dale(number):
    source = wave.open('in.wav', mode='rb')
    dest = wave.open('out.wav', mode='wb')
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack(f'<{frames_count}h', source.readframes(frames_count))
    newdata = data[::number]
    newframes = struct.pack(f'<{len(newdata)}h', *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()


if __name__ == '__main__':
    chip_and_dale(2)
