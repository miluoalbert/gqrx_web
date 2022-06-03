import telnetlib
import time

ENT = '\r\n'
HOST = '127.0.0.1'
PORT = 7356

GET_FREQ = 'f'
SET_FREQ = 'F '

tn = telnetlib.Telnet(HOST, PORT)
tn.write(('f' + ENT).encode('ascii'))
savefreq = tn.read_some().decode('ascii')

print(savefreq)