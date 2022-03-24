import array
import numpy as np
import os


def readPCM(fileName):
    file = open(fileName,'rb')
    pcm_data = array.array('h')
    size = int(os.path.getsize(fileName) / pcm_data.itemsize)
    pcm_data.fromfile(file, size)
    file.close()
    return pcm_data


if __name__ == '__main__':
    num = len(readPCM('audio.pcm'))/2
    print(int(num))
    print(readPCM('audio.pcm')[int(num)])
