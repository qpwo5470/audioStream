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

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
while True:
    data = stream.read(CHUNK)
    sock.sendto(b''.join(data), (IP, PORT))


stream.stop_stream()
stream.close()
sock.close()