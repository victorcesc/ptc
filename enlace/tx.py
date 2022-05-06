#!/usr/bin/python3

from serial import Serial
import sys

try:
  porta = sys.argv[1]
  arq = sys.argv[2]
except:
  print('Uso: %s porta_serial' % sys.argv[0])
  sys.exit(0)

try:
  p = Serial(porta, 9600, timeout=10)
except Exception as e:
  print('Não conseguiu acessar a porta serial', e)
  sys.exit(0)

msg = 'um teste ...\r\n'
f = open(arq,'rb')
#print(f.read().encode('ascii'))


n = p.write(f.read())
print('Enviou %d bytes' % n)

teste = input('Digite ENTER para terminar:')

sys.exit(0)

