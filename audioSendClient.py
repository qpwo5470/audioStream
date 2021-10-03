import pyaudio
import socket

IP = '192.168.55.183'
PORT = 15252

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if ('스테레오 믹스' in dev['name'] or 'Stereo Mix' in dev['name']) and dev['hostApi'] == 0:
        dev_index = dev['index']

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = dev_index,
                frames_per_buffer=CHUNK)


while True:
    data = stream.read(CHUNK)
    sock.sendto(data, (IP, PORT))


stream.stop_stream()
stream.close()
sock.close()