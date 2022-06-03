import telnetlib
import time

ENT = '\r\n'
HOST = '127.0.0.1'
PORT = 7356

GET_FREQ = 'f'
SET_FREQ = 'F '
GET_STR= 'l'
GET_SQL= 'l SQL'
SET_SQL= 'L SQL '
GET_REC= 'u RECORD'
SET_REC= 'U RECORD '

def cmd(string):
  return (string + ENT).encode('ascii')

def get_freq():
  return get(GET_FREQ)

def set_freq(freq):
  return set(freq, SET_FREQ, GET_FREQ)

def get_sql():
  return get(GET_SQL)

def get_strength():
  tn = telnetlib.Telnet(HOST, PORT)
  sum = 0
  for i in range(3):
    tn.write(cmd(GET_STR))
    sql = tn.read_some().decode('ascii')
    sum += float(sql)
    time.sleep(0.2)
  return str(sum/3)

def set_sql(sql):
  return set(sql, SET_SQL, GET_SQL)

def get_rec():
  return get(GET_REC)

def set_rec(rec):
  return set(rec, SET_REC, GET_REC)

def get(c):
  tn = telnetlib.Telnet(HOST, PORT)
  tn.write(cmd(c))
  return tn.read_some().decode('ascii')

def set(v, c, g):
  tn = telnetlib.Telnet(HOST, PORT)
  tn.write(cmd(c + v))
  tn.read_some().decode('ascii')
  tn.write(cmd(g))
  return tn.read_some().decode('ascii')